import logging
import time


class GMTFormatter(logging.Formatter):
    converter = time.gmtime  # type: ignore
