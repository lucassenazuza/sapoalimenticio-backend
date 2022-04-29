import logging
import os
from logging.handlers import RotatingFileHandler

from settings import ROOT_PATH

LOG_DIR = os.path.join(ROOT_PATH, "logs")
LOG_FILE = os.path.join(LOG_DIR, "logfile.log")


class Log(object):
    def __init__(self, name):
        logger = logging.getLogger(name)
        self._logger = logger
        self.config()

    @staticmethod
    def _create_path_if_not_exists() -> None:
        """Create Log path if not exists"""
        if not os.path.exists(LOG_DIR):
            os.mkdir(LOG_DIR)

    def config(self):
        self._create_path_if_not_exists()

        formatter = logging.Formatter(
            "{asctime} : {levelname:8s} : {name:24s} : {message}", style="{"
        )

        self._logger.setLevel(logging.DEBUG)

        # File Handler
        file_handler = RotatingFileHandler(
            LOG_FILE, maxBytes=3145728, backupCount=5
        )
        file_handler.setFormatter(formatter)
        self._logger.addHandler(file_handler)

        # Console Handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self._logger.addHandler(console_handler)

    def debug(self, msg):
        self._logger.debug(msg=msg)

    def info(self, msg):
        self._logger.info(msg=msg)

    def warning(self, msg):
        self._logger.warning(msg=msg)

    def error(self, msg, show_alert=True):
        self._logger.error(msg=msg)
        if show_alert:
            # alert(text=msg, title="Erro")
            ...
