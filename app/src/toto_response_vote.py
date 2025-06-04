import html
import os
import random
import toto_constant
from flask import request, Response
from toto_request_mapping_vote import *
from toto_library import *

######################################################################
# メイン関数                                                          #
######################################################################

def resp_vote(req:dict, segments:list, mapping_num:int) -> Response:
    """
    TOTO本投票要求のレスポンスを返す。

    Args:
        req (dict): リクエストデータ
        segments (list[int]): マッピング番号ごとに分割した数字リスト
        mapping_num (int): マッピング番号

    Returns:
        Response: レスポンス
    """
    # 必須項目チェック
    if validate_request_fields(req, toto_constant.VALIDATE_REQUEST_FIELDS_VOTE):
        return generate_error_response()

    # デフォルトレスポンス
    resp_dict = create_default_resp_dict(req)

    # 処理結果の判定
    X_shori_kekka, httpstatus = get_X_shori_kekka_for_vote_map_vote(segments[4])
    if X_shori_kekka != "00":
        return generate_error_response(X_shori_kekka, httpstatus)
    
    return resp_vote_map_vote_case_success(req, segments, resp_dict)


######################################################################
# No.2_本投票・本投票障害取消応答_マッピング　の関数                     #
######################################################################

def resp_vote_map_vote_case_success(req:dict, segments:list, resp_dict:dict) -> Response:
    """
    No.2_本投票・本投票障害取消応答_マッピング
    正常の場合のTOTO本投票要求のレスポンスを返す。

    Args:
        req (dict): リクエストデータ
        segments (list[int]): マッピング番号ごとに分割した数字リスト
        resp_dict (dict): レスポンスデータ

    Returns:
        Response: レスポンス
    """
    # 応答結果の取得
    resp_dict["X_outou_kekka"] = get_X_outou_kekka_for_vote_mapi_vote(segments[5])
    
    # 応答結果="00"：正常 または 応答結果="13"：totoセンターアプリエラー の場合、セットする
    if resp_dict["X_outou_kekka"] == "00":
        resp_dict["X_toto_kekka"] = "000000"
    elif resp_dict["X_outou_kekka"] == "13":
        resp_dict["X_toto_kekka"] = get_X_toto_kekka_for_vote_map_vote(segments[8])

    # 応答結果="00"：正常 の場合、セットする
    if resp_dict["X_outou_kekka"] == "00":
        resp_dict["X_ticket_cnt"] = str(get_X_ticket_cnt_for_purchase_map_vote(segments[1])).zfill(2)
    
    # チケット情報リストの生成
    tc_info_dict_list = create_tc_info_dict_list(segments, resp_dict)
    
    resp_xml = output_xml(resp_dict, tc_info_dict_list)
    return Response(resp_xml.encode(encoding='cp932'), status=200, content_type='text/xml; charset=Windows-31J')


def create_tc_info_dict_list(segments:list, resp_dict:dict) -> list:
    """
    No.2_本投票・本投票障害取消応答_マッピング
    チケット情報リストを生成する。

    Args:
        segments (list[int]): マッピング番号ごとに分割した数字リスト
        resp_dict (dict): レスポンスデータ

    Returns:
        list[dict]: チケット情報リスト
    """
    # 「応答結果」に"00"：正常以外のエラー応答がセットされる場合は、それより後の項目は空タグをセットする
    if resp_dict["X_outou_kekka"] != "00":
        return []

    tc_text_ID = get_tc_text_ID_for_vote_map_vote(segments[6])
    ticket_print_flag = get_whether_print_ticket_barcode_number_for_vote_map_vote(segments[7])
    ticket_cnt_int = int(resp_dict["X_ticket_cnt"])

    tc_info_dict_list = []
    for ticket_number in range(1, ticket_cnt_int + 1):
        tc_info_dict = {}
        tc_info_dict["X_vote_ticket_barcode"] = create_X_vote_ticket_barcode(ticket_print_flag)
        tc_info_dict["X_tc_template"] = get_template_code_for_vote_map_vote(tc_text_ID)
        file_name = tc_info_dict["X_tc_template"] + f"""_{tc_text_ID}.xml"""
        script_path = os.path.dirname(__file__).replace("\\", "/")
        file_path = f"""{script_path}/ticketxml/{tc_info_dict["X_tc_template"]}/{file_name}"""
        with open(file_path, 'r', encoding='cp932') as file:
            xml_content = file.read()
            text = html.escape(xml_content, quote=True)
        tc_info_dict["tc_text"] = text
        tc_info_dict_list.append(tc_info_dict)
    
    return tc_info_dict_list


