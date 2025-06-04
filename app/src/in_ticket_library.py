from logger import get_logger
logger = get_logger()

def get_mapping(req:dict) -> tuple[int,str]:
    mapping_no:int
    mapping_str:str

    # マッピング文字列取得
    if "X_barcode" in req:
        mapping_str = req["X_barcode"][2:12]
    
        # 2進数に変換
        bin_mapping_str = bin(int(mapping_str))[2:]

        # マッピング番号(int)
        mapping_no = int(bin_mapping_str[-1])
    else:
        raise ValueError("リクエストが不足しています。X_barcodeがない。")

    return (mapping_no, mapping_str)


def in_ticket_validate_check(req:dict) -> str:
    """
    validateチェックをする
    """
    res:str
    if "X_yokyu_kbn" not in req:
        res = "99"
        logger.debug(f"要求区分が必須項目。syori_kekka: {res}")
    elif req["X_yokyu_kbn"] not in {"01", "21", "02", "12"}:
        res = "99"
        logger.debug(f"要求区分が不正。X_yokyu_kbn: {req["X_yokyu_kbn"]}")
    elif "X_barcode"  not in req:
        res = "99"
        logger.debug(f"バーコードが必須項目。syori_kekka: {res}")
    elif check_key(req) == False:
        res = "99"
        logger.debug(f"リクエストが不足しています。syori_kekka: {res}")
    else:
        res = "00"
    return res

def check_key(req:dict) -> bool:
    res:bool
    keys = []
    if (req["X_yokyu_kbn"] == "01"):
        keys = ["X_shori_kekka",
                "X_gyomu_kbn",
                "X_kigyo_id",
                "X_mise_no",
                "X_regi_no",
                "X_hakken_regi_no",
                "X_regi_date_min",
                "X_shori_tuban",
                "X_saiso_kbn",
                "X_yokyu_kbn",
                "X_barcode",
                "X_cvs_code"]
    elif (req["X_yokyu_kbn"] == "21"):
        keys = ["X_shori_kekka",
                "X_gyomu_kbn",
                "X_kigyo_id",
                "X_mise_no",
                "X_regi_no",
                "X_hakken_regi_no",
                "X_regi_date_min", 
                "X_shori_tuban",
                "X_saiso_kbn",
                "X_yokyu_kbn",
                "X_barcode",
                "X_cvs_code",
                "X_shop_id",
                "X_order_id",
                "X_torikeshi_riyu",
                "X_kaishu_cnt"]
    elif (req["X_yokyu_kbn"] == "02"):
        keys = ["X_shori_kekka", 
                "X_gyomu_kbn", 
                "X_kigyo_id", 
                "X_mise_no", 
                "X_regi_no", 
                "X_hakken_regi_no", 
                "X_regi_date_min", 
                "X_shori_tuban", 
                "X_saiso_kbn", 
                "X_yokyu_kbn", 
                "X_barcode", 
                "X_cvs_code", 
                "X_shop_id", 
                "X_order_id", 
                "X_nyuukin"]
    elif (req["X_yokyu_kbn"] == "12"):
        keys = ["X_shori_kekka", 
                "X_gyomu_kbn", 
                "X_kigyo_id", 
                "X_mise_no", 
                "X_regi_no", 
                "X_hakken_regi_no", 
                "X_regi_date_min",
                "X_shori_tuban", 
                "X_saiso_kbn", 
                "X_yokyu_kbn", 
                "X_barcode", 
                "X_cvs_code", 
                "X_shop_id", 
                "X_order_id", 
                "X_nyuukin", 
                "X_kaishu_cnt"]

    # keyのチェック
    if all(key in req for key in keys):
        res = True
    else:
        res = False
    return res


#CD計算方法(ＪＡＮ－１３コード等に使用)
def calculate_CD(decimal_string):
    # 初期値
    A = 0
    # 右側からサーチ，奇数桁/偶数桁を判断
    for i, char in enumerate(reversed(decimal_string), start=1):
        num = int(char)
        if i % 2 == 1:  # 奇数桁
            A += num * 3
        else:  # 偶数桁
            A += num * 1
    # 計算 B、C
    B = A % 10
    C = 10 - B if B != 0 else 0  # 計算結果が１０だったら０とする
    return C

