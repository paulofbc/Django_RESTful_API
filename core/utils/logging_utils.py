"""
This module is responsible for creating logs during execution time
"""

from datetime import datetime
from logging import info, basicConfig, INFO, error, ERROR, exception, DEBUG

def __log_messages__(message: str, message_type):
    """
    This function is responsible for logging messages, given a type
    :param message: The message that needs to be logged
    :param message_type: The type of the message (ERROR, INFO,...)
    :return: None
    """

    basicConfig(level=message_type)

    if message_type == ERROR:
        error(f"[{datetime.now()}] {message}")
    else:
        info(f"[{datetime.now()}] {message}")

def log_info_messages(message: str):
    """
    This function is responsible for logging information messages
    :param message: The info message
    :return: None
    """

    __log_messages__(message, INFO)

def log_error_messages(message: str):
    """
    This function is responsible for logging error messages
    :param message: The error message
    :return: None
    """

    __log_messages__(message, ERROR)

def log_debug_messages(message: str):
    """
    This function is responsible for logging error messages
    :param message: The error message
    :return: None
    """

    __log_messages__(message, DEBUG)
