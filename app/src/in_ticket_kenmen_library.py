from ticket_library import (
    req_res_map,
)
from in_ticket_library import calculate_CD

def get_common_dict(req:dict, mapping:list) -> tuple[dict,int]:

        X_shop_id = get_shopID_mappingNO2(mapping[1]) # shopID

        X_outou_kekka_kbn = get_otoKekka_kubun_mappingNO2(mapping[2]) # 応答結果区分

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
            "X_shop_id": X_shop_id, 
            "X_order_id": "201100012581",
            "X_torikeshi_riyu": "",
            "X_kaishu_cnt": "",
            "X_outou_kekka_kbn": X_outou_kekka_kbn,
            "X_outou_kekka": "00",
        }
        return (common_dict, 200)

def get_success_dict(req:dict, mapping:list, common_dict:dict)->dict:
    success_dict:dict
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

    (shop_namek,
     X_renraku_saki,
     namek,
     name_kana,
     X_post,
     X_mail) = get_print_info(common_dict)

    success_dict = {
        "shop_namek": shop_namek,
        "X_renraku_saki": X_renraku_saki,
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
        "namek": namek,
        "name_kana": name_kana,
        "X_tel": "0557123456",
        "X_post":X_post ,
        "X_mail": X_mail,
        "X_ticket_hon_cnt": str(X_ticket_hon_cnt).zfill(2),
        "X_ticket_cnt": str(X_ticket_cnt).zfill(2),
        "X_hansoku_jan_code": X_hansoku_jan_code
    }
    return success_dict


def get_shopID_mappingNO2(map_num:int) -> str:
    """
    マッピング2　ショップID
    """
    res = req_res_map({
        0: "30400", # 7DC
        1: "30501", # CNプレイガイド
        2: "30512", # 旧ソフトバンクギフトショップ 組合せクーポンショップ
        3: "30513", # 組合せクーポンショップ
        4: "30514", # チケットぴあ①
        5: "30701", # Mコピーインターネットチケット①
        6: "30731", # チケットぴあ②
        7: "30732", # チケットぴあ③
        8: "30773", # Mコピーインターネットチケット②
        9: "30775", # JTBレジャー（TDR）
        10:"30705", # Webインターネットチケット
    }, map_num, "30400")
    return res

def get_otoKekka_kubun_mappingNO2(map_num:str)->str:
    """
    マッピング2　応答結果区分
    """
    res = req_res_map({
        0: "01", # 01代引き
        1: "02", # 02前払い（後日発券）
        2: "03", # 03代済発券
        3: "04", # 前払いのみ
    }, map_num, "01")
    return res


def get_price(common_dict:dict, mapping:list)->tuple[str,str,str,str,str]:

    # チケット代金, チケット購入代金
    X_tc_dai:str
    X_tc_kounyu_dai:str
    if common_dict["X_outou_kekka_kbn"] == "03":
        X_tc_dai = "000000"
        X_tc_kounyu_dai = "000000"
    else:
        X_tc_dai = get_ticket_daikin_mappingNO2(mapping[3])
        X_tc_kounyu_dai =  get_ticketkounyu_daikin_mappingNO2(mapping[5])

    # 発券代金
    X_hakken_dai:str
    if common_dict["X_outou_kekka_kbn"] == "04":
        X_hakken_dai = "000000"
    else:
        X_hakken_dai = get_hakken_daikin_mappingNO2(mapping[4]) 
    
    # 合計金額
    sumTemp = 0
    X_goukei:str
    # 「応答結果区分」="02"：前払い(後日発券)時の「合計金額」にはその発券代金は加算されない
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

    X_inshi_kijun = get_inshi_kijyungaku_mappingNO2(mapping[6]) # 印紙基準額

    return (X_goukei, X_tc_dai, X_tc_kounyu_dai, X_hakken_dai, X_inshi_kijun)

def get_code(req:dict, common_dict:dict) -> tuple[str,str,str,str,str]:

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
    X_hansoku_jan_code:str
    # 応答結果区分=04(前払いのみ) かつ 組合せクーポンショップ　　→13桁のＪＡＮコード(13固定)で応答
    if (common_dict["X_outou_kekka_kbn"] == "04" and
        common_dict["X_shop_id"] in {"30512","30513"}):
        X_hansoku_jan_code = "9850100001640"
    else:
        X_hansoku_jan_code = ""
    
    return (X_haraikomi, X_haraikomi_org, X_hikikae, X_hikikae_org, X_hansoku_jan_code)

def get_operation(common_dict:dict, mapping:list) -> tuple[str,str,str,str]:
    # 発券開始日時, 発券期限日時
    if common_dict["X_outou_kekka_kbn"] == "02":
        X_hakken_mise_date = "202401010000"
        X_hakken_lmt = "202512310000"
    else:
        X_hakken_mise_date = ""
        X_hakken_lmt = ""

    # チケット枚数
    X_ticket_cnt:int
    if (common_dict["X_outou_kekka_kbn"] == "01" or
        common_dict["X_outou_kekka_kbn"] == "03"):
        X_ticket_cnt = get_ticket_maisu_mappingNO2(mapping[7])
    else:
        X_ticket_cnt = 0

    # 本券購入枚数
    X_ticket_hon_cnt = 0
    kenmen_list = get_kenmen_info_mappingNO2(mapping[8]) # 券面情報データ
    # 券面情報各パターン
    for i in range(X_ticket_cnt):
        index = i % len(kenmen_list)
        # チケット種類の判断(本券・副券)
        if check_honken(kenmen_list[index]): #本券
            X_ticket_hon_cnt += 1

    return (X_hakken_mise_date, X_hakken_lmt, str(X_ticket_hon_cnt), str(X_ticket_cnt))

