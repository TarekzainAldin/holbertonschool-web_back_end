#!/usr/bin/env python3
"""
Module for filtering and obfuscating log messages.
"""
import logging
import re
from typing import List


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str
) -> str:
    """
    Returns the log message with specified fields obfuscated.

    Args:
        fields (List[str]): Fields to obfuscate.
        redaction (str): Replacement string for obfuscation.
        message (str): Log message.
        separator (str): Field separator in the log message.

    Returns:
        str: Obfuscated log message.
    """
    return re.sub(
        rf'({"|".join(fields)})=[^{separator}]*',
        lambda m: f"{m.group(1)}={redaction}",
        message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize RedactingFormatter with fields to redact.
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format log record, redacting specified fields.
        """
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR
        )
        return super().format(record)


if __name__ == "__main__":
    import sys
    print(filter_datum(["password"], "***", "user=admin;password=secret", ";"))
