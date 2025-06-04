import os
import html
from in_ticket_library import calculate_CD
from logger import get_logger
logger = get_logger()
from ticket_library import (
    req_res_map,
)
from in_ticket_kenmen_library import (
    get_common_dict,
    get_success_dict,
    get_kenmen_info_mappingNO2,
)

def get_in_ticket_kenmen_register(req:dict, mapping:list) -> tuple[int,dict,dict,list]:
    """
    券面情報確認シナリオのINチケットの登録

    Parameters
    ----------
    req:dict  
    mapping:list  

    Returns
    -------
    httpstatus:int HTTPステータス  
    common_dict:dict 共通レスポンス  
    success_dict:dict 成功レスポンス  
    ticket_list:list チケット情報  
    """
    common_dict, httpstatus = get_common_dict(req, mapping)
    success_dict = get_success_dict(req, mapping, common_dict)
    ticket_list = get_ticket_list(common_dict, success_dict, mapping)
    return (httpstatus, common_dict, success_dict, ticket_list)

def get_ticket_list(common_dict:dict, success_dict:dict, mapping:list) -> list:
    """
    チケット情報取得処理
    """
    ticket_list = []
    # 応答結果区分が02、04の場合  チケット情報がセットされない（空タグセットもなし）
    if (common_dict["X_outou_kekka_kbn"] == "02" or
        common_dict["X_outou_kekka_kbn"] == "04"):
        ticket_list = []

    # 応答結果区分が01、03の場合のみtc_infoを設定
    elif (common_dict["X_outou_kekka_kbn"] == "01" or
          common_dict["X_outou_kekka_kbn"] == "03"):
        kenmen_list = get_kenmen_info_mappingNO2(mapping[8]) # 券面情報データ
        
        barcode_cnt = 0
        X_tc_barcode_no:str
        tc_info:tuple[str,str,str,str]

        logger.debug(f"tc_kenmen_info_result: {kenmen_list}")
        for cnt in range(int(success_dict["X_ticket_cnt"])):
            index = cnt % len(kenmen_list)
            # チケットバーコード番号
            if check_exist_barcode(kenmen_list[index]): # バーコード番号あり
                culc = f"{600000000001 + barcode_cnt}"
                X_tc_barcode_no = culc + str(calculate_CD(culc))
                barcode_cnt += 1
            else:
                X_tc_barcode_no = ""

            # チケット区分
            X_tc_kbn = get_ticket_kubun(kenmen_list[index])

            # テンプレートコードとXMLファイルコード
            (X_tc_template, XML_file_code) = get_templete_code(kenmen_list[index])

            # 券面情報
            tc_text = get_tc_text(XML_file_code, kenmen_list[index])

            tc_info = (X_tc_barcode_no, X_tc_kbn, X_tc_template, tc_text)
            ticket_list.append(tc_info)
    return ticket_list

def get_tc_text(file_code:str, kenmen_info:str) -> str:
    tc_text:str
    # XMLデータファイル名
    file_name = file_code + f"""_{kenmen_info}.xml"""

    # XMLデータファイルパス
    script_path = os.path.dirname(__file__).replace("\\", "/") # dirパス
    file_path = f"""{script_path}/ticketxml/{file_code}/{file_name}""" # ファイルのパス

    # ファイル読込
    with open(file_path, 'r', encoding='Windows-31J') as file:
        xml_content = file.read()
        tc_text = html.escape(xml_content, quote=True)
    return tc_text

def get_ticket_kubun(str_in:str) -> str:
    """
    チケット区分
    """
    res = req_res_map({
        "A" : "2",
        **dict.fromkeys(["B","C","T","V"], "1"),
        **dict.fromkeys(["D","U","W"], "4"),
        **dict.fromkeys(["E","F"], "3"),
    }, str_in[0], "1")
    return res

def check_exist_barcode(str_in:str) -> bool:
    """
    バーコード付きのチケットか否かのチェック

    Returns
    -------
    True: バーコード付き
    False: バーコード無し
    """
    res:bool
    if str_in in ("A", "D", "U", "W"):
        res = False
    else:
        res = True
    return res

def get_templete_code(str_in:str) -> tuple[str,str]:
    """
    文字列の先頭を参照して、テンプレートコードとXMLファイルコードを返す
    """
    res = req_res_map({
        "A": ("ETSNHN0003","NTSNHN0003"),
        "B": ("ETSNHQ0001","NTSNHQ0001"),
        "C": ("NTPA000001","NTPA000001"),
        "D": ("ETSNFN0001","NTSNFN0001"),
        "E": ("ETCN000006","NTCN000006"),
        "F": ("ETCN000006","NTCN000006"),
        **dict.fromkeys(["G","H","J","K","L","M","N"], ("TTPA000001","TTPA000001")),
        **dict.fromkeys(["P","R","S"], ("TTEP101355","TTEP101355")),
        **dict.fromkeys(["T","U"], ("NTST000010","NTST000010")),
        **dict.fromkeys(["V","W"], ("NTSW000010","NTSW000010")),
    }, str_in[0], ("ETSNHN0003","NTSNHN0003"))
    return res
