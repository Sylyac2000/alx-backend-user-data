#!/usr/bin/env python3
"""This module is about Regex-ing
"""
from typing import List
import re


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """ return an obfuscated log message
    regex [^;]+: one or more characters that are not a semicolon (;)
    replacement = separator.join(f"{field}={redaction}" for field in fields)
    """
    regex = separator.join(f"{field}=[^;]+" for field in fields)
    return re.sub(regex,
                  separator.join(f"{field}={redaction}" for field in fields),
                  message)
