import random
from ticket_library import (
    req_res_map,
)
from logger import get_logger
logger = get_logger()

from ticket_library import (
   calculate_CD,
)

def ec_ticket_validate_check(request_data:dict) -> str:
    """
    validateチェックをする
    """
    res:str
    # 要求区分チェック
    if ("yokyu_kubun" not in request_data):
        res = "99"
        logger.debug(f"要求区分が必須項目。syori_kekka: {res}")
    # リクエストの充足チェック
    elif (check_key(request_data) == False):
        res = "99"
        logger.debug(f"パラメータが不足。syori_kekka: {res}")
    # 検索キーチェック
    elif ((request_data["yokyu_kubun"] in {"A", "B", "H", "J"}) and
          (request_data["kensaku_key"] == "")):
        res = "99"
        logger.debug(f"検索キーが必須項目。syori_kekka: {res}")
    # バーコードNoチェック
    elif ((request_data["yokyu_kubun"] in {"E", "L"}) and
          (request_data["bar_code_no"] == "")):
        res = "99"
        logger.debug(f"bar_code_noが必須項目。syori_kekka: {res}")
    # 電文区分エラー
    elif request_data["denbun_kubun"] != "20":
        res = "10"
        logger.debug(f"電文区分エラー　syori_kekka: {res}")
    # 業務区分エラー
    elif request_data["gyomu_kubun"] != "0067":
        res = "11"
        logger.debug(f"電文区分エラー　syori_kekka: {res}")
    else:
        res = "00"
    return res

def check_key(request_data:dict) -> bool:
    """
    リクエストにキーが含まれていることを確認する
    """
    res:bool
    keys:list = []
    if ("toiawase_kanryo_kubun" not in request_data):
        res = False
    else:
        # 要求区分
        # "A"：チケット発券依頼（代引）
        # "B"：チケット発券取消（代引)、
        # "H"：ﾁｹｯﾄﾌﾟﾘﾝﾀｴﾗｰ発券取消（代引）
        # "J"：XMLﾌｧｲﾙ・イメージファイル取得NG発券取消（代引）
        if (request_data["yokyu_kubun"] in {"A", "B", "H", "J"}):
            if (request_data["toiawase_kanryo_kubun"] == "1"):
                keys = ["denbun_kubun", "syori_kekka", "gyomu_kubun", "kigyo_id", "mise_no", "tuban", "regi_no", 
                    "ticket_regi_no", "order_type", "syohin_info_kbn", "riyo_time_ymdhms", "syori_tuban", "retry_flg",
                    "yokyu_kubun", "toiawase_kanryo_kubun", "kensaku_key", "bar_code_no", "cvs_code", "item_pointer"]
        
            elif (request_data["toiawase_kanryo_kubun"] == "2"):
                keys = ["denbun_kubun", "syori_kekka", "gyomu_kubun", "kigyo_id", "mise_no", "tuban", "regi_no", 
                        "ticket_regi_no", "kanryo_tuchi_kubun", "shiharai_hoho_kbn", "riyo_time_ymdhms", "syori_tuban", 
                        "retry_flg", "yokyu_kubun", "toiawase_kanryo_kubun", "kensaku_key", "bar_code_no", "cvs_code", 
                        "kino_kbn", "shop_id", "shuno_kingaku", "otoKekka_kubun", "oto_kekka"]
            else:
                raise ValueError(f"不正toiawase_kanryo_kubun = {request_data["toiawase_kanryo_kubun"]}")
        # 要求区分
        # "E"：チケット払戻、"L"：チケット払戻取消
        elif (request_data["yokyu_kubun"] in {"E", "L"}):
            keys = ["denbun_kubun", "syori_kekka", "gyomu_kubun", "kigyo_id", "mise_no", "tuban", 
                    "regi_no", "ticket_regi_no", "riyo_time_ymdhms", "syori_tuban", "retry_flg", 
                    "yokyu_kubun", "toiawase_kanryo_kubun", "shop_id", "torikeshi_riyu", "bar_code_no"]
        else:
            raise ValueError(f"不正yokyu_kubun:{request_data["yokyu_kubun"]}")

        # 送信するパラメータには上記の項目が揃えていない場合      
        if not all(key in request_data for key in keys):
            res = False  
        else:
            res = True

        unexpected_keys = [key for key in keys if key not in request_data]
        if unexpected_keys:
            logger.error(f'不足しているリクエストパラメータ: {unexpected_keys}')

    return res