def get_print_info(common_dict:dict) -> tuple[str,str,str,str,str,str]:
    shop_namek:str
    X_renraku_saki:str
    namek:str
    name_kana:str
    X_post:str
    X_mail:str
    # ぴあの場合
    if common_dict["X_shop_id"] == "30514":
        # ぴあの場合
        shop_namek = "ショップ名称漢字９０１２３４５６７８９０１２ＥＮＤ"
        X_renraku_saki = "ｼｮｯﾌﾟﾚﾝﾗｸｻｷ2345678901234567＿＠％＿67890123456789012345678901END"
        namek = "ｵｷｬｸｻﾏｼﾒｲ012345678901234567EN@"
        name_kana = "カナカナカナカナカナ"
        X_post = "9876543"
        X_mail = "0558-76-9208@yahoo.co.jp"
    else:
        shop_namek = "ｾﾌﾞﾝﾄﾞﾘｰﾑ(i.JTB 高速バス)"
        X_renraku_saki = "0570-01-6009(i.JTB HTA販売センター)"
        namek = "四谷太郎"
        name_kana = "ヨツヤタロウ"
        X_post = "9250001"
        X_mail = "aanm@sxxxx.xxxxx.com"
    return (shop_namek, X_renraku_saki, namek, name_kana, X_post, X_mail)

def get_ticket_daikin_mappingNO2(map_num:int)->str:
    """
    マッピング2　チケット代金
    """
    res = req_res_map({
        0: "000000", # 最低値
        1: "999999", # 最大値
        2: "003500", # 一般値
        3: "001000",
    }, map_num, "000000")
    return res

def get_hakken_daikin_mappingNO2(map_num:int)->str:
    """
    マッピング2　発券代金
    """
    res = req_res_map({
        0: "000000", # 最低値
        1: "999999", # 最大値
        2: "003500", # 一般値
        3: "001000",
    }, map_num, "000000")
    return res

def get_ticketkounyu_daikin_mappingNO2(map_num:int)->str:
    """
    マッピング2　チケット購入代金
    """
    res = req_res_map({
        0: "000000", # 最低値
        1: "999999", # 最大値
        2: "003500", # 一般値
        3: "001000",
    }, map_num, "000000")
    return res

def get_inshi_kijyungaku_mappingNO2(map_num:int) -> str:
    """
    マッピング2　印紙基準額
    """
    res = req_res_map({
        0: "000000", # 最低値
        1: "999999", # 最大値
        2: "003500", # 一般値
        3: "001000",
    }, map_num, "000000")
    return res

# マッピング2　券面情報データ（本券）   
def get_kenmen_info_mappingNO2(map_num:int) -> list:
    res = req_res_map({
        0:  ["A"],
        1:  ["B"],
        2:  ["C"],
        3:  ["A","D"],
        4:  ["A","E"],
        5:  ["A","F"],
        6:  ["B","D"],
        7:  ["B","E"],
        8:  ["B","F"],
        9:  ["C","D"],
        10: ["C","E"],
        11: ["C","F"],
        12: ["G"],
        13: ["H01","H02"],
        14: ["J01","J02"],
        15: ["K01","K02","K03","K04"],
        16: ["L01","L02","L03","L04","L05","L06","L07","L08","L09","L10","L11","L12","L13","L14","L15","L16","L17","L18","L19","L20"],
        17: ["M01","M02","M03","M04","M05","M06","M07","M08","M09","M10","M11","M12","M13","M14","M15","M16","M17","M18","M19","M20"],
        18: ["N01","N02","N03","N04","N05","N06","N07","N08","N09","N10","N11","N12","N13","N14","N15","N16","N17","N18","N19","N20"],
        19: ["P01","P02","P03","P04","P05","P06","P07","P08","P09","P10","P11","P12","P13","P14","P15","P16","P17","P18","P19","P20"],
        20: ["R01","R02","R03","R04","R05","R06","R07","R08","R09","R10","R11","R12","R13","R14","R15","R16","R17","R18","R19","R20"],
        21: ["S01","S02","S03","S04","S05","S06","S07","S08","S09","S10","S11","S12","S13","S14","S15","S16","S17","S18","S19","S20"],
        22: ["T","U"],
        23: ["V","W"],
    }, map_num, ["A"])
    return res



def get_ticket_maisu_mappingNO2(map_num:int) -> int:
    """
    マッピング2　チケット枚数
    """
    res = req_res_map({
        0:  0,
        1:  1,
        2:  2,
        3:  3,
        4:  4,
        5:  5,
        6:  6,
        7:  7,
        8:  8,
        9:  9,
        10: 10,
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        15: 15,
        16: 16,
        17: 17,
        18: 18,
        19: 19,
        20: 20,
    }, map_num, 0)
    return res


def check_honken(str_in:str) -> bool:
    """
    本件か否かのチェック

    Returns
    -------
    True: 本券
    False: 副券
    """
    res:bool
    if str_in in ("D", "E", "F", "U", "W"):
        res = False
    else:
        res = True
    return res
