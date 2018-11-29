import logging


class CustomLogger:
    innerLogger = logging.getLogger('spam_application')
    innerLogger.setLevel(logging.DEBUG)

    fh = logging.FileHandler('sites.log')
    fh.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    innerLogger.addHandler(fh)
    innerLogger.addHandler(ch)

    def error(self, message: str):
        self.innerLogger.error(message)

    def info(self, message: str):
        self.innerLogger.info(message)

    def debug(self, message: str):
        self.innerLogger.debug(message)
