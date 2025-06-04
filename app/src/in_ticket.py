from flask import Response

from in_ticket_library import (
    in_ticket_validate_check,
    get_mapping,
)
from in_ticket_base import (
    get_in_base_field,
)
from in_ticket_kenmen import (
    get_in_kenmen_field,
)
from in_ticket_xmldef import in_ticket_output_xml
from logger import get_logger
logger = get_logger()


#　インターネットチケット モックサーバ - 入金/発券問合せ, 入金/発券完了通知
def mock_inticket_ms_main(req:dict)  ->  Response:
    #================================#
    # リクエストパラメタのチェック処理  #
    #================================#
    common_dict:dict = {}
    success_dict:dict = {}
    ticket_list:list = []
    httpstatus:int = 400

    check_result = in_ticket_validate_check(req)
    if check_result == "00":
        (mapping_no, mapping_str) = get_mapping(req)

        # mapping_noが0の場合⇒No.1_INチケット問合せ応答_マッピング
        if mapping_no == 0:
            # 辞書を作成
            (httpstatus,
             common_dict,
             success_dict,
             ticket_list) = get_in_base_field(req, mapping_str)

        # mapping_noが1の場合⇒No.2_INチケット問合せ応答_マッピング          
        elif mapping_no == 1:
            (httpstatus,
             common_dict,
             success_dict,
             ticket_list) = get_in_kenmen_field(req, mapping_str)
        
        else:
            raise ValueError(f"mapping_noが不正です。{mapping_no}")
    else:
        common_dict["X_shori_kekka"] = check_result

    xml_response = in_ticket_output_xml(req, common_dict, success_dict, ticket_list)


    return Response(xml_response.encode(encoding='Windows-31J'),
                    status=httpstatus,
                    content_type='text/xml; charset=Windows-31J')



