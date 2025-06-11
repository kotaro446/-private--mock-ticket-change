import random
from ticket_library import (
    req_res_map,
    split_bits,
    calculate_CD,
)
from ec_ticket_library import (
    get_ec_query_pay_type,
    get_ec_query_dlv_type,
    get_ec_query_keijyo_type,
    get_ec_query_inshi_kijun,
    get_ec_query_kingaku_henko_flg,
    get_ec_query_kino_kbn,
    get_ec_query_shuno_kingaku,
    get_ec_kanryo_inshi_syukin_gaku,
    check_pia_ticket,
    get_order_details_dictionary,
)

def get_ec_kenmen_field(request_data:dict, mapping_str:str) -> tuple[dict,dict,dict,dict,int]:

    mapping = split_bits(mapping_str, [
        11,# reserved
        2, # mapping[1]支払種別
        1, # mapping[2]納品種別
        2, # mapping[3]売上計上区分
        2, # mapping[4]印紙基準額
        1, # mapping[5]価格変更フラグ
        1, # mapping[6]機能区分
        4, # mapping[7]SHOPCD
        2, # mapping[8]収納金額
        4, # mapping[9]チケット枚数
        4, # mapping[10]券面情報データ
        2, # NoCare
    ]) # 36bit（内、11bitが未使用、23bitがオプション、2bitがマップ番号）
    
    # interface_infoの辞書の作成
    interface_info = {
        "syori_kekka": "00"
    }
    httpstatus = 200

    # order_infoの辞書の作成
    order_info = get_order_info(request_data, mapping)

    # ticket_infoの辞書の作成
    ticket_info = get_ticket_info(request_data, mapping, order_info)

    # order_detailsを生成（B,H,J要求区分の場合のみ）
    order_details = {}
    if request_data["yokyu_kubun"] in {"B", "H", "J"}:
        order_details = get_order_details_dictionary(request_data)

    return (interface_info, order_info, ticket_info, order_details, httpstatus)

def get_order_info(request_data:dict, mapping:list) -> dict:
    """
    order_infoの辞書の作成
    """
    order_info:dict
    if request_data["toiawase_kanryo_kubun"] == "1": #(EC関連問合せ)
        res_query_pay_type = get_ec_query_pay_type(mapping[1])#支払種別
        res_query_dlv_type = get_ec_query_dlv_type(mapping[2])#納品種別
        res_query_keijyo_type = get_ec_query_keijyo_type(mapping[3])#売上計上区分
        res_query_inshi_kijun = get_ec_query_inshi_kijun(mapping[4])#印紙基準額
        res_query_kingaku_henko_flg = get_ec_query_kingaku_henko_flg(mapping[5])#価格変更フラグ
        res_query_query_kino_kbn = get_ec_query_kino_kbn(mapping[6])#機能区分
        res_query_shop_id = get_ec_query_shop_id_2(mapping[7])#SHOP-CD
        res_query_shuno_kingaku = get_ec_query_shuno_kingaku(mapping[8])#収納金額
        order_info = {
            "oto_kekka": "00",
            "pay_type": res_query_pay_type,
            "dlv_type": res_query_dlv_type,
            "keijyo_type": res_query_keijyo_type,
            "inshi_kijun": res_query_inshi_kijun,
            "kingaku_henko_flg": res_query_kingaku_henko_flg,
            "kino_kbn": res_query_query_kino_kbn,
            "shop_id": res_query_shop_id,
            "shuno_kingaku": res_query_shuno_kingaku,
        }
    elif request_data["toiawase_kanryo_kubun"] == "2":#(EC関連完了)
        res_kanryo_inshi_syukin_gaku = get_ec_kanryo_inshi_syukin_gaku(mapping[4])#印紙基準額/収納金額
        res_kanryo_kino_kbn = get_ec_query_kino_kbn(mapping[6])#機能区分
        res_kanryo_shop_id = get_ec_query_shop_id_2(mapping[7])# SHOP-CD
        order_info = {
            "oto_kekka": "00",
            "kino_kbn": res_kanryo_kino_kbn,
            "shop_id": res_kanryo_shop_id,
            "shuno_kingaku": res_kanryo_inshi_syukin_gaku,
        }
    else:
        raise ValueError(f"問合せ・完了区分が不正です。{request_data["toiawase_kanryo_kubun"]}")
    return order_info

def get_ticket_info(request_data:dict, mapping:list, order_info:dict) -> dict:
    """
    ticket_infoの辞書の作成
    """
    ticket_info:dict = {}
    if (request_data["toiawase_kanryo_kubun"] == "1" and
        request_data["yokyu_kubun"] == "A" and
        order_info["oto_kekka"] == "00"):
        ticket_maisu = get_ec_ticket_maisu(mapping[9])#チケット発券個別情報
        # ぴあチケットの場合
        if check_pia_ticket(order_info["shop_id"]):
            for i in range(1, ticket_maisu + 1):
                ticket_info[f"html_name{i}"] = get_ec_ticket_kenmen_info(mapping[10])[0]
                # ぴあチケット印刷用バーコードの生成
                B1_B12 = random.randint(0, 999999999999)
                B1_B12_str = str(B1_B12).zfill(12)
                ticket_info[f"barcode{i}"] = B1_B12_str + str(calculate_CD(B1_B12_str))
                ticket_info[f"ticket_data{i}"] = get_ec_ticket_kenmen_info(mapping[10])[1]
        # ぴあチケットの場合
        else:
            for i in range(1, ticket_maisu + 1):
                ticket_info[f"html_name{i}"] = get_ec_ticket_kenmen_info(mapping[10])[0]
                ticket_info[f"barcode{i}"] = "             " 
                ticket_info[f"ticket_data{i}"] = get_ec_ticket_kenmen_info(mapping[10])[1]

    return ticket_info

def get_ec_query_shop_id_2(map_num:int) -> str:
    """
    SHOP-CD（EC関連問合せ No.4マッピング対応）
    """
    res = req_res_map({
        0: "00000", #オリンピックチケット以外
        1: "00236", #オリンピックチケット
        2: "00245", #一般値
        3: "00745", #一般値
        4: "00781", #ティーガイア（PIN）
        5: "30731", #ぴあ
        6: "30771", #ディスコ
        7: "30773", #JTB（レジャー）
        8: "30775", #JTB（ＴＤＲ）
    }, map_num, "00000")
    return  res

def get_ec_ticket_maisu(map_num:int) -> int:
    """
    チケット発券個別情報（枚数）（EC関連問合せ No.4マッピング対応）
    """
    res = req_res_map({
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 12,
        12: 14,
        13: 16,
        14: 18,
        15: 20,
    }, map_num, 0)
    return res

def get_ec_ticket_kenmen_info(map_num:int) -> tuple[str,str]:
    """
    券面情報データ （EC関連問合せ No.4マッピング対応）
    """
    res = req_res_map({
        0: ("ETPM000001","NTPM000001_Normal"),
        1: ("ETDJUP0001","TTDJUP0001_Normal"),
        2: ("ETDJUP0001","TTDJUP0001_Max"),
        3: ("ETJW01001T","NTJW01001T_Normal"),
        4: ("ETJW01002T","NTJW01002T"),
        5: ("ETJD03020T","NTJD03020T_Normal"),
        6: ("ETPI001102","NTPI001102"),
        7: ("TTOT000017","TI03190100"),
        8: ("TTOT000178","TI03190101")
    }, map_num, ("ETPI001102","NTPI001102"))
    return res