#!/usr/bin/env python3
"""This module is about Regex-ing
"""
from typing import List
import re
import logging
import os
import mysql.connector


PII_FIELDS = ('name', 'password', 'phone', 'ssn', 'email')


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """ return an obfuscated log message
    """
    for field in fields:
        message = re.sub(field+'=.*?'+separator,
                         field+'='+redaction+separator, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.__fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ filter and format logging message"""
        message = filter_datum(list(self.__fields),
                               RedactingFormatter.REDACTION,
                               super(RedactingFormatter, self).format(record),
                               RedactingFormatter.SEPARATOR)
        return message


def get_logger() -> logging.Logger:
    """ returns a logger object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """return a mysql connector
    """
    dbhost = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    dbname = os.getenv("PERSONAL_DATA_DB_NAME", "")
    dbuser = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    dbpwd = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    connection = mysql.connector.connect(
        host=dbhost,
        port=3306,
        user=dbuser,
        password=dbpwd,
        database=dbname,
    )
    return connection


def main():
    """ read and filter data """
    dbconnection = get_db()

    logger = get_logger()
    cursor = dbconnection.cursor()
    cursor.execute("SELECT * FROM users;")
    fields = cursor.column_names
    for row in cursor:
        message = "".join("{}={}; ".format(k, v) for k, v in zip(fields, row))
        logger.info(message.strip())
    cursor.close()
    dbconnection.close()


if __name__ == '__main__':
    main()
