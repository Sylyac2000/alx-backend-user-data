#!/usr/bin/env python3
"""This module is about Regex-ing
"""
from typing import List, Tuple
import re
import logging


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

    def __init__(self, fields: Tuple[str, str, str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.__fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ filter and format logging message"""
        log_msg = super(RedactingFormatter, self).format(record)
        message = filter_datum(list(self.__fields),
                               RedactingFormatter.REDACTION,
                               log_msg,
                               RedactingFormatter.SEPARATOR)
        return message
