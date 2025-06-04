from logger import get_logger
logger = get_logger()
import in_const as in_const
from in_ticket_library import calculate_CD
import time
from in_ticket_base_library import (
    get_in_register_otoKekka_kubun,
    get_price,
    get_code,
    get_operation
)
from ticket_library import (
    req_res_map,
)


def get_in_ticket_base_register(req:dict, mapping:list)-> tuple[int,dict,dict,list]:
    """
    INチケットの登録

    parameters
    ----------
    req:dict  
    mapping:list

    Returns
    -------
    tuple[int, dict, dict, list]  
    - httpstatus: HTTPステータス
    - common_dict: 共通項目の辞書
    - success_dict: 成功時のみ値をセットする辞書
    - ticket_list: チケット情報リスト
    """
    success_dict = {}
    ticket_list = []
    (common_dict, httpstatus) = get_common_dict(req, mapping)
    if common_dict["X_shori_kekka"] == "00":
        success_dict = get_success_dict(req, common_dict, mapping)
        ticket_list = get_ticket_info_list(common_dict, success_dict)

    return (httpstatus, common_dict, success_dict, ticket_list)

def get_ticket_info_list(common_dict:dict, success_dict:dict) -> list:
    ticket_list=[]

    # 応答結果区分が01、03の場合のみtc_infoを設定
    if (common_dict["X_outou_kekka_kbn"] == "01" or
        common_dict["X_outou_kekka_kbn"] == "03"):
        ticket_info:tuple[str,str,str,str]
        X_tc_barcode_no:str
        X_tc_kbn = "1"
        X_tc_template:str
        tc_text:str
        if (common_dict["X_shop_id"] == "30514"):# ぴあの場合
            X_tc_template = "NTPA000001"
            tc_text = in_const.pia_text
        else:
            X_tc_template = "ETSNHN0001"
            tc_text = in_const.ticket_text
        # tc_infoループ
        for i in range(int(success_dict["X_ticket_cnt"])):
            X_tc_barcode_no = str(600000000001 + i) + str(calculate_CD(str(600000000001 + i)))
            ticket_info = (X_tc_barcode_no, X_tc_kbn, X_tc_template, tc_text)
            ticket_list.append(ticket_info)
    return ticket_list

def get_common_dict(req:dict, mapping:list) -> tuple[dict, int]:
    common_dict:dict
    # 処理結果
    (httpstatus, syori_kekka) = get_in_ticket_syori_kekka(req, mapping)

    if syori_kekka == "00":
        
        X_outou_kekka = get_in_ticket_oto_kekka(req, mapping)

        # ショップID
        X_shop_id = get_in_register_shopID(mapping[3])

        # 応答結果区分
        X_outou_kekka_kbn = get_in_register_otoKekka_kubun(mapping[4])

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
            "X_shop_id": X_shop_id,
            "X_order_id": "201100012581",
            "X_torikeshi_riyu": "",
            "X_kaishu_cnt": "",
            "X_outou_kekka_kbn": X_outou_kekka_kbn,
            "X_outou_kekka": X_outou_kekka,
        }
    else:
        common_dict = {
            "X_shori_kekka": syori_kekka,
        }
    return (common_dict, httpstatus)

def get_success_dict(req, common_dict, mapping) -> dict:
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

        (shop_namek,
         X_renraku_saki,
         namek,
         name_kana,
         X_post,
         X_mail) = get_print_info(common_dict)

        #レスポンス定義
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
            "X_post": X_post,
            "X_mail": X_mail,
            "X_ticket_hon_cnt": str(X_ticket_hon_cnt).zfill(2),
            "X_ticket_cnt": str(X_ticket_cnt).zfill(2),
            "X_hansoku_jan_code": X_hansoku_jan_code,
        }
    else:
        success_dict = {}
    return success_dict

