import time
import in_const as in_const

from ticket_library import (
    req_res_map,
    split_bits,
)
from ec_ticket_library import (
    get_ticket_info,
    get_ec_query_pay_type,
    get_ec_query_dlv_type,
    get_ec_query_keijyo_type,
    get_ec_query_inshi_kijun,
    get_ec_query_kingaku_henko_flg,
    get_ec_query_kino_kbn,
    get_ec_query_shuno_kingaku,
    get_order_details_dictionary,
)

def get_ec_nomal_field(request_data:dict, mapping_str:str) -> tuple[dict,dict,dict,dict,int]:
    """
    No.1_EC関連問合せ応答の更新データを取得する
    ----

    Parameters
    ----------
    request_data :dict  
    mapping_str :str

    Returns
    -------
    interface_info :dict  
    order_info :dict  
    ticket_info :dict
    order_details :dict
    httpstatus :int
    """

    mapping = split_bits(mapping_str, [
        3, # reserved
        3, # mapping[1]処理結果
        4, # mapping[2]応答結果
        2, # mapping[3]支払種別
        1, # mapping[4]納品種別
        2, # mapping[5]売上計上区分
        2, # mapping[6]印紙基準額
        1, # mapping[7]価格変更フラグ
        1, # mapping[8]機能区分
        3, # mapping[9]SHOPCD
        2, # mapping[10]収納金額
        3, # mapping[11]チケット枚数
        1, # mapping[12]レスポンスパターン（再送区分用）
        3, # mapping[13]取消処理結果
        2, # mapping[14]取消応答結果
        1, # mapping[15]レスポンスパターン（取消再送区分用）
        2, # NoCare
    ]) # 36bit（内、3bitが未使用、31bitがオプション、2bitがマップ番号）

    (interface_info, httpstatus) = get_interface_info(request_data, mapping)
    order_info = get_order_info(request_data, mapping)
    ticket_info = get_ticket_info(request_data, mapping[11], order_info)
    
    # order_detailsを生成（B,H,J要求区分の場合のみ）
    order_details = {}
    if request_data["yokyu_kubun"] in {"B", "H", "J"}:
        order_details = get_order_details_dictionary(request_data)

    return (interface_info, order_info, ticket_info, order_details, httpstatus)

def get_interface_info(request_data:dict, mapping:list) -> tuple[dict,int]:
    """
    interface_infoの辞書を作成
    """
    # 処理結果、HTTPステータス取得
    res_query_syori_kekka:str
    httpstatus:int
    if request_data["toiawase_kanryo_kubun"] == "1":
        # 要求区分が "A"：チケット発券依頼（代引）の場合
        if request_data["yokyu_kubun"] == "A":
            #再送の場合
            if (request_data["retry_flg"] == "1" and
                get_ec_query_response_saisoyo(mapping[12]) == "0"):
                res_query_syori_kekka = "00"
                httpstatus = 200
            else:
                (res_query_syori_kekka, httpstatus) = get_ec_query_syori_kekka(mapping[1])
        # 要求区分が
        # "B"：チケット発券取消（代引)
        # "H"：ﾁｹｯﾄﾌﾟﾘﾝﾀｴﾗｰ発券取消（代引）
        # "J"：XMLﾌｧｲﾙ・イメージファイル取得NG発券取消（代引）の場合
        elif request_data["yokyu_kubun"] in {"B", "H", "J"}:
            if (request_data["retry_flg"] == "1" and
                get_ec_query_delete_response_saisoyo(mapping[15]) == "0"):
                res_query_syori_kekka = "00"
                httpstatus = 200
            else:
                (res_query_syori_kekka, httpstatus) = get_ec_query_syori_kekka(mapping[13])
        else:
            raise ValueError(f"要求区分が不正です。yokyu_kubun = {request_data["yokyu_kubun"]}")
    elif request_data["toiawase_kanryo_kubun"] == "2":
        res_query_syori_kekka = "00"
        httpstatus = 200

    interface_info = {
        "syori_kekka": res_query_syori_kekka
    }
    return (interface_info, httpstatus)

