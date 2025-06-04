# ==================================================
# No.4_当せん返還消込応答_マッピング
# ==================================================
import time
import toto_constant
from toto_library import *

def get_X_payback_amt_for_refund_map_clearing(bi_int:int) -> str:
    """
    No.4_当せん返還消込応答_マッピング
    払戻金額の取得（払戻）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        str: 数字に対応する文字列
    """
    resp = req_res_map_flexible({
        0: "0000000000",
        1: "0000003500",
        2: "0000005000",
        3: "9999999999"
    }, bi_int, "9999999999")
    return resp


def get_X_shori_kekka_for_refund_cancel_map_clearing(bi_int:int) -> (str, int):
    """
    No.4_当せん返還消込応答_マッピング
    処理結果の取得（払戻取消）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        (str, int): 数字に対応する文字列, 数字に対応する数字
    """
    resp = req_res_map_flexible({
        0: ("00", 200, False),  # "00"：正常
        1: ("16", 400, False),  # "16"：SEJセンター混雑エラー
        2: ("99", 400, False),  # "99"：その他エラー(400)
        3: ("99", 500, False),  # "99"：その他エラー(500)
        4: ("00", 200, True),   # "00"：タイムアウト(正常)
        5: ("99", 500, True)    # "99"：タイムアウト(その他エラー500)
    }, bi_int, ("00", 200, False))
    if resp[2]:  # タイムアウト処理
        time.sleep(toto_constant.TIMEOUT_SEC)
    return resp[:2]


def get_X_outou_kekka_for_refund_cancel_map_clearing(bi_int:int) -> str:
    """
    No.4_当せん返還消込応答_マッピング
    応答結果の取得（払戻取消）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        str: 数字に対応する文字列
    """
    resp = req_res_map_flexible({
        0: "00",  # "00"：正常応答
        1: "04",  # "04"：未払戻エラー
        2: "06",  # "06"：払戻済エラー
        3: "07",  # "07"：払戻期限切れエラー
        4: "08",  # "08"：取消済みエラー
        5: "99"   # "99"：その他エラー
    }, bi_int, "00")
    return resp


def get_X_payback_amt_for_refund_cancel_map_clearing(bi_int:int) -> str:
    """
    No.4_当せん返還消込応答_マッピング
    払戻金額の取得（払戻取消）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        str: 数字に対応する文字列
    """
    resp = req_res_map_flexible({
        0: "0000000000",
        1: "0000003500",
        2: "0000005000",
        3: "9999999999"
    }, bi_int, "9999999999")
    return resp


def get_X_shori_kekka_for_clearing_map_clearing(bi_int:int) -> (str, int):
    """
    No.4_当せん返還消込応答_マッピング
    処理結果の取得（当せん返還消込）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        (str, int): 数字に対応する文字列, 数字に対応する数字
    """
    resp = req_res_map_flexible({
        0: ("00", 200, False),  # 正常
        1: ("15", 400, False),  # タイムアウトエラー
        2: ("16", 400, False),  # SEJセンター混雑エラー
        3: ("99", 400, False),  # その他エラー(400)
        4: ("99", 500, False),  # その他エラー(500)
        5: ("00", 200, True),   # タイムアウト(正常)
        6: ("99", 500, True)    # タイムアウト(その他エラー500)
    }, bi_int, ("00", 200, False))
    if resp[2]:  # タイムアウト処理
        time.sleep(toto_constant.TIMEOUT_SEC)
    return resp[:2]


def get_X_outou_kekka_for_clearing_map_clearing(bi_int:int) -> str:
    """
    No.4_当せん返還消込応答_マッピング
    応答結果の取得（当せん返還消込）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        str: 数字に対応する文字列
    """
    resp = req_res_map_flexible({
        0: "00",  # 正常応答
        1: "01",  # 検索キーエラー
        2: "04",  # 未払戻エラー
        3: "06",  # 払戻済エラー
        4: "07",  # 払戻期限切れエラー
        5: "08",  # 取消済みエラー
        6: "11",  # totoセンター接続エラー
        7: "12",  # totoセンター混雑エラー
        8: "13",  # totoセンターアプリエラー
        9: "14",  # totoセンター通信その他エラー
        10: "99"   # その他エラー
    }, bi_int, "00")
    return resp


def get_X_toto_kekka_for_clearing_map_clearing(bi_int:int) -> str:
    """
    No.4_当せん返還消込応答_マッピング
    totoセンター応答結果の取得（当せん返還消込）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        str: 数字に対応する文字列
    """
    resp = req_res_map_flexible({
        0: "",       # 空タグ
        1: "000000", # "000000"
        2: "000001", # "000001"
        3: "000002"  # "000002"
    }, bi_int, "")
    return resp