def get_print_info(common_dict:dict) -> tuple[str,str,str,str,str,str]:
    shop_namek:str
    X_renraku_saki:str
    namek:str
    name_kana:str
    X_post:str
    X_mail:str
    # 応答結果区分が01、03の場合のみtc_infoを設定
    if ((common_dict["X_outou_kekka_kbn"] == "01" or
         common_dict["X_outou_kekka_kbn"] == "03") and
         common_dict["X_shop_id"] == "30514"):# ぴあの場合
        shop_namek = "ショップ名称漢字９０１２３４５６７８９０１２ＥＮＤ"
        X_renraku_saki = "ｼｮｯﾌﾟﾚﾝﾗｸｻｷ2345678901234567＿＠％＿67890123456789012345678901END"
        namek = "ｵｷｬｸｻﾏｼﾒｲ012345678901234567EN@"
        name_kana = "カナカナカナカナカナ"
        X_post = "9876543"
        X_mail = "0558-76-9208@yahoo.co.jp"
    else:
        shop_namek = "ｾﾌﾞﾝﾄﾞﾘｰﾑ(i.JTB 高速バス)",
        X_renraku_saki = "0570-01-6009(i.JTB HTA販売センター)",
        namek = "四谷太郎",
        name_kana = "ヨツヤタロウ",
        X_post = "9250001",
        X_mail = "aanm@sxxxx.xxxxx.com",
    return (shop_namek, X_renraku_saki, namek, name_kana, X_post, X_mail)


def get_in_ticket_syori_kekka(req:dict, mapping:list) -> tuple[int, str]:
    shori_kekka:str
    httpstatus:int
    # 処理結果
    (shori_kekka, httpstatus) = get_in_register_shori_kekka(mapping[1])
    
    # レスポンスパターン(再送区分用)
    pattern = get_in_register_response_saisoyo_kbn(mapping[7])

    # 再送時に、再送時正常の指定なら、処理結果を"00"で返す
    if (req["X_saiso_kbn"] == "1" and
        pattern == "0"):
        shori_kekka = "00"
        httpstatus = 200
    
    if not shori_kekka in ("00", "11", "14", "15", "99"):
        httpstatus = 400
    
    return (httpstatus, shori_kekka)

def get_in_ticket_oto_kekka(req:dict, mapping:list) -> str:

    # 応答結果
    oto_kekka = get_in_register_otoKekka(mapping[2])
    
    # レスポンスパターン(再送区分用)
    pattern = get_in_register_response_saisoyo_kbn(mapping[7])

    # 再送区分＝1　
    if (req["X_saiso_kbn"] == "1" and
        pattern == "0"):
        oto_kekka = "00"
    return oto_kekka

# 処理結果(問合せ用)
def get_in_register_shori_kekka(map_num:int) -> tuple[str, int]:
    res = req_res_map({
       0: ("00",200, False), #正常
       1: ("11",400, False), #業務区分エラー
       2: ("14",400, False), #サービス時間帯エラー
       3: ("15",400, True),  #タイムアウトエラー
       4: ("99",400, False), #その他エラー(400)
       5: ("99",500, False), #その他エラー(500)
       6: ("00",200, True),  #タイムアウト(正常)
       7: ("99",500, True),  #タイムアウト(その他エラー500)
    }, map_num, ("00",200, False))
    if res[2]:
           time.sleep(in_const.TIMEOUT_SEC)
    return res[:2]

# レスポンスパターン（再送区分用）
def get_in_register_response_saisoyo_kbn(map_num:int) -> str:
    res = req_res_map({
       0: "0", #再送正常系
       1: "1", #再送異常系
    }, map_num, "0")
    return res


# 応答結果(問合せ用)
def get_in_register_otoKekka(map_num:int)->str:
    res = req_res_map({
       0: "00", #正常応答
       1: "01", #検索キーエラー
       2: "02", #支払期限エラー
       3: "03", #支払済エラー
       4: "05", #決済中止エラー（ショップ取引停止エラー）
       5: "07", #発券済エラー
       6: "08", #発券期限エラー
       7: "13", #入金中止エラー
       8: "14", #発券開始前エラー
       9: "15", #発券中止エラー
       10:"99", #その他エラー
    }, map_num, "00")
    return res

# ショップID取得(問合せ用)
def get_in_register_shopID(map_num:int)->str:
    res = req_res_map({
        0: "30400", # "30400"：7DC
        1: "30512", # "30512"：旧ソフトバンクギフトショップ/組合せクーポンショップ
        2: "30513", # ”30513”：組合せクーポンショップ
        3: "30514", # ”30514”：チケットぴあ①
        4: "30701", # ”30701”：Mコピーインターネットチケット①
        5: "30731", # ”30731”：チケットぴあ②
        6: "30732", # ”30732”：チケットぴあ③
        7: "30773", # ”30773”：Mコピーインターネットチケット②
        8: "30775", # ”30775”：JTBレジャー（TDR）
    }, map_num, "30400")
    return res


