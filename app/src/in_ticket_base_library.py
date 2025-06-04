
from in_ticket_library import (
    calculate_CD,
)
from ticket_library import (
    req_res_map,
)

# 
def get_in_register_otoKekka_kubun(map_num:int) -> str:
    """
    応答結果区分(問合せ用)
    """
    res = req_res_map({
       0: "01", #代引き
       1: "02", #前払い（後日発券）
       2: "03", #代済発券
       3: "04", #前払いのみ
    }, map_num, "01")
    return res

# 
def get_in_register_ticket_daikin(map_num:int) -> str:
    """
    チケット代金/発券代金/チケット購入代金/印紙基準額(問合せ用)
    """
    res = req_res_map({
        0: "000000", #最低値
        1: "999999", #最大値
        2: "003500", #一般値
        3: "001000", #一般値
    }, map_num, "000000")
    return res

def get_in_register_ticket_maisu(map_num:int) -> int:
    """
    本券購入枚数/チケット枚数(問合せ用)
    """
    res = req_res_map({
        0: 1,
        1: 20,
    }, map_num, 1)
    return res

def get_price(common_dict:dict, mapping:list) -> tuple[str,str,str,str,str]:
    """
    金額関連の取得

    Parameter
    ---------
    common_dict:dict  
    mapping:list

    Return
    ------
    X_goukei:合計金額  
    X_tc_dai:チケット代金  
    X_tc_kounyu_dai:チケット購入代金  
    X_hakken_dai:発券代金
    X_inshi_kijun:印紙基準
    """
    # チケット代金
    X_tc_dai:str
    if common_dict["X_outou_kekka_kbn"] == "03":
        X_tc_dai = "000000"
    else:
        X_tc_dai = get_in_register_ticket_daikin(mapping[5])

    # チケット購入代金
    X_tc_kounyu_dai:str
    if common_dict["X_outou_kekka_kbn"] == "03":
        X_tc_kounyu_dai = "000000"
    else:
        X_tc_kounyu_dai = get_in_register_ticket_daikin(mapping[5])

    # 発券代金
    X_hakken_dai:str
    if common_dict["X_outou_kekka_kbn"] == "04":
        X_hakken_dai = "000000"
    else:
        X_hakken_dai = get_in_register_ticket_daikin(mapping[5])
    
    # 合計金額
    sumTemp = 0
    X_goukei:str
    if common_dict["X_outou_kekka_kbn"] == "02":
        sumTemp += int(X_tc_dai)
        sumTemp += int(X_tc_kounyu_dai)
    else:
        sumTemp += int(X_tc_dai)
        sumTemp += int(X_tc_kounyu_dai)
        sumTemp += int(X_hakken_dai)
    if sumTemp > 999999:
        X_goukei = "999999"
    else:
        X_goukei = f"""{sumTemp}""".zfill(6) 

    #印紙基準
    X_inshi_kijun =get_in_register_ticket_daikin(mapping[5])

    return (X_goukei, X_tc_dai, X_tc_kounyu_dai, X_hakken_dai, X_inshi_kijun)

def get_code(req:dict, common_dict:dict) -> tuple[str,str,str,str,str]:
    """
    コード、番号関連の取得

    Parameter
    ---------
    req:dict
    common_dict:dict  

    Return
    ------
    X_haraikomi:払込票番号
    X_haraikomi_org:払込票番号ORG
    X_hikikae:引換票番号
    X_hikikae_org:引換票番号ORG
    X_hansoku_jan_code:販促JANコード
    """
    # 払込票番号, 払込票番号ORG
    X_haraikomi:str
    X_haraikomi_org:str
    if common_dict["X_outou_kekka_kbn"] == "03":
        X_haraikomi = ""
        X_haraikomi_org = ""
    else:
        X_haraikomi = req["X_barcode"]
        X_haraikomi_org = req["X_barcode"]

    # 引換票番号, 引換票番号ORG
    X_hikikae:str
    X_hikikae_org:str
    if (common_dict["X_outou_kekka_kbn"] == "02" or
        common_dict["X_outou_kekka_kbn"] == "03"):

        work = req["X_barcode"]
        work = work[0] + "2" + work[2:12] 
        X_hikikae = work + str(calculate_CD(work))

        work = req["X_barcode"]
        work = work[0] + "2" + work[2:12]
        X_hikikae_org = work + str(calculate_CD(work))
    else:
        X_hikikae = ""
        X_hikikae_org = ""

    # 販促JANコード
    # 応答結果区分=04(前払いのみ) かつ 組合せクーポンショップ　　→13桁のＪＡＮコード(13固定)で応答
    X_hansoku_jan_code:str
    if (common_dict["X_outou_kekka_kbn"] == "04" and 
        common_dict["X_shop_id"] in {"30512","30513"}):
        X_hansoku_jan_code = "9850100001640"
    else:
        X_hansoku_jan_code = ""

    return (X_haraikomi, X_haraikomi_org, X_hikikae, X_hikikae_org, X_hansoku_jan_code)

def get_operation(common_dict:dict, mapping:list):
    """
    操作関連情報の取得

    Parameter
    ---------
    common_dict:dict  
    mapping:list

    Return
    ------
    X_hakken_mise_date:発券開始日時  
    X_hakken_lmt:発券期限日時  
    X_ticket_hon_cnt:本券購入枚数  
    X_ticket_cnt:チケット枚数
    """

    # 発券開始日時, 発券期限日時
    if common_dict["X_outou_kekka_kbn"] == "02":
        X_hakken_mise_date = "202401010000"
        X_hakken_lmt = "202512310000"
    else:
        X_hakken_mise_date = ""
        X_hakken_lmt = ""

    # 本券購入枚数, チケット枚数
    if (common_dict["X_outou_kekka_kbn"] == "01" or
        common_dict["X_outou_kekka_kbn"] == "03"): 
        X_ticket_hon_cnt = get_in_register_ticket_maisu(mapping[6])
        X_ticket_cnt = get_in_register_ticket_maisu(mapping[6])
    else:
        X_ticket_hon_cnt = "00"
        X_ticket_cnt = "00"  

    return (X_hakken_mise_date, X_hakken_lmt, X_ticket_hon_cnt, X_ticket_cnt)
