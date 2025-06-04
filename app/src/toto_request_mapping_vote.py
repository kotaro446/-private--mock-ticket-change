# ==================================================
# No.2_本投票・本投票障害取消応答_マッピング
# ==================================================
import time
import toto_constant
from toto_library import *

def get_X_tc_dai_for_purchase_map_vote(bi_int:int) -> str:
    """
    No.2_本投票・本投票障害取消応答_マッピング
    チケット代金の取得（購入）

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


def get_X_ticket_cnt_for_purchase_map_vote(bi_int:int) -> int:
    """
    No.2_本投票・本投票障害取消応答_マッピング
    チケット枚数の取得（購入）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        int: 数字に対応する数字
    """
    resp = req_res_map_flexible({
        0: 0,
        1: 1,
        2: 2,
        3: 5
    }, bi_int, 1)
    return resp


def get_X_shori_kekka_for_purchase_cancel_map_vote(bi_int:int) -> tuple[str, int]:
    """
    No.2_本投票・本投票障害取消応答_マッピング
    処理結果の取得（購入取消）

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


def get_X_outou_kekka_for_purchase_cancel_map_vote(bi_int:int) -> str:
    """
    No.2_本投票・本投票障害取消応答_マッピング
    応答結果の取得（購入取消）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        str: 数字に対応する文字列
    """
    resp = req_res_map_flexible({
        0: "00",  # "00"：正常応答
        1: "04",  # "04"：未入金/発券エラー
        2: "06",  # "06"：入金/発券済みエラー
        3: "07",  # "07"：入金/発券期限エラー
        4: "08",  # "08"：取消済みエラー
        5: "99",  # "99"：その他エラー
        6: "01",  # "01"：検索キーエラー
    }, bi_int, "00")
    return resp


def get_X_shori_kekka_for_vote_map_vote(bi_int:int) -> tuple[str, int]:
    """
    No.2_本投票・本投票障害取消応答_マッピング
    処理結果の取得（本投票）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        (str, int): 数字に対応する文字列, 数字に対応する数字
    """
    resp = req_res_map_flexible({
        0: ("00", 200, False),  # "00"：正常
        1: ("15", 400, False),  # "15"：タイムアウトエラー
        2: ("16", 400, False),  # "16"：SEJセンター混雑エラー
        3: ("99", 400, False),  # "99"：その他エラー(400)
        4: ("99", 500, False),  # "99"：その他エラー(500)
        5: ("00", 200, True),   # "00"：タイムアウト(正常)
        6: ("99", 500, True)    # "99"：タイムアウト(その他エラー500)
    }, bi_int, ("00", 200, False))
    if resp[2]:  # タイムアウト処理
        time.sleep(toto_constant.TIMEOUT_SEC)
    return resp[:2]


def get_X_outou_kekka_for_vote_mapi_vote(bi_int:int) -> str:
    """
    No.2_本投票・本投票障害取消応答_マッピング
    応答結果の取得（本投票）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        str: 数字に対応する文字列
    """
    resp = req_res_map_flexible({
        0: "00",  # "00"：正常応答
        1: "01",  # "01"：検索キーエラー
        2: "04",  # "04"：未払戻エラー
        3: "06",  # "06"：入金/発券済みエラー
        4: "07",  # "07"：入金/発券期限エラー
        5: "08",  # "08"：取消済みエラー
        6: "11",  # "11"：totoセンター接続エラー
        7: "12",  # "12"：totoセンター混雑エラー
        8: "13",  # "13"：totoセンターアプリエラー
        9: "14",  # "14"：totoセンター通信その他エラー
        10: "99"  # "99"：その他エラー
    }, bi_int, "00")
    return resp


def get_tc_text_ID_for_vote_map_vote(bi_int:int) -> str:
    """
    No.2_本投票・本投票障害取消応答_マッピング
    券面情報データの取得（本投票）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        str: 数字に対応する文字列
    """
    resp = req_res_map_flexible({
        0: "A",
        1: "B",
        2: "C",
        3: "D",
        4: "E",
        5: "F"
    }, bi_int, "B")
    return resp


