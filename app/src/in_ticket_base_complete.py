from logger import get_logger
logger = get_logger()
import time
import in_const as in_const

from ticket_library import (
    req_res_map,
)

def get_in_ticket_base_complete(req:dict, mapping:list) -> tuple[int, dict]:
    common_dict:dict

    # 処理結果
    (X_shori_kekka, httpstatus) = get_in_complete_shori_kekka(mapping[11])

    if X_shori_kekka == "00":
        # 応答結果(完了通知用)(str)
        X_outou_kekka = get_in_complete_otoKekka(mapping[12]) 

        # 回収枚数
        X_kaishu_cnt:str
        if req["X_yokyu_kbn"] == "02":
            # 回収枚数　要求区分="02"の場合は空タグセット
            X_kaishu_cnt = "" 
        elif req["X_yokyu_kbn"] == "12":
            # 回収枚数　問合せＰＯＳＴデータの内容と同様。
            X_kaishu_cnt = req["X_kaishu_cnt"]

        #レスポンス定義
        common_dict = {
            "X_shori_kekka": X_shori_kekka,
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
            "X_nyuukin": req["X_nyuukin"],
            "X_kaishu_cnt": X_kaishu_cnt,
            "X_outou_kekka_kbn":"99",
            "X_outou_kekka":X_outou_kekka,
        }
    else:
        common_dict = {
            "X_shori_kekka": X_shori_kekka,
        }
    return (httpstatus, common_dict)

def get_in_complete_shori_kekka(map_num:int) -> tuple[str,int]:
    """
    処理結果(完了通知用)
    """
    res = req_res_map({
        0: ("00", 200, False), #正常
        1: ("11", 400, False), #業務区分エラー
        2: ("14", 400, False), #サービス時間帯エラー
        3: ("15", 400, True),  #タイムアウトエラー
        4: ("99", 400, False), #その他エラー (400)
        5: ("99", 500, False), #その他エラー (500)
        6: ("00", 200, True),  #タイムアウト（正常）
        7: ("99", 500, True), #タイムアウト（その他エラー500)
    }, map_num, ("00", 200, False))
    if res[2]:
        time.sleep(in_const.TIMEOUT_SEC)
    return res[:2]

def get_in_complete_otoKekka(map_num:int)->str:
    """
    応答結果(完了通知用)
    """
    res = req_res_map({
        0: "00", #正常応答
        1: "01", #検索キーエラー
        2: "99", #その他エラー
    }, map_num, "00")
    return res

