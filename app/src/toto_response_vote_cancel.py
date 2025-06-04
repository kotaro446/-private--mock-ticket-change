import toto_constant
from flask import request, Response
from toto_request_mapping_vote import *
from toto_library import *

######################################################################
# メイン関数                                                          #
######################################################################

def resp_vote_cancel(req:dict, segments:list, mapping_num:int) -> Response:
    """
    TOTO本投票障害取消要求のレスポンスを返す。

    Args:
        req (dict): リクエストデータ
        segments (list[int]): マッピング番号ごとに分割した数字リスト
        mapping_num (int): マッピング番号

    Returns:
        Response: レスポンス
    """
    # 必須項目チェック
    if validate_request_fields(req, toto_constant.VALIDATE_REQUEST_FIELDS_VOTE_CANCEL):
        return generate_error_response()

    # デフォルトレスポンス
    resp_dict = create_default_resp_dict(req)

    # 処理結果の判定
    X_shori_kekka, httpstatus = get_X_shori_kekka_for_vote_cancel_map_vote(segments[9])
    if X_shori_kekka != "00":
        return generate_error_response(X_shori_kekka, httpstatus)
    
    return resp_vote_cancel_map_vote_case_success(req, segments, resp_dict)


######################################################################
# No.2_本投票・本投票障害取消応答_マッピング　の関数                     #
######################################################################

def resp_vote_cancel_map_vote_case_success(req:dict, segments:list, resp_dict:dict) -> Response:
    """
    No.2_本投票・本投票障害取消応答_マッピング
    TOTO本投票障害取消要求の正常レスポンスを返す。

    Args:
        req (dict): リクエストデータ
        segments (list[int]): マッピング番号ごとに分割した数字リスト
        mapping_num (int): マッピング番号

    Returns:
        Response: レスポンス
    """
    # 応答結果の取得
    resp_dict["X_outou_kekka"] = get_X_outou_kekka_for_vote_cancel_map_vote(segments[10])
    
    # 応答結果="00"：正常 または 応答結果="13"：totoセンターアプリエラー の場合、セットする
    if resp_dict["X_outou_kekka"] == "00":
        resp_dict["X_toto_kekka"] = "000000"
    elif resp_dict["X_outou_kekka"] == "13":
        resp_dict["X_toto_kekka"] = get_X_toto_kekka_for_vote_map_vote(segments[11])

    # 応答結果="00"：正常 の場合、セットする
    if resp_dict["X_outou_kekka"] == "00":
        resp_dict["X_ticket_cnt"] = str(get_X_ticket_cnt_for_purchase_map_vote(segments[1])).zfill(2)

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
    resp_dict["X_hakken_regi_no"] = req["X_hakken_regi_no"]
    resp_dict["X_regi_date_min"] = req["X_regi_date_min"]
    resp_dict["X_shori_tuban"] = req["X_shori_tuban"]
    resp_dict["X_yokyu_kbn"] = req["X_yokyu_kbn"]
    resp_dict["X_barcode"] = req["X_barcode"]
    resp_dict["X_torikeshi_riyu"] = req["X_torikeshi_riyu"]
    resp_dict["X_toto_terminal_id"] = req["X_toto_terminal_id"]
    resp_dict["X_toto_terminal_kbn"] = req["X_toto_terminal_kbn"]
    resp_dict["X_toto_julian_date"] = req["X_toto_julian_date"]
    resp_dict["X_toto_julian_time"] = req["X_toto_julian_time"]
    resp_dict["X_toto_soukan_id"] = req["X_toto_soukan_id"]
    resp_dict["X_torikeshi_riyu_kbn"] = req["X_torikeshi_riyu_kbn"]
    resp_dict["X_outou_kekka"] = "00"
    resp_dict["X_toto_kekka"] = ""
    resp_dict["X_ticket_cnt"] = ""
    return resp_dict


def output_xml(resp_dict:dict) -> str:
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
		<X_ticket_cnt>{resp_dict["X_ticket_cnt"]}</X_ticket_cnt>
	</body>
</sejmsg>"""