def get_template_code_for_vote_map_vote(ID:str) -> str:
    """
    No.2_本投票・本投票障害取消応答_マッピング
    券面情報のテンプレートコードの取得（本投票）

    Args:
        ID (str): 券面情報データ

    Returns:
        str: テンプレートコード
    """
    match ID:
        case "A":
            return "TTNA000001"
        case "B":
            return "TTNA000001"
        case "C":
            return "TTNA000001"
        case "D":
            return "TTNA000002"  
        case "E":
            return "TTNA000002"
        case "F":
            return "TTNA000003"
        case _:
            return "TTNA000001"


def get_whether_print_ticket_barcode_number_for_vote_map_vote(bi_int:int) -> bool:
    """
    No.2_本投票・本投票障害取消応答_マッピング
    投票券バーコード番号印字要否の取得（本投票）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        bool: 投票券バーコード番号印字要否
    """
    resp = req_res_map_flexible({
        0: True,
        1: False
    }, bi_int, True)
    return resp


def get_X_toto_kekka_for_vote_map_vote(bi_int:int) -> str:
    """
    No.2_本投票・本投票障害取消応答_マッピング
    totoセンター応答結果の取得（本投票）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        str: 数字に対応する文字列
    """
    resp = req_res_map_flexible({
        0: "000000",  # "000000"
        1: "000001"   # "000001"
    }, bi_int, "000000")
    return resp


def get_X_shori_kekka_for_vote_cancel_map_vote(bi_int:int) -> str:
    """
    No.2_本投票・本投票障害取消応答_マッピング
    処理結果の取得（本投票障害取消）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        (str, int): 数字に対応する文字列, 数字に対応する数字
    """
    resp = req_res_map_flexible({
        0: ("00", 200, False),  # "00"：正常
        1: ("15", 400, False),  # "15"：タイムアウトエラー
        2: ("16", 400, False),  # "16"：SEJセンター混雑エラー
        3: ("99", 400, False),  # "99"：その他エラー(400)
        4: ("99", 500, False),  # "99"：その他エラー(500)
        5: ("00", 200, True),   # "00"：タイムアウト(正常)
        6: ("99", 500, True)    # "99"：タイムアウト(その他エラー500)
    }, bi_int, ("00", 200, False))
    if resp[2]:  # タイムアウト処理
        time.sleep(toto_constant.TIMEOUT_SEC)
    return resp[:2]


def get_X_outou_kekka_for_vote_cancel_map_vote(bi_int:int) -> str:
    """
    No.2_本投票・本投票障害取消応答_マッピング
    応答結果の取得（本投票障害取消）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        str: 数字に対応する文字列
    """
    resp = req_res_map_flexible({
        0: "00",  # "00"：正常応答
        1: "01",  # "01"：検索キーエラー
        2: "04",  # "04"：未払戻エラー
        3: "06",  # "06"：入金/発券済みエラー
        4: "07",  # "07"：入金/発券期限エラー
        5: "08",  # "08"：取消済みエラー
        6: "09",  # "09"：取消期限エラー
        7: "11",  # "11"：totoセンター接続エラー
        8: "12",  # "12"：totoセンター混雑エラー
        9: "13",  # "13"：totoセンターアプリエラー
        10: "14",  # "14"：totoセンター通信その他エラー
        11: "99"   # "99"：その他エラー
    }, bi_int, "00")
    return resp


def get_X_toto_kekka_for_vote_cancel_map_vote(bi_int:int) -> str:
    """
    No.2_本投票・本投票障害取消応答_マッピング
    totoセンター応答結果の取得（本投票障害取消）

    Args:
        bi_int (int): マッピングで割り当てられた数字

    Returns:
        str: 数字に対応する文字列
    """
    resp = req_res_map_flexible({
        0: "000000",  # "000000"
        1: "000001"   # "000001"
    }, bi_int, "000000")
    return resp
