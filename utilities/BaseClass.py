import logging

import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:
    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
    def getLogger(self):
        logger = logging.getLogger(__name__)

        logger.addHandler(BaseClass.fileHandler)  # fileHandler object

        logger.setLevel(logging.DEBUG)

        return logger