def create_X_vote_ticket_barcode(ticket_print_flag:bool) -> str:
    """
    No.2_本投票・本投票障害取消応答_マッピング
    投票券バーコード番号を生成する。

    Args:
        ticket_print_flag (bool): 投票券バーコード番号印字要否

    Returns:
        str: 投票券バーコード番号
    """
    # 投票券バーコード番号印字要否が FALSE の場合、空文字を返す。
    if not ticket_print_flag:
        return ""

    B1_B12 = random.randint(0, 999999999999)
    B1_B12_str = str(B1_B12).zfill(12)
    C_D = (int('92' + B1_B12_str)) % 7
    return B1_B12_str + str(C_D)


######################################################################
# 共通関数                                                            #
######################################################################

def create_default_resp_dict(req:dict) -> dict:
    """
    辞書型レスポンスの初期値を設定する。

    Args:
        req (dict): リクエストデータ

    Returns:
        dict: 辞書型のレスポンス
    """
    resp_dict = {}
    resp_dict["X_shori_kekka"] = "00"
    resp_dict["X_kigyo_id"] = req["X_kigyo_id"]
    resp_dict["X_mise_no"] = req["X_mise_no"]
    resp_dict["X_regi_no"] = req["X_regi_no"]
    resp_dict["X_hakken_regi_no"] = req["X_hakken_regi_no"]
    resp_dict["X_regi_date_min"] = req["X_regi_date_min"]
    resp_dict["X_shori_tuban"] = req["X_shori_tuban"]
    resp_dict["X_yokyu_kbn"] = req["X_yokyu_kbn"]
    resp_dict["X_barcode"] = req["X_barcode"]
    resp_dict["X_torikeshi_riyu"] = ""
    resp_dict["X_toto_terminal_id"] = req["X_toto_terminal_id"]
    resp_dict["X_toto_terminal_kbn"] = req["X_toto_terminal_kbn"]
    resp_dict["X_toto_julian_date"] = req["X_toto_julian_date"]
    resp_dict["X_toto_julian_time"] = req["X_toto_julian_time"]
    resp_dict["X_toto_soukan_id"] = req["X_toto_soukan_id"]
    resp_dict["X_torikeshi_riyu_kbn"] = ""
    resp_dict["X_outou_kekka"] = "00"
    resp_dict["X_toto_kekka"] = ""
    resp_dict["X_ticket_cnt"] = ""
    return resp_dict


def output_xml(resp_dict:dict, tc_info_dict_list:list) -> str:
    tc_info_xml = ""
    for index, tc_info_dict in enumerate(tc_info_dict_list, start=1):
        tc_info_xml += f"""
		<tc_info no="{index}">
			<X_vote_ticket_barcode>{tc_info_dict["X_vote_ticket_barcode"]}</X_vote_ticket_barcode>
			<X_tc_template>{tc_info_dict["X_tc_template"]}</X_tc_template>
			<tc_text>{tc_info_dict["tc_text"]}</tc_text>
		</tc_info>"""

    return f"""<?xml version="1.0" encoding="Shift_JIS"?>
<sejmsg xmlns="http://sej.co.jp/">
	<body>
		<X_shori_kekka>{resp_dict["X_shori_kekka"]}</X_shori_kekka>
		<X_kigyo_id>{resp_dict["X_kigyo_id"]}</X_kigyo_id>
		<X_mise_no>{resp_dict["X_mise_no"]}</X_mise_no>
		<X_regi_no>{resp_dict["X_regi_no"]}</X_regi_no>
		<X_hakken_regi_no>{resp_dict["X_hakken_regi_no"]}</X_hakken_regi_no>
		<X_regi_date_min>{resp_dict["X_regi_date_min"]}</X_regi_date_min>
		<X_shori_tuban>{resp_dict["X_shori_tuban"]}</X_shori_tuban>
		<X_yokyu_kbn>{resp_dict["X_yokyu_kbn"]}</X_yokyu_kbn>
		<X_barcode>{resp_dict["X_barcode"]}</X_barcode>
		<X_torikeshi_riyu>{resp_dict["X_torikeshi_riyu"]}</X_torikeshi_riyu>
		<X_toto_terminal_id>{resp_dict["X_toto_terminal_id"]}</X_toto_terminal_id>
		<X_toto_terminal_kbn>{resp_dict["X_toto_terminal_kbn"]}</X_toto_terminal_kbn>
		<X_toto_julian_date>{resp_dict["X_toto_julian_date"]}</X_toto_julian_date>
		<X_toto_julian_time>{resp_dict["X_toto_julian_time"]}</X_toto_julian_time>
		<X_toto_soukan_id>{resp_dict["X_toto_soukan_id"]}</X_toto_soukan_id>
		<X_torikeshi_riyu_kbn>{resp_dict["X_torikeshi_riyu_kbn"]}</X_torikeshi_riyu_kbn>
		<X_outou_kekka>{resp_dict["X_outou_kekka"]}</X_outou_kekka>
		<X_toto_kekka>{resp_dict["X_toto_kekka"]}</X_toto_kekka>
		<X_ticket_cnt>{resp_dict["X_ticket_cnt"]}</X_ticket_cnt>{tc_info_xml}
	</body>
</sejmsg>"""
