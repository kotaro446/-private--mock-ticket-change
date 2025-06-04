import toto_constant
from flask import request, Response
from toto_request_mapping_clearing import *
from toto_library import *

######################################################################
# メイン関数                                                          #
######################################################################

def resp_clearing(req:dict, segments:list, mapping_num:int) -> Response:
    """
    TOTO当せん返還消込要求のレスポンスを返す。

    Args:
        req (dict): リクエストデータ
        segments (list[int]): マッピング番号ごとに分割した数字リスト
        mapping_num (int): マッピング番号

    Returns:
        Response: レスポンス
    """
    # 必須項目チェック
    if validate_request_fields(req, toto_constant.VALIDATE_REQUEST_FIELDS_CLEARING):
        return generate_error_response()

    # デフォルトレスポンス
    resp_dict = create_default_resp_dict(req)

    # 処理結果の判定
    X_shori_kekka, httpstatus = get_X_shori_kekka_for_clearing_map_clearing(segments[4])
    if X_shori_kekka != "00":
        return generate_error_response(X_shori_kekka, httpstatus)

    return resp_clearing_map_clearing_case_success(req, segments, resp_dict)


######################################################################
# No.4_当せん返還消込応答_マッピング　の関数                            #
######################################################################

def resp_clearing_map_clearing_case_success(req:dict, segments:list, resp_dict:dict) -> Response:
    """
    TOTO当せん返還消込要求の正常レスポンスを返す。

    Args:
        req (dict): リクエストデータ
        segments (list[int]): マッピング番号ごとに分割した数字リスト
        mapping_num (int): マッピング番号

    Returns:
        Response: レスポンス
    """
    # 応答結果の取得
    resp_dict["X_outou_kekka"] = get_X_outou_kekka_for_clearing_map_clearing(segments[5])
    
    # 応答結果="00"：正常 または 応答結果="13"：totoセンターアプリエラー の場合、セットする
    if resp_dict["X_outou_kekka"] == "00":
        resp_dict["X_toto_kekka"] = "000000"
    elif resp_dict["X_outou_kekka"] == "13":
        resp_dict["X_toto_kekka"] = get_X_toto_kekka_for_clearing_map_clearing(segments[6])

    resp_xml = output_xml(resp_dict)
    return Response(resp_xml.encode(encoding='cp932'), status=200, content_type='text/xml; charset=Windows-31J')


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
    resp_dict["X_regi_date_min"] = req["X_regi_date_min"]
    resp_dict["X_shori_tuban"] = req["X_shori_tuban"]
    resp_dict["X_yokyu_kbn"] = req["X_yokyu_kbn"]
    resp_dict["X_barcode"] = req["X_barcode"]
    resp_dict["X_vote_ticket_barcode"] = req["X_vote_ticket_barcode"]
    resp_dict["X_toto_terminal_id"] = req["X_toto_terminal_id"]
    resp_dict["X_toto_terminal_kbn"] = req["X_toto_terminal_kbn"]
    resp_dict["X_toto_julian_date"] = req["X_toto_julian_date"]
    resp_dict["X_toto_julian_time"] = req["X_toto_julian_time"]
    resp_dict["X_pos_trade_no"] = req["X_pos_trade_no"]
    resp_dict["X_payback_flg"] = req["X_payback_flg"]
    resp_dict["X_outou_kekka"] = "00"
    resp_dict["X_toto_kekka"] = ""
    return resp_dict


def output_xml(resp_dict:dict) -> str:
    return f"""<?xml version="1.0" encoding="Shift_JIS"?>
<sejmsg xmlns="http://sej.co.jp/">
	<body>
		<X_shori_kekka>{resp_dict["X_shori_kekka"]}</X_shori_kekka>
		<X_kigyo_id>{resp_dict["X_kigyo_id"]}</X_kigyo_id>
		<X_mise_no>{resp_dict["X_mise_no"]}</X_mise_no>
		<X_regi_no>{resp_dict["X_regi_no"]}</X_regi_no>
		<X_regi_date_min>{resp_dict["X_regi_date_min"]}</X_regi_date_min>
		<X_shori_tuban>{resp_dict["X_shori_tuban"]}</X_shori_tuban>
		<X_yokyu_kbn>{resp_dict["X_yokyu_kbn"]}</X_yokyu_kbn>
		<X_barcode>{resp_dict["X_barcode"]}</X_barcode>
		<X_vote_ticket_barcode>{resp_dict["X_vote_ticket_barcode"]}</X_vote_ticket_barcode>
		<X_toto_terminal_id>{resp_dict["X_toto_terminal_id"]}</X_toto_terminal_id>
		<X_toto_terminal_kbn>{resp_dict["X_toto_terminal_kbn"]}</X_toto_terminal_kbn>
		<X_toto_julian_date>{resp_dict["X_toto_julian_date"]}</X_toto_julian_date>
		<X_toto_julian_time>{resp_dict["X_toto_julian_time"]}</X_toto_julian_time>
		<X_pos_trade_no>{resp_dict["X_pos_trade_no"]}</X_pos_trade_no>
		<X_payback_flg>{resp_dict["X_payback_flg"]}</X_payback_flg>
		<X_outou_kekka>{resp_dict["X_outou_kekka"]}</X_outou_kekka>
		<X_toto_kekka>{resp_dict["X_toto_kekka"]}</X_toto_kekka>
	</body>
</sejmsg>"""
