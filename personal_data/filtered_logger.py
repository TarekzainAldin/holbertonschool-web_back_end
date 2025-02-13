#!/usr/bin/env python3
"""
Module for filtering and obfuscating log messages.
"""
import logging
import re
from typing import List, Tuple
import mysql
from mysql.connector import Error
import os


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


PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


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


def get_logger() -> logging.Logger:
    """
    Creates and returns a logger named "user_data".
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connect to the MySQL database using credentials from environment variables.

    Returns:
        mysql.connector.connection.MySQLConnection: Database connector object.
    """
    # Get credentials from environment variables
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "1")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    # Connect to the database
    try:
        db = mysql.connector.connect(
            user=username,
            password=password,
            host=host,
            database=db_name
        )
        return db
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        raise


def main():
    """
    Main function to retrieve data from the users table and log it securely.
    """
    # Configure logger
    logger = get_logger()

    # Connect to database
    db = get_db()
    cursor = db.cursor()

    try:
        # Retrieve all rows from users table
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

        # Log each row securely
        for row in rows:
            # Construct the log message
            log_message = "; ".join(
                [f"{field}={value}" for field, value in zip(
                    cursor.column_names, row)])
            log_message += ";"  # Add semicolon at the end
            logger.info(log_message)

    except mysql.connector.Error as err:
        logger.error(f"Error fetching data from MySQL: {err}")

    finally:
        # Clean up resources
        cursor.close()
        db.close()


if __name__ == "__main__":
    main()
