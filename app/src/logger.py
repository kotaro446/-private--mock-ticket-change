from config import Config

CONFIG = Config.get_instance()


class Logger:
    def __init__(self):
        self._logger = None

    def setup_logger(self, app):
        self._logger = app.logger
        self._logger.setLevel(CONFIG.log_level)

    # debugやinfoなどのログレベルごとの出力をself._loggerに委譲
    def __getattr__(self, name):
        return getattr(self._logger, name)


_logger = Logger()


def get_logger():
    return _logger
