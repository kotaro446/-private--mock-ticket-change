import datetime
import os
import threading

from flask import request

from config import Config
from logger import get_logger

EXT = '.request'
RES_EXT = ".response"

logger = get_logger()
lock = threading.Lock()


def save_request(req: request):
    dir_name = get_and_create_save_dir(req)
    time_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    # 秒間Nアクセスまで対応可能とする
    n = 100
    n_digits = len(str(n - 1))  # 最大の数値の桁数でゼロ詰めの数字を付与したい
    for i in range(n + 1):  # +1 分は番兵用
        file_name = f"{dir_name}/{time_str}-{str(i + 1).zfill(n_digits)}{EXT}"
        with lock:
            if os.path.exists(file_name):
                logger.debug(f"{file_name} already exists")
                continue
            if i == n:
                # エラー
                logger.debug(
                    "リクエストの保存に失敗しました。同時アクセスが多すぎてファイル名が決められなかったようです")
                return
            with open(file_name, 'wb') as f:
                break
    with open(file_name, 'wb') as f:
        full_path = os.path.abspath(file_name)
        logger.debug(f"{full_path} save start.")
        f.write(req.get_data())
        logger.debug(f"{full_path} save end.")


def get_and_create_save_dir(req: request):
    history_dir = Config.get_instance().history_dir
    api_name = req.path.strip('/').replace('/', '_')
    date_str = datetime.datetime.now().strftime('%Y%m%d')
    store = req.headers.get('original-store-code', '')
    pos = req.headers.get('pos-number', '')
    if len(store) != 0 and len(pos) != 0:
        save_dir = "/".join([history_dir, api_name, date_str, store, pos])
    elif len(store) != 0:
        save_dir = "/".join([history_dir, api_name, date_str, store, "unknown"])
    elif len(pos) != 0:
        save_dir = "/".join([history_dir, api_name, date_str, "unknown", pos])
    else:
        save_dir = "/".join([history_dir, api_name, date_str, "unknown", "unknown"])
    os.makedirs(save_dir, exist_ok=True)
    return save_dir

def save_response(req: request, res: str):
    dir_name = get_and_create_save_dir(req)
    time_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    # 秒間Nアクセスまで対応可能とする
    n = 100
    n_digits = len(str(n - 1))  # 最大の数値の桁数でゼロ詰めの数字を付与したい
    for i in range(n + 1):  # +1 分は番兵用
        file_name = f"{dir_name}/{time_str}-{str(i + 1).zfill(n_digits)}{RES_EXT}"
        with lock:
            if os.path.exists(file_name):
                logger.debug(f"{file_name} already exists")
                continue
            if i == n:
                # エラー
                logger.debug(
                    "リクエストの保存に失敗しました。同時アクセスが多すぎてファイル名が決められなかったようです")
                return
            with open(file_name, 'wb') as f:
                break
    with open(file_name, 'w') as f:
        full_path = os.path.abspath(file_name)
        logger.debug(f"{full_path} save start.")
        f.write(res)
        #pickle.dump(str_res, f)
        logger.debug(f"{full_path} save end.")