import time
from ticket_library import (
    req_res_map,
    split_bits,
)
import in_const as in_const
def get_ec_refund_field(request_data:dict, mapping_str:str) -> tuple[dict, dict, int]:
    """
    No.2_EC関連払戻し応答の更新データを取得する
    ----

    Parameters
    ----------
    request_data :dict  
    mapping_str :str

    Returns
    -------
    interface_info :dict  
    payback_info :dict  
    httpstatus :int
    """
    mapping = split_bits(mapping_str, [
        9, # reserved
        3, # mapping[1]処理結果
        4, # mapping[2]応答結果区分
        2, # mapping[3]払戻金額
        2, # mapping[4]開始日・終了日
        2, # mapping[5]開始時間・終了時間
        1, # mapping[6]半券確認要否
        2, # mapping[7]チケット手数料払戻金額
        3, # mapping[8]取消処理結果
        2, # mapping[9]取消応答結果
        1, # mapping[10]レスポンスパターン再送
        2, # NoCare
    ]) # 33bit（内、9bitが未使用、22bitがオプション、2bitがマップ番号）

    # interface_infoの辞書を作成
    (interface_info, httpstatus) = get_interface_info(request_data, mapping)

    # payback_infoの辞書を作成
    payback_info = get_payback_info(request_data, mapping)

    return (interface_info, payback_info, httpstatus)

def get_interface_info(request_data:dict, mapping:list) -> tuple[dict, int]:
    """
    interface_infoの辞書を作成
    """
    syori_kekka:str
    httpstatus:int
    if request_data["yokyu_kubun"] == "E":# 要求区分が "E"：チケット払戻 の場合
        (syori_kekka, httpstatus) = get_ec_refund_syori_kekka( mapping[1] )
    elif request_data["yokyu_kubun"] == "L":# 要求区分が "L"：チケット払戻取消 の場合
        if (request_data["retry_flg"] == "1" and
            get_ec_refund_delete_response_saisoyo( mapping[10] )):
            syori_kekka = "00"
            httpstatus = 200
        else:
            (syori_kekka, httpstatus) = get_ec_refund_delete_syori_kekka( mapping[8] )
    else:
       raise ValueError(f"要求区分不正：{request_data["yokyu_kubun"]}")
    interface_info = {
        "syori_kekka": syori_kekka,
    }
    return (interface_info, httpstatus)

