# ==================================================
# No.3_払戻・払戻取消応答_マッピング
# ==================================================
import time
import toto_constant
from toto_library import *

def get_X_shori_kekka_for_refund_map_refund(bi_int:int) -> (str, int):
    """
    No.3_払戻・払戻取消応答_マッピング
    処理結果の取得（払戻）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        (str, int): 数字に対応する文字列, 数字に対応する数字
    """
    resp = req_res_map_flexible({
        0: ("00", 200, False),  # "00"：正常
        1: ("14", 400, False),  # "14"：サービス時間帯エラー
        2: ("16", 400, False),  # "16"：SEJセンター混雑エラー
        3: ("99", 400, False),  # "99"：その他エラー(400)
        4: ("99", 500, False),  # "99"：その他エラー(500)
        5: ("00", 200, True),  # "00"：タイムアウト(正常)
        6: ("99", 500, True)   # "99"：タイムアウト(その他エラー500)
    }, bi_int, ("00", 200, False))
    if resp[2]:  # タイムアウト処理
        time.sleep(toto_constant.TIMEOUT_SEC)
    return resp[:2]


def get_X_outou_kekka_for_refund_map_refund(bi_int:int) -> str:
    """
    No.3_払戻・払戻取消応答_マッピング
    応答結果の取得（払戻）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        str: 数字に対応する文字列
    """
    resp = req_res_map_flexible({
        0: "00",  # 正常応答
        1: "01",  # 検索キーエラー
        2: "02",  # 店舗チェックエラー
        3: "03",  # 取引停止中エラー
        4: "05",  # 払戻中エラー
        5: "06",  # 払戻済エラー
        6: "07",  # 払戻期限切れエラー
        7: "08",  # 取消済みエラー
        8: "99"   # その他エラー
    }, bi_int, "00")
    return resp


def get_X_payback_amt_for_refund_map_refund(bi_int:int) -> str:
    """
    No.3_払戻・払戻取消応答_マッピング
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


def get_X_saiso_kbn_for_refund_map_refund(bi_int:int) -> str:
    """
    No.3_払戻・払戻取消応答_マッピング
    再送区分の取得（払戻）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        str: 数字に対応する文字列
    """
    resp = req_res_map_flexible({
        0: "0",  # "0"：再送正常
        1: "1"   # "1"：再送異常
    }, bi_int, "0")
    return resp


def get_X_shori_kekka_for_refund_cancel_map_refund(bi_int:int) -> (str, int):
    """
    No.3_払戻・払戻取消応答_マッピング
    処理結果の取得（払戻取消）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        (str, int): 数字に対応する文字列, 数字に対応する数字
    """
    resp = req_res_map_flexible({
        0: ("00", 200, False),  # 正常
        1: ("16", 400, False),  # SEJセンター混雑エラー
        2: ("99", 400, False),  # その他エラー(400)
        3: ("99", 500, False),  # その他エラー(500)
        4: ("00", 200, True),   # タイムアウト(正常)
        5: ("99", 500, True)    # タイムアウト(その他エラー500)
    }, bi_int, ("00", 200, False))
    if resp[2]:  # タイムアウト処理
        time.sleep(toto_constant.TIMEOUT_SEC)
    return resp[:2]


def get_X_outou_kekka_for_refund_cancel_map_refund(bi_int:int) -> str:
    """
    No.3_払戻・払戻取消応答_マッピング
    応答結果の取得（払戻取消）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        str: 数字に対応する文字列
    """
    resp = req_res_map_flexible({
        0: "00",  # 正常応答
        1: "04",  # 未払戻エラー
        2: "06",  # 払戻済エラー
        3: "07",  # 払戻期限切れエラー
        4: "08",  # 取消済みエラー
        5: "99"   # その他エラー
    }, bi_int, "00")
    return resp


def get_X_payback_amt_for_refund_cancel_map_refund(bi_int:int) -> str:
    """
    No.3_払戻・払戻取消応答_マッピング
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


def get_X_saiso_kbn_for_refund_cancel_map_refund(bi_int:int) -> str:
    """
    No.3_払戻・払戻取消応答_マッピング
    再送区分の取得（払戻取消）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        str: 数字に対応する文字列
    """
    resp = req_res_map_flexible({
        0: "0",  # "0"：再送正常
        1: "1"   # "1"：再送異常
    }, bi_int, "0")
    return resp


def get_X_shop_id_for_refund_cancel_map_refund(bi_int:int) -> str:
    """
    No.3_払戻・払戻取消応答_マッピング
    ショップIDの取得（払戻取消）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        str: 数字に対応する文字列
    """
    resp = req_res_map_flexible({
        0: "00000",
        1: "30514",
        2: "30801",
        3: "99999"
    }, bi_int, "00000")
    return resp
