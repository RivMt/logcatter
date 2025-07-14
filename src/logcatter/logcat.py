import logging


class Logcat(logging.Logger):
    NAME = "logcat"

    def __init__(self):
        super().__init__(name=self.NAME, level=logging.DEBUG)