def get_interface_info_dictionary(request_data:dict) -> dict:
    res:dict
    if (request_data["toiawase_kanryo_kubun"] == "1"):
        if (request_data["yokyu_kubun"] in {"E", "L"}):
            res = {
                "denbun_kubun": "22",
                "syori_kekka": "00",
                "gyomu_kubun": "0067",
                "kigyo_id": "07",
                "mise_no": request_data["mise_no"],
                "tuban": "SQ",
                "regi_no": request_data["regi_no"],
                "ticket_regi_no": " ",
                "riyo_time_ymdhms": request_data["riyo_time_ymdhms"],
                "syori_tuban": request_data["syori_tuban"],
                "retry_flg": request_data["retry_flg"],
                "yokyu_kubun": request_data["yokyu_kubun"],
                "toiawase_kanryo_kubun": request_data["toiawase_kanryo_kubun"],
            }
        else:
            res = {
                "denbun_kubun": "22",
                "syori_kekka": "00",
                "gyomu_kubun": "0067",
                "kigyo_id": "07",
                "mise_no": request_data["mise_no"],
                "tuban": "SQ",
                "regi_no": request_data["regi_no"],
                "ticket_regi_no": request_data["ticket_regi_no"],
                "order_type": " ",
                "syohin_info_kbn": " ",
                "riyo_time_ymdhms": request_data["riyo_time_ymdhms"],
                "syori_tuban": request_data["syori_tuban"],
                "retry_flg": request_data["retry_flg"],
                "yokyu_kubun": request_data["yokyu_kubun"],
                "toiawase_kanryo_kubun": request_data["toiawase_kanryo_kubun"],
            }
    elif (request_data["toiawase_kanryo_kubun"] == "2"):
        res = {
            "denbun_kubun": "22",
            "syori_kekka": "00",
            "gyomu_kubun": "0067",
            "kigyo_id": "07",
            "mise_no": request_data["mise_no"],
            "tuban": "SQ",
            "regi_no": request_data["regi_no"],
            "ticket_regi_no": request_data["ticket_regi_no"],
            "kanryo_tuchi_kubun": "1",
            "shiharai_hoho_kbn": request_data["shiharai_hoho_kbn"],
            "riyo_time_ymdhms": request_data["riyo_time_ymdhms"],
            "syori_tuban": request_data["syori_tuban"],
            "retry_flg": request_data["retry_flg"],
            "yokyu_kubun": request_data["yokyu_kubun"],
            "toiawase_kanryo_kubun": request_data["toiawase_kanryo_kubun"],
        }
    else:
        raise ValueError(f"問合せ完了区分の不正：{request_data["toiawase_kanryo_kubun"]}")
    return res

def get_order_info_dictionary(request_data:dict) -> dict:
    res:dict
    if (request_data["toiawase_kanryo_kubun"] == "1"):
        if (request_data["yokyu_kubun"] in {"E", "L"}):
            res = {}
        else:
            res = {
                "kensaku_key": request_data["kensaku_key"],
                "bar_code_no": "             ",
                "oto_kekka": "  ",
                "pay_type": " ",
                "dlv_type": " ",
                "tenpo_bango": request_data["mise_no"],
                "mise_namek": "○○店舗                            ",
                "mise_address": "住所（漢字）                                    ",
                "tenpo_tel_no": "029-298-0203",
                "keijyo_type": " ",
                "inshi_kijun": "      ",
                "kingaku_henko_flg": " ",
                "kino_kbn": " ",
                "haraikomi_no": "6" + str(request_data["kensaku_key"]) + str(calculate_CD("6" + str(request_data["kensaku_key"]))),
                "shop_id":"     ",
                "shuno_kingaku": "      ",
                "shohin_daikin": "000000",
                "shop_namek": "ショップ名                                        ",
                "user_namek": "お客様名                      ",
                "renraku_saki": "ショップ連絡先                                                  ",
            }
    elif (request_data["toiawase_kanryo_kubun"] == "2"):
        res = {
            "kensaku_key": request_data["kensaku_key"],
            "bar_code_no": request_data["bar_code_no"],
            "cvs_code": "8037110000004",
            "kino_kbn": request_data["kino_kbn"],
            "shop_id":request_data["shop_id"],
            "shuno_kingaku": request_data["shuno_kingaku"],
            "otoKekka_kubun": "99",
            "oto_kekka": "00"
        }
    else:
        raise ValueError(f"問合せ完了区分の不正：{request_data["toiawase_kanryo_kubun"]}")
    return res

def get_payback_info_dictionary(request_data:dict) -> dict:
    res:dict
    if (request_data["toiawase_kanryo_kubun"] == "1" and
        request_data["yokyu_kubun"] in {"E", "L"}):
        res = {
            "kessai_id": request_data["bar_code_no"][1:12],
            "bar_code_no": request_data["bar_code_no"],
            "oto_kekka": "00",
            "tenpo_bango": request_data["mise_no"],
            "mise_namek": "                                    ",
            "mise_address": "                                                ",
            "tenpo_tel_no": "029-298-0203",
            "haraikomi_no": "6" + str(request_data["bar_code_no"][1:12]) + str(calculate_CD("6" + str(request_data["bar_code_no"][1:12]))),
            "shop_id": request_data["shop_id"],
            "payback_kingaku": "000000",
            "shop_namek": "ショップ名                                        " ,
            "user_namek": "お客様名                      " ,
            "renraku_saki": "ショップ連絡先                                                  " ,
            "payback_start_ymd": "      ",
            "payback_end_ymd":"      ",
            "svc_time_start_hm": "    ",
            "svc_time_end_hm": "    ",
            "kogyo_name": "ハライモドシテスト                                                                                                                                                                                      ",
            "koen_date_ymd": "20250228",
            "hanken_yohi": "0",
            "fuka_riyu": "  ",
            "payback_tesuryo": "      ",
        }
    else:
        res = {}
    return res

