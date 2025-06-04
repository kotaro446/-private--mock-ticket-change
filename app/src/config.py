import os


class Config:
    _instance = None

    HISTORY_DIR: str = "../histories"
    LOG_LEVEL: str = "DEBUG"

    def __init__(self):
        # 環境変数から読み込み
        self.history_dir = self.getenv("HISTORY_DIR", Config.HISTORY_DIR)
        self.log_level = self.getenv("LOG_LEVEL", Config.LOG_LEVEL)

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Config()
        return cls._instance

    @staticmethod
    def getenv(key: str, default=None, converter=None):
        # 環境変数から取得
        s = os.getenv(key)
        # 値が空かつデフォルト値がある場合はデフォルト値をかえす
        if (s is None or s.strip() == "") and default is not None:
            return default
        # 値が空でない場合かつ変換器がある場合は型変換
        if s is not None and converter is not None:
            return converter(s)
        # 上記以外はそのまま返却
        return s