def get_payback_info(request_data:dict, mapping:list) -> dict:
    """
    payback_infoの辞書を作成
    """
    # 応答結果区分
    otoKekka:str
    if request_data["yokyu_kubun"] == "E":# 要求区分が "E"：チケット払戻 の場合
        otoKekka = get_ec_refund_otoKekka( mapping[2] )
    elif request_data["yokyu_kubun"] == "L":# 要求区分が "L"：チケット払戻取消 の場合
        if (request_data["retry_flg"] == "1" and
            get_ec_refund_delete_response_saisoyo( mapping[10] )):
            otoKekka = "00"
        else:
            otoKekka = get_ec_refund_delete_otoKekka( mapping[9] )
    else:
       raise ValueError(f"要求区分不正：{request_data["yokyu_kubun"]}")

    # 開始日・終了日／開始時刻・終了時刻を設定
    res_combined_dates = get_ec_refund_date(mapping[4])
    res_combined_times = get_ec_refund_time(mapping[5])

    # 応答結果が "52"の場合　開始日,終了日を設定
    if (otoKekka == "52"):
        payback_info = {
            "kessai_id" : "           ",
            "oto_kekka": otoKekka,
            "tenpo_bango" : "      ",
            "mise_namek" : "                                    ",
            "mise_address" : "                                                ",
            "tenpo_tel_no" : "            ",
            "haraikomi_no" : "             ",
            "shop_id" : "     ",
            "payback_kingaku" : "000000",
            "shop_namek" : "                                                  ",
            "user_namek" : "                              ",
            "renraku_saki" : "                                                                ",
            "payback_start_ymd": res_combined_dates[0],
            "payback_end_ymd": res_combined_dates[1],
            "svc_time_start_hm" : "    ",
            "svc_time_end_hm" : "    ",
            "kogyo_name" : "                                                                                                                                                                                                        ",
            "koen_date_ymd" : "        ",
            "hanken_yohi" : " ",
            "fuka_riyu" : "  ",
            "payback_tesuryo" : "000000",
        }
    # 応答結果が "55"または"56"の場合　開始時刻,終了時刻を設定
    elif otoKekka in ("55", "56"):
        payback_info = {
            "kessai_id" : "           ",
            "oto_kekka": otoKekka,
            "tenpo_bango" : "      ",
            "mise_namek" : "                                    ",
            "mise_address" : "                                                ",
            "tenpo_tel_no" : "            ",
            "haraikomi_no" : "             ",
            "shop_id" : "     ",
            "payback_kingaku" : "000000",
            "shop_namek" : "                                                  ",
            "user_namek" : "                              ",
            "renraku_saki" : "                                                                ",
            "payback_start_ymd" : "        ",
            "payback_end_ymd" : "        ",
            "svc_time_start_hm": res_combined_times[0],
            "svc_time_end_hm": res_combined_times[1],
            "kogyo_name" : "                                                                                                                                                                                                        ",
            "koen_date_ymd" : "        ",
            "hanken_yohi" : " ",
            "fuka_riyu" : "  ",
            "payback_tesuryo" : "000000",
        }
    elif (otoKekka == "00"):
        # 辞書作成
        payback_info = {
            "oto_kekka": otoKekka,
            "payback_kingaku": get_ec_refund_payback_kingaku(mapping[3]),
            "payback_start_ymd": res_combined_dates[0],
            "payback_end_ymd": res_combined_dates[1],
            "svc_time_start_hm": res_combined_times[0],
            "svc_time_end_hm": res_combined_times[1],
            "hanken_yohi": get_ec_refund_hanken_yohi(mapping[6]),
            "payback_tesuryo": get_ec_refund_payback_tesuryo(mapping[7]),
        }
    else:
        payback_info = {
            "kessai_id" : "           ",
            "oto_kekka": otoKekka,
            "tenpo_bango" : "      ",
            "mise_namek" : "                                    ",
            "mise_address" : "                                                ",
            "tenpo_tel_no" : "            ",
            "haraikomi_no" : "             ",
            "shop_id" : "     ",
            "payback_kingaku" : "000000",
            "shop_namek" : "                                                  ",
            "user_namek" : "                              ",
            "renraku_saki" : "                                                                ",
            "payback_start_ymd" : "        ",
            "payback_end_ymd" : "        ",
            "svc_time_start_hm" : "    ",
            "svc_time_end_hm" : "    ",
            "kogyo_name" : "                                                                                                                                                                                                        ",
            "koen_date_ymd" : "        ",
            "hanken_yohi" : " ",
            "fuka_riyu" : "  ",
            "payback_tesuryo" : "000000",
        }
    return payback_info

def get_ec_refund_syori_kekka(map_num:int) -> tuple[str, int]:
    """
    処理結果(EC関連払戻し)

    Parameters
    ----------
    map_num:int

    Returns
    -------
    tuple[str, int]
        処理結果
        HTTPステータスコード
    """
    res = req_res_map({
        0: ("00", 200, False),  # 正常
        1: ("10", 400, False),  # 電文区分エラー
        2: ("11", 400, False),  # 業務区分エラー
        3: ("14", 400, False),  # サービス時間帯エラー
        4: ("99", 400, False),  # その他エラー(400)
        5: ("99", 500, False),  # その他エラー(500)
        6: ("00", 200, True),   # タイムアウト(正常)
        7: ("99", 500, True),   # タイムアウト(その他エラー500)
    }, map_num, ("00", 200, False))
    if res[2]:  # タイムアウト処理
        time.sleep(in_const.TIMEOUT_SEC)
    return res[:2]