def get_order_info(request_data:dict, mapping:list) -> dict:
    """
    order_infoの辞書を作成
    """
    res_query_oto_kekka:str
    if request_data["toiawase_kanryo_kubun"] == "1":
        # 要求区分が "A"：チケット発券依頼（代引）の場合
        if request_data["yokyu_kubun"] == "A":
            #再送の場合
            if (request_data["retry_flg"] == "1" and
                get_ec_query_response_saisoyo(mapping[12]) == "0"):
                res_query_oto_kekka = "00"
            else:
                res_query_oto_kekka = get_ec_query_otoKekka(mapping[2])
        # 要求区分が "B"：チケット発券取消（代引)、"H"：ﾁｹｯﾄﾌﾟﾘﾝﾀｴﾗｰ発券取消（代引）、"J"：XMLﾌｧｲﾙ・イメージファイル取得NG発券取消（代引）の場合
        elif request_data["yokyu_kubun"] in {"B", "H", "J"}:
            if (request_data["retry_flg"] == "1" and
                get_ec_query_delete_response_saisoyo(mapping[15]) == "0"):
                res_query_oto_kekka = "00"
            else:
                res_query_oto_kekka = get_ec_delete_otoKekka(mapping[14])
        else:
            raise ValueError(f"要求区分が不正です。yokyu_kubun = {request_data["yokyu_kubun"]}")
    elif request_data["toiawase_kanryo_kubun"] == "2":
        res_query_oto_kekka = "00"

    if (res_query_oto_kekka != "00"): # 応答結果:異常
        order_info = {
            "bar_code_no" : "             ",
            "oto_kekka": res_query_oto_kekka,
            "pay_type" : " ",
            "dlv_type" : " ",
            "tenpo_bango" : "      ",
            "mise_namek" : "                                    ",
            "mise_address" : "                                                ",
            "tenpo_tel_no" : "            ",
            "keijyo_type" : " ",
            "inshi_kijun" : "      ",
            "kingaku_henko_flg" : " ",
            "kino_kbn" : " ",
            "haraikomi_no" : "             ",
            "shop_id" : "     ",
            "shuno_kingaku" : "      ",
            "shohin_daikin" : "      ",
            "shop_namek" : "                                                  ",
            "user_namek" : "                              ",
            "renraku_saki" : "                                                                ",
        }
    else: # 応答結果:正常
        order_info = {
            "oto_kekka": res_query_oto_kekka,
            "pay_type": get_ec_query_pay_type(mapping[3]),
            "dlv_type": get_ec_query_dlv_type(mapping[4]),
            "keijyo_type": get_ec_query_keijyo_type(mapping[5]),
            "inshi_kijun": get_ec_query_inshi_kijun(mapping[6]),
            "kingaku_henko_flg": get_ec_query_kingaku_henko_flg(mapping[7]),
            "kino_kbn": get_ec_query_kino_kbn(mapping[8]),
            "shop_id": get_ec_query_shop_id(mapping[9]),
            "shuno_kingaku": get_ec_query_shuno_kingaku(mapping[10])
        }

    return order_info

def get_ec_query_response_saisoyo(map_num:int) -> str:
    """
    レスポンスパターン再送（EC関連問合せ）
    """
    res = req_res_map({
        0 : "0",#再送正常
        1 : "1",#再送異常
    }, map_num, "0")
    return res

def get_ec_query_syori_kekka(map_num:int) -> tuple[str, int]:
    """
    処理結果(EC関連問合せ)
    """
    res = req_res_map({
        0: ("00", 200, False), #正常
        1: ("10", 400, False), #電文区分エラー
        2: ("11", 400, False), #業務区分エラー
        3: ("14", 400, False), #サービス時間帯エラー
        4: ("99", 400, False), #その他エラー (400)
        5: ("99", 500, False), #その他エラー (500)
        6: ("00", 200, True),  #タイムアウト（正常）
        7: ("99", 500, True), #タイムアウト（その他エラー500)
    }, map_num, ("00", 200, False))
    if res[2]:
        time.sleep(in_const.TIMEOUT_SEC)
    return res[:2]

def get_ec_delete_otoKekka(map_num:int) -> str:
    """
    取消応答結果（EC関連問合せ）   
    """
    res = req_res_map({
        0:"00", #正常応答
        1:"01", #取消異常（検索キーエラー）
        2:"04", #取消異常（取消済み）
        3:"99", #取消異常（その他エラー）
    }, map_num, "00")
    return res

def get_ec_query_delete_response_saisoyo(map_num:int) -> str:
    """
    レスポンスパターン取消再送（EC関連問合せ）
    """
    res = req_res_map({
        0 : "0",#再送正常
        1 : "1",#再送異常
    }, map_num, "0")
    return res

def get_ec_query_otoKekka(map_num:int) -> str:
    """
    応答結果(EC関連問合せ)
    """
    res = req_res_map({
        0: "00", #正常応答(決済可能)
        1: "01", #検索キーエラー
        2: "02", #支払期限エラー
        3: "03", #支払済み
        4: "05", #決済中止
        5: "11", #店舗指定エラー
        6: "12", #店舗引渡中止
        7: "16", #受付中
        8: "99", #その他エラー
    }, map_num, "00")
    return res

def get_ec_query_shop_id(map_num:int)->str:
    """
    SHOP-CD（EC関連問合せ No.1マッピング対応）
    """
    res = req_res_map({
        0 : "00000", #オリンピックチケット以外
        1 : "00236", #オリンピックチケット
        2 : "00245",
        3 : "00745",
        4 : "30731", #ぴあ
    }, map_num, "00000")
    return res