def get_test_option(request_data:dict) -> tuple[int, str]:
    """
    optionの番号と文字列の取得
    """
    mapping_str:str
    mapping_no:int
    if request_data["yokyu_kubun"] in {"A", "B", "H", "J"} :
        # 検索キー:11桁
        mapping_str = request_data["kensaku_key"]
    elif request_data["yokyu_kubun"] in {"E", "L"}:
        # バーコードの3桁目から12桁目を取得:10桁
        mapping_str = request_data["bar_code_no"][2:12]

    # mapping_strを2進数にして、末尾2桁を取得
    bin_str = bin(int(mapping_str))[2:]
    bin_str = bin_str.zfill(2)
    mapping_no = int(bin_str[-2:],2)
    logger.debug(f"mapping_no: {mapping_no}")

    return (mapping_no, mapping_str)

def check_pia_ticket(shop_id:str) -> bool:
    """
    「チケットぴあ」か否かの判定
    """
    res:bool
    if (shop_id in {"30514","30515","30731","30732","30733","30734","30735","30736","30737","30738","30739"}):
        res = True
    else:
        res = False
    return res

def get_ec_ticket_count(map_num:int) -> int:
    """
    チケット発券枚数（EC関連問合せ No.1, No3マッピング対応）
    """
    res = req_res_map({
        0: 0,
        1: 1,
        2: 2,
        3: 10,
        4: 20,
    }, map_num, 0)
    return res

def get_ticket_info(request_data:dict, map_num:int, order_info:dict) -> dict:
    res:dict = {}
    if (request_data["toiawase_kanryo_kubun"] == "1" and
        request_data["yokyu_kubun"] == "A" and
        order_info["oto_kekka"] == "00"):
        ticket_count = get_ec_ticket_count(map_num)
        if check_pia_ticket(order_info["shop_id"]):
            for i in range(1, ticket_count + 1):
                res[f"html_name{i}"] = "NTPM000001"
                # ぴあチケット印刷用バーコードの生成
                B1_B12 = random.randint(0, 999999999999)
                B1_B12_str = str(B1_B12).zfill(12)
                res[f"barcode{i}"] = B1_B12_str + str(calculate_CD(B1_B12_str))
                res[f"ticket_data{i}"] = "NTPM000001"
        else:
            for i in range(1, ticket_count + 1):
                res[f"html_name{i}"] = "ETPI001102"
                res[f"barcode{i}"] = "             "
                res[f"ticket_data{i}"] = "NTPI001102"
                
    return res

def get_ec_query_pay_type(map_num:int)->str:
    """
    支払種別(EC関連問合せ)
    """
    res = req_res_map({
        0:"1", #前払い
        1:"2", #代金引換
        2:"3", #後払い
    }, map_num, "1")
    return res

def get_ec_query_dlv_type(map_num:int)->str:
    """
    納品種別(EC関連問合せ)
    """
    res = req_res_map({
        0:"1", #店渡し
        1:"2", #宅配
    }, map_num, "1")
    return res

def get_ec_query_keijyo_type(map_num:int) -> str:
    """
    売上計上区分(EC関連問合せ)
    """
    res = req_res_map({
        0:" ", #預り金計上
        1:"1", #売上計上
        2:"2", #売上計上/未収入金計上
    }, map_num, " ")
    return res

def get_ec_query_inshi_kijun(map_num:int)->str:
    """
    印紙基準額(EC関連問合せ)
    """
    res = req_res_map({
        0 : "      ", #" "（ALL半角空白）：未設定
        1 : "000000", #最低値
        2 : "001000", #一般値
        3 : "999999", #最大値
    }, map_num, "      ")
    return res

def get_ec_query_kingaku_henko_flg(map_num:int)->str:
    """
    価格変更フラグ(EC関連問合せ)
    """
    res = req_res_map({
        0 : " ", #" "（ALL半角空白）：未設定
        1 : "1", #合計金額の変更がある場合
    }, map_num, " ")
    return res

def get_ec_query_kino_kbn(map_num:int)->str:
    """
    機能区分(EC関連問合せ)
    """
    res = req_res_map({
        0 : "3", #チケット発券
        1 : "5", #新プリペイドサービス
    }, map_num, "3")
    return res

def get_ec_query_shuno_kingaku(map_num:int)->str:
    """
    収納金額（EC関連問合せ）
    """
    res = req_res_map({
        0 : "      ", #" "（ALL半角空白）：未設定
        1 : "000000", #最低値
        2 : "001000", #一般値
        3 : "999999", #最大値
    }, map_num, "000000")
    return res

def get_ec_kanryo_inshi_syukin_gaku(map_num:int)->str:
    """
    印紙基準額/収納金額(EC関連完了)
    """
    res = req_res_map({
        0 : "      ", #(ALL半角空白) :未設定
        1 : "000000", #最低値
        2 : "001000", #一般値
        3 : "999999", #最大値
    }, map_num, "      ")
    return res
