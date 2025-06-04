def get_in_ticket_kenmen_complete(req:dict) -> tuple[dict,int]:
    httpstatus = 200
    # 回収枚数
    X_kaishu_cnt:str
    if req["X_yokyu_kbn"] == "02":
        X_kaishu_cnt = "" 
    elif req["X_yokyu_kbn"] == "12":
        X_kaishu_cnt = req["X_kaishu_cnt"]

    #レスポンス定義
    common_dict = {
        "X_shori_kekka": "00",
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
        "X_outou_kekka":"00"
    }
    return (common_dict, httpstatus)
