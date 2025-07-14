import logging

from logcatter.formatter import LogFormatter
from logcatter.logcat import Logcat


class Log:

    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

    @staticmethod
    def getLogger() -> logging.Logger:
        logger = logging.getLogger(Logcat.NAME)
        if not logger.hasHandlers():
            handler = logging.StreamHandler()
            handler.setFormatter(LogFormatter())
            logger.addHandler(handler)
        return logger

    @staticmethod
    def setLevel(level: int | str):
        Log.getLogger().setLevel(level)

    @staticmethod
    def d(msg: str, *args, **kwargs):
        Log.getLogger().debug(msg, *args, stacklevel=2, **kwargs)

    @staticmethod
    def i(msg: str, *args, **kwargs):
        Log.getLogger().info(msg, *args, stacklevel=2, **kwargs)

    @staticmethod
    def w(msg: str, *args, **kwargs):
        Log.getLogger().warning(msg, *args, stacklevel=2, **kwargs)

    @staticmethod
    def e(
            msg: str,
            *args,
            e: object | None = None,
            s: bool = False,
            **kwargs,
    ):
        Log.getLogger().error(
            msg,
            *args,
            stacklevel=2,
            exc_info=e,
            stack_info=s,
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
        Log.getLogger().critical(
            msg,
            *args,
            stacklevel=2,
            exc_info=e,
            stack_info=s,
            **kwargs,
        )
