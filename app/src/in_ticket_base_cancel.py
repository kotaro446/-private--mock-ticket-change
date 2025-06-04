from logger import get_logger
logger = get_logger()
from in_ticket_base_library import (
    get_in_register_otoKekka_kubun,
    get_price,
    get_code,
    get_operation
)
import time
from ticket_library import (
    req_res_map,
)
import in_const as in_const

def get_in_ticket_base_cancel(req:dict, mapping:list) -> tuple[int, dict, dict]:
    """
    INチケットの取消

    parameters
    ----------
    req:dict  
    mapping:list

    Returns
    -------
    tuple[int, dict, dict]  
    - httpstatus: HTTPステータス
    - common_dict: 共通項目の辞書
    - success_dict: 成功時のみ値をセットする辞書
    """
    (common_dict, httpstatus) = get_common_dict(req, mapping)
    success_dict = get_success_dict(req, common_dict, mapping)

    return (httpstatus, common_dict, success_dict)

def get_success_dict(req:dict, common_dict:dict, mapping:list) -> dict:
    success_dict:dict
    if common_dict["X_shori_kekka"] == "00":
        (X_goukei,
         X_tc_dai,
         X_tc_kounyu_dai,
         X_hakken_dai,
         X_inshi_kijun) = get_price(common_dict, mapping)
        
        (X_haraikomi,
         X_haraikomi_org,
         X_hikikae,
         X_hikikae_org,
         X_hansoku_jan_code) = get_code(req, common_dict)

        (X_hakken_mise_date,
         X_hakken_lmt,
         X_ticket_hon_cnt,
         X_ticket_cnt) = get_operation(common_dict, mapping)

        success_dict = {
            "shop_namek": "ｾﾌﾞﾝﾄﾞﾘｰﾑ(i.JTB 高速バス)",
            "X_renraku_saki": "0570-01-6009(i.JTB HTA販売センター)",
            "X_haraikomi": X_haraikomi,
            "X_haraikomi_org": X_haraikomi_org,
            "X_hikikae": X_hikikae,
            "X_hikikae_org": X_hikikae_org,
            "X_hakken_mise_date": X_hakken_mise_date,
            "X_hakken_lmt": X_hakken_lmt,
            "X_goukei": X_goukei,
            "X_tc_dai": X_tc_dai,
            "X_tc_kounyu_dai": X_tc_kounyu_dai,
            "X_hakken_dai": X_hakken_dai,
            "X_inshi_kijun": X_inshi_kijun,
            "namek": "四谷太郎",
            "name_kana": "ヨツヤタロウ",
            "X_tel": "0557123456",
            "X_post": "9250001",
            "X_mail": "aanm@sxxxx.xxxxx.com",
            "X_ticket_hon_cnt": str(X_ticket_hon_cnt).zfill(2),
            "X_ticket_cnt": str(X_ticket_cnt).zfill(2),
            "X_hansoku_jan_code": X_hansoku_jan_code
        }
    else:
        success_dict = {}
    return success_dict




def get_common_dict(req:dict, mapping:list) -> tuple[dict,int]:

    common_dict:dict
    (httpstatus, syori_kekka) = get_in_ticket_syori_kekka(req, mapping)

    if syori_kekka == "00":
        # 取消応答結果(str)
        oto_kekka = get_in_ticket_oto_kekka(req, mapping)

        # 応答結果区分(str)
        oto_kekka_kubun = get_in_register_otoKekka_kubun(mapping[4])

        #レスポンス定義
        common_dict = {
            "X_shori_kekka": syori_kekka,
            "X_gyomu_kbn": req["X_gyomu_kbn"],
            "X_kigyo_id": req["X_kigyo_id"],
            "X_mise_no": req["X_mise_no"],
            "X_regi_no": req["X_regi_no"],
            "X_hakken_regi_no": req["X_hakken_regi_no"],
            "X_regi_date_min": req["X_regi_date_min"],
            "X_shori_tuban": req["X_shori_tuban"],
            "X_saiso_kbn": req["X_saiso_kbn"],
            "X_yokyu_kbn": req["X_yokyu_kbn"],
            "X_barcode": req["X_barcode"],
            "X_cvs_code": req["X_cvs_code"],
            "X_shop_id": req["X_shop_id"], 
            "X_order_id": req["X_order_id"],
            "X_torikeshi_riyu": req["X_torikeshi_riyu"],
            "X_kaishu_cnt": req["X_kaishu_cnt"],
            "X_outou_kekka_kbn": oto_kekka_kubun,
            "X_outou_kekka": oto_kekka,
        }
    else:
        common_dict = {
            "X_shori_kekka": syori_kekka,
        }
    return (common_dict, httpstatus)

def get_in_ticket_syori_kekka(req:dict, mapping:list) -> tuple[int, str]:
    # 取消処理結果(str)
    (shori_kekka, httpstatus) = get_in_register_torikeshi_shori_kekka(mapping[8])

    # レスポンスパターン(取消再送区分用)
    pattern = get_in_register_response_torikeshi_saisoyo_kbn(mapping[10])

    # 再送時に、再送時正常の指定なら、処理結果を"00"で返す
    if (req["X_saiso_kbn"] == "1" and
        pattern == "0"):
        shori_kekka = "00"
        httpstatus = 200

    return (httpstatus, shori_kekka)

def get_in_ticket_oto_kekka(req:dict, mapping:list) -> str:

    oto_kekka = get_in_register_torikeshi_otoKekka(mapping[9])
    
    # レスポンスパターン(取消再送区分用)
    pattern = get_in_register_response_torikeshi_saisoyo_kbn(mapping[10])

    # 再送区分1、再送正常
    if (req["X_saiso_kbn"] == "1" and
        pattern == "0"):    
        oto_kekka = "00"

    return oto_kekka

# 取消処理結果
def get_in_register_torikeshi_shori_kekka(map_num:int) -> tuple[str, int]:
    res = req_res_map({
        0: ("00",200, False), #正常
        1: ("10",400, False), #電文区分エラー
        2: ("11",400, False), #業務区分エラー
        3: ("14",400, False), #サービス時間帯エラー
        4: ("99",400, False), #その他エラー(400)
        5: ("99",500, False), #その他エラー(500)
        6: ("00",200, True),  #タイムアウト(正常)
        7: ("99",500, False), #タイムアウト(その他エラー500)
    }, map_num, ("00",200,False))
    if res[2]:
           time.sleep(in_const.TIMEOUT_SEC)
    return res[:2]

# 取消応答結果
def get_in_register_torikeshi_otoKekka(map_num:int) -> str:
    res = req_res_map({
        0: "00", #取消正常
        1: "01", #取消異常(検索キーエラー)
        2: "04", #取消異常(取消済み)
        3: "09", #発券取消済みエラー
        4: "60", #強制成立取消不可
        5: "99", #取消異常(その他エラー)
    }, map_num, "00")
    return res
   
# レスポンスパターン（取消再送区分用）
def get_in_register_response_torikeshi_saisoyo_kbn(map_num:int) -> str:
    res = req_res_map({
        0: "0", #再送正常
        1: "1", #再送異常
    }, map_num, "0")
    return res
