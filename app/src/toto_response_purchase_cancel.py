import toto_constant
from flask import request, Response
from toto_request_mapping_purchase import *
from toto_request_mapping_vote import *
from toto_library import *

######################################################################
# メイン関数                                                          #
######################################################################

def resp_purchase_cancel(req:dict, segments:list, mapping_num:int) -> Response:
    """
    TOTO購入要求取消のレスポンスを返す。

    Args:
        req (dict): リクエストデータ
        segments (list[int]): マッピング番号ごとに分割した数字リスト
        mapping_num (int): マッピング番号

    Returns:
        Response: レスポンス
    """
    # 必須項目チェック
    if validate_request_fields(req, toto_constant.VALIDATE_REQUEST_FIELDS_CANCEL):
        return generate_error_response()

    # デフォルトレスポンス
    resp_dict = create_default_resp_dict(req)

    # No.2_本投票・本投票障害取消応答_マッピングの場合
    if mapping_num == 1:
        return resp_purchase_cancel_map_vote(req, segments, resp_dict)
    
    # No.1_購入・購入取消応答_マッピングの場合
    return resp_purchase_cancel_map_purchase(req, segments, resp_dict)


######################################################################
# No.1_購入・購入取消応答_マッピング　の関数                            #
######################################################################

def resp_purchase_cancel_map_purchase(req:dict, segments:list, resp_dict:dict) -> Response:
    """
    No.1_購入・購入取消応答_マッピングの場合
    TOTO購入取消要求のレスポンスを返す。

    Args:
        req (dict): リクエストデータ
        segments (list[int]): マッピング番号ごとに分割した数字リスト
        resp_dict (dict): レスポンスデータ

    Returns:
        Response: レスポンス
    """
    # 再送区分の判定
    if req["X_saiso_kbn"] == "1":
        if get_X_saiso_kbn_status_for_purchase_cancel_map_purchase(segments[8]) == "0":
            return resp_purchase_cancel_map_purchase_case_resend(req, segments, resp_dict)

    # 処理結果の判定
    X_shori_kekka, httpstatus = get_X_shori_kekka_for_purchase_cancel_map_purchase(segments[5])
    if X_shori_kekka != "00":
        return generate_error_response(X_shori_kekka, httpstatus)
    
    # 正常レスポンス
    return resp_purchase_cancel_map_purchase_case_success(req, segments, resp_dict)


def resp_purchase_cancel_map_purchase_case_resend(req:dict, segments:list, resp_dict:dict) -> Response:
    """
    No.1_購入・購入取消応答_マッピング
    再送の場合のTOTO購入取消要求のレスポンスを返す。

    Args:
        req (dict): リクエストデータ
        segments (list[int]): マッピング番号ごとに分割した数字リスト
        resp_dict (dict): レスポンスデータ

    Returns:
        Response: レスポンス
    """
    resp_dict["X_shop_id"] = get_X_shop_id_for_purchase_cancel_map_purchase(segments[9])
    resp_dict["X_haraikomi"] = req["X_barcode"]
    resp_dict["X_tc_dai"] = get_X_tc_dai_for_purchase_cancel_map_purchase(segments[7])
    resp_dict["X_ticket_cnt"] = str(get_X_ticket_cnt_for_purchase_map_purchase(segments[3])).zfill(2)
    resp_xml = output_xml(resp_dict)
    return Response(resp_xml.encode(encoding='cp932'), status=200, content_type='text/xml; charset=Windows-31J')


