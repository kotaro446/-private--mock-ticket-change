# ==================================================
# No.1_購入・購入取消応答_マッピング
# ==================================================
import time
import toto_constant
from toto_library import *

def get_X_shori_kekka_for_purchase_map_purchase(bi_int:int) -> tuple[str, int]:
    """
    No.1_購入・購入取消応答_マッピング
    処理結果の取得（購入応答）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        (str, int): 数字に対応する文字列, 数字に対応する数字
    """
    resp = req_res_map_flexible({
        0: ("00", 200, False),  # 正常
        1: ("14", 400, False),  # サービス時間帯エラー
        2: ("16", 400, False),  # SEJセンター混雑エラー
        3: ("99", 400, False),  # その他エラー(400)
        4: ("99", 500, False),  # その他エラー(500)
        5: ("00", 200, True),   # タイムアウト(正常)
        6: ("99", 500, True)    # タイムアウト(その他エラー500)
    }, bi_int, ("00", 200, False))
    if resp[2]:  # タイムアウト処理
        time.sleep(toto_constant.TIMEOUT_SEC)
    return resp[:2]


def get_X_outou_kekka_for_purchase_map_purchase(bi_int:int) -> str:
    """
    No.1_購入・購入取消応答_マッピング
    応答結果の取得（購入応答）

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
        4: "05",  # 入金/発券中エラー
        5: "06",  # 入金/発券済みエラー
        6: "07",  # 入金/発券期限エラー
        7: "08",  # 取消済みエラー
        8: "99"   # その他エラー
    }, bi_int, "00")
    return resp


def get_X_tc_dai_for_purchase_map_purchase(bi_int:int) -> str:
    """
    No.1_購入・購入取消応答_マッピング
    チケット代金の取得（購入応答）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        str: 数字に対応する文字列
    """
    resp = req_res_map_flexible({
        0: "000000",
        1: "003500",
        2: "010000",
        3: "999999",
        4: "049999",
        5: "050000",
    }, bi_int, "000000")
    return resp


def get_X_ticket_cnt_for_purchase_map_purchase(bi_int:int) -> int:
    """
    No.1_購入・購入取消応答_マッピング
    チケット枚数の取得（購入応答）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        int: 数字に対応する数字
    """
    resp = req_res_map_flexible({
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5
    }, bi_int, 1)
    return resp


def get_X_saiso_kbn_status_for_purchase_map_purchase(bi_int:int) -> str:
    """
    No.1_購入・購入取消応答_マッピング
    再送区分ステータスの取得（購入応答）

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


def get_X_shori_kekka_for_purchase_cancel_map_purchase(bi_int:int) -> tuple[str, int]:
    """
    No.1_購入・購入取消応答_マッピング
    処理結果の取得（購入取消応答）

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


def get_X_outou_kekka_for_purchase_cancel_map_purchase(bi_int:int) -> str:
    """
    No.1_購入・購入取消応答_マッピング
    応答結果の取得（購入取消応答）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        str: 数字に対応する文字列
    """
    resp = req_res_map_flexible({
        0: "00",  # 正常応答
        1: "04",  # 未入金/発券エラー
        2: "06",  # 入金/発券済みエラー
        3: "07",  # 入金/発券期限エラー
        4: "08",  # 取消済みエラー
        5: "99",  # その他エラー
        6: "01",  # 検索キーエラー
    }, bi_int, "00")
    return resp


def get_X_tc_dai_for_purchase_cancel_map_purchase(bi_int:int) -> str:
    """
    No.1_購入・購入取消応答_マッピング
    チケット代金の取得（購入取消応答）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        str: 数字に対応する文字列
    """
    resp = req_res_map_flexible({
        0: "000000",
        1: "003500",
        2: "010000",
        3: "999999",
        4: "049999",
        5: "050000",
    }, bi_int, "000000")
    return resp


def get_X_saiso_kbn_status_for_purchase_cancel_map_purchase(bi_int:int) -> str:
    """
    No.1_購入・購入取消応答_マッピング
    再送区分ステータスの取得（購入取消応答）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        str: 数字に対応する文字列
    """
    resp = req_res_map_flexible({
        0: "0",  # 再送正常
        1: "1"   # 再送異常
    }, bi_int, "0")
    return resp


def get_X_shop_id_for_purchase_cancel_map_purchase(bi_int:int) -> str:
    """
    No.1_購入・購入取消応答_マッピング
    ショップIDの取得（購入取消応答）

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