def get_ec_refund_otoKekka(map_num:int) -> str:
    """
    応答結果(EC関連払戻し)

    Parameters
    ----------
    map_num:int

    Returns
    -------
    res:str 応答結果
    """
    res = req_res_map({
        0 : "00", #正常応答(決済可能)
        1 : "01", #検索キーエラー
        2 : "05", #決済中止
        3 : "11", #店舗指定エラー
        4 : "51", #払戻済み
        5 : "52", #払戻期間前エラー
        6 : "53", #払戻不可エラー
        7 : "55", #払戻サービス時間外エラー
        8 : "56", #初日時間前エラー
        9 : "57", #払戻期間終了後エラー
        10: "99", #その他エラー
    }, map_num, "00")
    return res

def get_ec_refund_payback_kingaku(map_num:int) -> str:
    """
    払戻金額(EC関連払戻し)

    Parameters
    ----------
    map_num:int

    Returns
    -------
    res:str 応答結果
    """
    res = req_res_map({
        0:"      ", #" "（ALL半角空白）：未設定
        1:"000000", #最低値
        2:"001000", #一般値
        3:"999999", #最大値
    }, map_num, "      ")
    return res

def get_ec_refund_date(map_num:int) -> tuple[str,str]:
    """
    開始日・終了日(EC関連払戻し)
    
    Parameters
    ----------
    map_num:int

    Returns
    -------
    res:str 応答結果
    """
    res = req_res_map({
        0: ("20250101", "20250131"),
        1: ("20250201", "99999999"),
        2: ("99999999", "20250131"),
        3: ("20000101", "99999999"),
    }, map_num, ("20250101", "20250131"))
    return res

def get_ec_refund_time(map_num:int) -> tuple[str,str]:
    """
    開始時間・終了時間(EC関連払戻し)
    
    Parameters
    ----------
    map_num:int

    Returns
    -------
    res:str 応答結果
    """
    res = req_res_map({
       0: ("0000", "2359"),
       1: ("0930", "1259"),
       2: ("1830", "2200"),
       3: ("0000", "9999")
    }, map_num, ("0000", "2359"))
    return res

def get_ec_refund_hanken_yohi(map_num:int) -> str:
    """
    半券確認要否(EC関連払戻し)
    """
    res = req_res_map({
        0: "0", #不要
        1: "1", #要
    }, map_num, "0")
    return  res

def get_ec_refund_payback_tesuryo(map_num:int) -> str:
    """
    チケット手数料払戻金額(EC関連払戻し)
    """
    res = req_res_map({
        0: "      ", #"      "（ALL半角空白）：未設定
        1: "000000", #最低値
        2: "003000", #一般値
        3: "999999", #最大値
    }, map_num, "000000")
    return res

def get_ec_refund_delete_syori_kekka(map_num:int) -> tuple[str, int]:
    """
    取消処理結果(EC関連払戻し)
    """
    res = req_res_map({
       0: ("00", 200, False), #正常
       1: ("10", 400, False), #電文区分エラー
       2: ("11", 400, False), #業務区分エラー
       3: ("14", 400, False), #サービス時間帯エラー
       4: ("99", 400, False), #その他エラー (400)
       5: ("99", 500, False), #その他エラー (500)
       6: ("00", 200, True),  #タイムアウト（正常）
       7: ("99", 500, True),  #タイムアウト（その他エラー500)
    }, map_num, ("00", 200, False))
    if res[2]: #タイムアウト処理
        time.sleep(in_const.TIMEOUT_SEC)
    return res[:2]

def get_ec_refund_delete_otoKekka(map_num:int) -> str:
    """
    取消応答結果(EC関連払戻し)
    """
    res = req_res_map({
        0: "00", #取消正常
        1: "01", #取消異常（検索キーエラー）
        2: "54", #取消異常（払戻未済み）
        3: "99", #取消異常（その他エラー）
    }, map_num, "00")
    return res

# レスポンスパターン再送(EC関連払戻し)
def get_ec_refund_delete_response_saisoyo(map_num:int) -> bool:
    """
    レスポンスパターン再送

    Parameters
    ----------
    map_num:int

    Returns
    -------
    True: 再送時正常(処理結果、応答値の差し替え)
    False:再送時異常
    """
    res = req_res_map({
        0: True,
        1: False,
    }, map_num, True)
    return res
