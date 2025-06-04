import toto_constant
from flask import request, Response
from toto_request_mapping_refund import *
from toto_request_mapping_clearing import *
from toto_library import *

######################################################################
# メイン関数                                                          #
######################################################################

def resp_refund(req:dict, segments:list, mapping_num:int) -> Response:
    """
    TOTO払戻要求のレスポンスを返す。

    Args:
        req (dict): リクエストデータ
        segments (list[int]): マッピング番号ごとに分割した数字リスト
        mapping_num (int): マッピング番号

    Returns:
        Response: レスポンス
    """
    # 必須項目チェック
    if validate_request_fields(req, toto_constant.VALIDATE_REQUEST_FIELDS_REFUND):
        return generate_error_response()

    # デフォルトレスポンス
    resp_dict = create_default_resp_dict(req)

    # No.4_当せん返還消込応答_マッピングの場合
    if mapping_num == 3:
        return resp_refund_map_clearing(req, segments, resp_dict)

    # No.3_払戻・払戻取消応答_マッピング
    return resp_refund_map_refund(req, segments, resp_dict)


######################################################################
# No.3_払戻・払戻取消応答_マッピング　の関数                            #
######################################################################

def resp_refund_map_refund(req:dict, segments:list, resp_dict:dict) -> Response:
    """
    No.3_払戻・払戻取消応答_マッピング
    TOTO払戻要求のレスポンスを返す。

    Args:
        req (dict): リクエストデータ
        segments (list[int]): マッピング番号ごとに分割した数字リスト
        resp_dict (dict): レスポンスデータ

    Returns:
        Response: レスポンス
    """
    # 再送区分の判定
    if req["X_saiso_kbn"] == "1":
        if get_X_saiso_kbn_for_refund_map_refund(segments[3]) == "0":
            return resp_refund_map_refund_case_resend(req, segments, resp_dict)

    # 処理結果の判定
    X_shori_kekka, httpstatus = get_X_shori_kekka_for_refund_map_refund(segments[0])
    if X_shori_kekka != "00":
        return generate_error_response(X_shori_kekka, httpstatus)

    return resp_refund_map_refund_case_success(req, segments, resp_dict)


def resp_refund_map_refund_case_success(req:dict, segments:list, resp_dict:dict) -> Response:
    """
    No.3_払戻・払戻取消応答_マッピング
    正常の場合のTOTO払戻要求のレスポンスを返す。

    Args:
        req (dict): リクエストデータ
        segments (list[int]): マッピング番号ごとに分割した数字リスト
        resp_dict (dict): レスポンスデータ

    Returns:
        Response: レスポンス
    """
    resp_dict["X_outou_kekka"] = get_X_outou_kekka_for_refund_map_refund(segments[1])

    # 応答結果が "00" の場合、設定する
    if resp_dict["X_outou_kekka"] == "00":
        resp_dict["X_shop_id"] = get_X_shop_id_for_refund_cancel_map_refund(segments[8])
        resp_dict["X_haraimodoshi"] = req["X_barcode"]
        resp_dict["X_payback_amt"] = get_X_payback_amt_for_refund_map_refund(segments[2])

    resp_xml = output_xml(resp_dict)
    return Response(resp_xml.encode(encoding='cp932'), status=200, content_type='text/xml; charset=Windows-31J')


def resp_refund_map_refund_case_resend(req:dict, segments:list, resp_dict:dict) -> Response:
    """
    No.3_払戻・払戻取消応答_マッピング
    再送の場合のTOTO払戻要求のレスポンスを返す。

    Args:
        req (dict): リクエストデータ
        segments (list[int]): マッピング番号ごとに分割した数字リスト
        resp_dict (dict): レスポンスデータ

    Returns:
        Response: レスポンス
    """
    resp_dict["X_shop_id"] = get_X_shop_id_for_refund_cancel_map_refund(segments[8])
    resp_dict["X_haraimodoshi"] = req["X_barcode"]
    resp_dict["X_payback_amt"] = get_X_payback_amt_for_refund_map_refund(segments[2])
    resp_xml = output_xml(resp_dict)
    return Response(resp_xml.encode(encoding='cp932'), status=200, content_type='text/xml; charset=Windows-31J')


######################################################################
# No.4_当せん返還消込応答_マッピング　の関数                            #
######################################################################

def resp_refund_map_clearing(req:dict, segments:list, resp_dict:dict) -> Response:
    """
    No.4_当せん返還消込応答_マッピング
    TOTO払戻要求のレスポンスを返す。

    Args:
        req (dict): リクエストデータ
        segments (list[int]): マッピング番号ごとに分割した数字リスト
        resp_dict (dict): レスポンスデータ

    Returns:
        Response: レスポンス
    """
    resp_dict["X_shop_id"] = "30801"
    resp_dict["X_haraimodoshi"] = req["X_barcode"]
    resp_dict["X_payback_amt"] = get_X_payback_amt_for_refund_map_clearing(segments[0])
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
    resp_dict["X_saiso_kbn"] = req["X_saiso_kbn"]
    resp_dict["X_yokyu_kbn"] = req["X_yokyu_kbn"]
    resp_dict["X_barcode"] = req["X_barcode"]
    resp_dict["X_vote_ticket_barcode"] = req["X_vote_ticket_barcode"]#
    resp_dict["X_shop_id"] = ""
    resp_dict["X_torikeshi_riyu"] = ""
    resp_dict["X_outou_kekka"] = "00"
    resp_dict["X_haraimodoshi"] = ""
    resp_dict["X_payback_amt"] = ""
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
		<X_saiso_kbn>{resp_dict["X_saiso_kbn"]}</X_saiso_kbn>
		<X_yokyu_kbn>{resp_dict["X_yokyu_kbn"]}</X_yokyu_kbn>
		<X_barcode>{resp_dict["X_barcode"]}</X_barcode>
		<X_vote_ticket_barcode>{resp_dict["X_vote_ticket_barcode"]}</X_vote_ticket_barcode>
		<X_shop_id>{resp_dict["X_shop_id"]}</X_shop_id>
		<X_torikeshi_riyu>{resp_dict["X_torikeshi_riyu"]}</X_torikeshi_riyu>
		<X_outou_kekka>{resp_dict["X_outou_kekka"]}</X_outou_kekka>
		<X_haraimodoshi>{resp_dict["X_haraimodoshi"]}</X_haraimodoshi>
		<X_payback_amt>{resp_dict["X_payback_amt"]}</X_payback_amt>
	</body>
</sejmsg>"""
