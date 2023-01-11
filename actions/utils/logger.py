import logging
import os

LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'DEBUG')


def decode_logging_level(logging_level):
    if logging_level == 'DEBUG':
        return logging.DEBUG
    elif logging_level == 'INFO':
        return logging.INFO
    elif logging_level == 'WARNING':
        return logging.WARNING
    elif logging_level == 'ERROR':
        return logging.ERROR
    elif logging_level == 'CRITICAL':
        return logging.CRITICAL
    return logging.NOTSET

logging_level_value = decode_logging_level(LOGGING_LEVEL)

logger = logging.getLogger('global')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%dT%H:%M:%S%z')
ch.setFormatter(formatter)
logger.addHandler(ch)


def get_root_logger():
    return logger
