#!/usr/bin/env python3
"""
Module for filtering and obfuscating log messages.
"""

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


if __name__ == "__main__":
    import sys
    print(filter_datum(["password"], "***", "user=admin;password=secret", ";"))
