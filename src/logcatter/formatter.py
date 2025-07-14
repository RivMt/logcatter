import logging
import time


class LogFormatter(logging.Formatter):

    COLOR = {
        logging.DEBUG: '\x1b[37;20m',
        logging.INFO: '\x1b[32;20m',
        logging.WARNING: '\x1b[33;20m',
        logging.ERROR: '\x1b[31;20m',
        logging.CRITICAL: '\x1b[31;1m',
    }

    def format(self, record):
        # Default message
        asctime = self.formatTime(record)
        level = record.levelname.upper()[0]
        tag = record.filename
        message = record.getMessage()
        color = self.COLOR.get(record.levelno)
        color_reset = self.COLOR.get(logging.DEBUG)
        result = f"{color}{asctime} [{level}/{tag}] {message}{color_reset}"
        # Exception and errors
        if record.exc_info:
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)
        if record.exc_text:
            if result[-1:] != '\n':
                result += '\n'
            result += f"{color}{record.exc_text}{color_reset}"
        # Stack
        if record.stack_info:
            if result[-1:] != '\n':
                result += '\n'
            result += f"{color}{self.formatStack(record.stack_info)}{color_reset}"
        return result

    def formatTime(self, record, datefmt = None):
        ct = self.converter(record.created)
        if datefmt:
            s = time.strftime(datefmt, ct)
        else:
            t = time.strftime("%Y-%m-%d %H:%M:%S", ct)
            s = f"{t} {int(record.msecs):03d}"
        return s