def resp_purchase_cancel_map_purchase_case_success(req:dict, segments:list, resp_dict:dict) -> Response:
    """
    No.1_購入・購入取消応答_マッピング
    正常の場合のTOTO購入要求のレスポンスを返す。

    Args:
        req (dict): リクエストデータ
        segments (list[int]): マッピング番号ごとに分割した数字リスト
        resp_dict (dict): レスポンスデータ

    Returns:
        Response: レスポンス
    """
    # 応答結果を取得する
    resp_dict["X_outou_kekka"] = get_X_outou_kekka_for_purchase_cancel_map_purchase(segments[6])

    # 応答結果が "00" の場合、セットする
    if resp_dict["X_outou_kekka"] == "00":
        resp_dict["X_shop_id"] = get_X_shop_id_for_purchase_cancel_map_purchase(segments[9])
        resp_dict["X_haraikomi"] = req["X_barcode"]
        resp_dict["X_tc_dai"] = get_X_tc_dai_for_purchase_cancel_map_purchase(segments[7])
        resp_dict["X_ticket_cnt"] = str(get_X_ticket_cnt_for_purchase_map_purchase(segments[3])).zfill(2)

    resp_xml = output_xml(resp_dict)
    return Response(resp_xml.encode(encoding='cp932'), status=200, content_type='text/xml; charset=Windows-31J')


######################################################################
# No.2_本投票・本投票障害取消応答_マッピング　の関数                     #
######################################################################

def resp_purchase_cancel_map_vote(req:dict, segments:list, resp_dict:dict) -> Response:
    """
    No.2_本投票・本投票障害取消応答_マッピング
    TOTO購入取消要求のレスポンスを返す。

    Args:
        req (dict): リクエストデータ
        segments (list[int]): マッピング番号ごとに分割した数字リスト
        resp_dict (dict): レスポンスデータ

    Returns:
        Response: レスポンス
    """
    # 処理結果の判定
    X_shori_kekka, httpstatus = get_X_shori_kekka_for_purchase_cancel_map_vote(segments[2])
    if X_shori_kekka != "00":
        return generate_error_response(X_shori_kekka, httpstatus)

    # 正常レスポンス
    return resp_purchase_cancel_map_vote_case_success(req, segments, resp_dict)


def resp_purchase_cancel_map_vote_case_success(req:dict, segments:list, resp_dict:dict) -> Response:
    """
    No.2_本投票・本投票障害取消応答_マッピング
    正常の場合のTOTO購入要求のレスポンスを返す。

    Args:
        req (dict): リクエストデータ
        segments (list[int]): マッピング番号ごとに分割した数字リスト
        resp_dict (dict): レスポンスデータ

    Returns:
        Response: レスポンス
    """
    # 応答結果を取得する
    resp_dict["X_outou_kekka"] = get_X_outou_kekka_for_purchase_cancel_map_vote(segments[3])

    # 応答結果が "00" の場合、セットする
    if resp_dict["X_outou_kekka"] == "00":
        resp_dict["X_shop_id"] = "30801"
        resp_dict["X_haraikomi"] = req["X_barcode"]
        resp_dict["X_tc_dai"] = get_X_tc_dai_for_purchase_map_vote(segments[0])
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
    resp_dict["X_saiso_kbn"] = req["X_saiso_kbn"]
    resp_dict["X_yokyu_kbn"] = req["X_yokyu_kbn"]
    resp_dict["X_barcode"] = req["X_barcode"]
    resp_dict["X_shop_id"] = ""
    resp_dict["X_torikeshi_riyu"] = req["X_torikeshi_riyu"]
    resp_dict["X_outou_kekka"] = "00"
    resp_dict["X_haraikomi"] = ""
    resp_dict["X_tc_dai"] = ""
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
		<X_saiso_kbn>{resp_dict["X_saiso_kbn"]}</X_saiso_kbn>
		<X_yokyu_kbn>{resp_dict["X_yokyu_kbn"]}</X_yokyu_kbn>
		<X_barcode>{resp_dict["X_barcode"]}</X_barcode>
		<X_shop_id>{resp_dict["X_shop_id"]}</X_shop_id>
		<X_torikeshi_riyu>{resp_dict["X_torikeshi_riyu"]}</X_torikeshi_riyu>
		<X_outou_kekka>{resp_dict["X_outou_kekka"]}</X_outou_kekka>
		<X_haraikomi>{resp_dict["X_haraikomi"]}</X_haraikomi>
		<X_tc_dai>{resp_dict["X_tc_dai"]}</X_tc_dai>
		<X_ticket_cnt>{resp_dict["X_ticket_cnt"]}</X_ticket_cnt>
	</body>
</sejmsg>"""
