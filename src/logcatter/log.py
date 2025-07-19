"""
Provides a static, Android Logcat-style logging interface.

This module offers a simple, zero-configuration facade over Python's standard
logging module, designed to be instantly familiar to Android developers.
"""

import logging

from logcatter.formatter import LogFormatter
from logcatter.logcat import Logcat
from logcatter.level import LEVEL_VERBOSE, LEVEL_DEBUG, LEVEL_INFO, LEVEL_WARNING, LEVEL_ERROR, LEVEL_FATAL


class Log:
    """
    A static utility class that provides an Android Logcat-like logging interface.

    This class is not meant to be instantiated. It offers a set of static methods
    (e.g., `d`, `i`, `w`, `e`) that wrap the standard Python `logging` module
    to provide a simple, zero-configuration logging experience. It automatically
    configures a logger that outputs messages in a format similar to Android's
    Logcat, including automatic tagging with the calling filename.
    """

    VERBOSE = LEVEL_VERBOSE
    DEBUG = LEVEL_DEBUG
    INFO = LEVEL_INFO
    WARNING = LEVEL_WARNING
    ERROR = LEVEL_ERROR
    FATAL = LEVEL_FATAL

    @staticmethod
    def getLogger() -> logging.Logger:
        """
        Retrieves the singleton logger instance for the application.

        On the first call, it initializes the logger with a `StreamHandler` and
        the custom `LogFormatter`. Subsequent calls return the same logger instance
        without adding more handlers, preventing duplicate log messages.

        Returns:
            logging.Logger: The configured logger instance.
        """
        logger = logging.getLogger(Logcat.NAME)
        if not logger.hasHandlers():
            logger.setLevel(logging.DEBUG)
            handler = logging.StreamHandler()
            handler.setFormatter(LogFormatter())
            logger.addHandler(handler)
        return logger

    @staticmethod
    def setLevel(level: int | str):
        """
        Sets the logging level for the application's logger.

        Messages with a severity lower than `level` will be ignored.

        Args:
            level (int | str): The minimum level of severity to log.
                Can be an integer constant (e.g., `logging.INFO`) or its string
                representation (e.g., "INFO").
        """
        Log.getLogger().setLevel(level)

    @staticmethod
    def is_verbose():
        """
        Checks the logging level is `Log.VERBOSE` or below.
        :return:
            bool: `True` when the level is `Log.VERBOSE` or below, `False` otherwise.
        """
        return Log.getLogger().level <= Log.VERBOSE

    @staticmethod
    def is_quiet():
        """
        Checks the logging level is `Log.WARNING` or above.
        :return:
            bool: `True` when the level is `Log.WARNING` or above, `False` otherwise.
        """
        return Log.getLogger().level >= Log.WARNING

    @staticmethod
    def is_silent():
        """
        Checks the logging level is greater than `Log.FATAL`.
        :return:
            bool: `True` when the level is greater than `Log.FATAL`, `False` otherwise.
        """
        return Log.getLogger().level > Log.FATAL

    @staticmethod
    def _log(
            level: int,
            msg: str,
            *args,
            e: object | None = None,
            s: bool = False,
            **kwargs,
    ):
        """
        Logs a message with the given level.

        Args:
            :param level: Level of the message.
            :param msg: The message to be logged.
            :param e: Exception object to logged together.
            :param s: Whether stacktrace or not
        """
        messages = msg.split('\n')
        for index, message in enumerate(messages):
            Log.getLogger().log(
                level,
                message,
                *args,
                stacklevel=3,
                exc_info=e if index == len(messages)-1 else None,
                stack_info=s if index == len(messages)-1 else False,
                **kwargs,
            )

    @staticmethod
    def v(
            msg: str,
            *args,
            e: object | None = None,
            s: bool = False,
            **kwargs,
    ):
        """
        Logs a message with the VERBOSE level.

        Args:
            :param msg: The message to be logged.
            :param e: Exception object to logged together.
            :param s: Whether stacktrace or not
        """
        Log._log(
            Log.VERBOSE,
            msg,
            *args,
            e=e,
            s=s,
            **kwargs,
        )

    @staticmethod
    def d(
            msg: str,
            *args,
            e: object | None = None,
            s: bool = False,
            **kwargs,
    ):
        """
        Logs a message with the DEBUG level.

        Args:
            :param msg: The message to be logged.
            :param e: Exception object to logged together.
            :param s: Whether stacktrace or not
        """
        Log._log(
            Log.DEBUG,
            msg,
            *args,
            e=e,
            s=s,
            **kwargs,
        )

    @staticmethod
    def i(
            msg: str,
            *args,
            e: object | None = None,
            s: bool = False,
            **kwargs,
    ):
        """
        Logs a message with the INFO level.

        Args:
            :param msg: The message to be logged.
            :param e: Exception object to logged together.
            :param s: Whether stacktrace or not
        """
        Log._log(
            Log.INFO,
            msg,
            *args,
            e=e,
            s=s,
            **kwargs,
        )

    @staticmethod
    def w(
            msg: str,
            *args,
            e: object | None = None,
            s: bool = False,
            **kwargs,
    ):
        """
        Logs a message with the WARNING level.

        Args:
            :param msg: The message to be logged.
            :param e: Exception object to logged together.
            :param s: Whether stacktrace or not
        """
        Log._log(
            Log.WARNING,
            msg,
            *args,
            e=e,
            s=s,
            **kwargs,
        )

    @staticmethod
    def e(
            msg: str,
            *args,
            e: object | None = None,
            s: bool = False,
            **kwargs,
    ):
        """
        Logs a message with the ERROR level.

        Args:
            :param msg: The message to be logged.
            :param e: Exception object to logged together.
            :param s: Whether stacktrace or not
        """
        Log._log(
            Log.ERROR,
            msg,
            *args,
            e=e,
            s=s,
            **kwargs,
        )

    @staticmethod
    def f(
            msg: str,
            *args,
            e: object | None = None,
            s: bool = False,
            **kwargs,
    ):
        """
        Logs a message with the CRITICAL level.

        Args:
            :param msg: The message to be logged.
            :param e: Exception object to logged together.
            :param s: Whether stacktrace or not
        """
        Log._log(
            Log.FATAL,
            msg,
            *args,
            e=e,
            s=s,
            **kwargs,
        )
