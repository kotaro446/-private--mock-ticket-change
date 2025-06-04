
from flask import Response
from logger import get_logger
logger = get_logger()

from ec_ticket_library import (
    get_interface_info_dictionary,
    get_order_info_dictionary,
    get_payback_info_dictionary,
    ec_ticket_validate_check,
    get_test_option,
)
from ec_ticket_nomal import (
    get_ec_nomal_field,
)
from ec_ticket_refund import (
    get_ec_refund_field,
)
from ec_ticket_complete import (
    get_ec_complete_field,
)
from ec_ticket_kenmen import (
    get_ec_kenmen_field,
)

from ec_ticket_xmldef import ec_ticket_output_xml

# NRIセンターEC関連問合わせモックサーバ
def mock_ecticket_ms_main(request_data:dict)  ->  Response:
    #================================#
    # リクエストパラメタのチェック処理  #
    #================================#
    interface_info:dict = {}
    order_info:dict = {}
    ticket_info:dict = {}
    payback_info:dict = {}
    httpstatus:int = 400

    try:
        check_result = ec_ticket_validate_check(request_data)
        
        if check_result != "00":
            interface_info["syori_kekka"] = check_result
            ValueError(f"処理結果が正常ではありません。")
        else:
            #==================#
            # チケット情報を作成 #
            #==================#
            (interface_info,
            order_info,  
            ticket_info,
            payback_info,
            httpstatus) = make_ticket_info(request_data)
    except ValueError as e:
        logger.debug(f"ValueError: {e}")
        if interface_info == {}:
            interface_info["syori_kekka"] = "99"

    #==========================#
    # レスポンスXMLを生成して返却#
    #==========================#
    xml_response = ec_ticket_output_xml(request_data, interface_info, order_info, ticket_info, payback_info)
    logger.debug(f"レスポンスデータ: {xml_response}")
    return Response(xml_response.encode(encoding='cp932'), status=httpstatus, content_type='text/xml; charset=Windows-31J')
  
def make_ticket_info(request_data:dict) -> tuple[dict, dict, dict, dict, int]:
    """
    チケット情報を作成

    Parameters
    ----------
    request_data:dict

    Returns
    -------
    interface_info:dict  
    order_info:dict  
    res_ticket_info:dict  
    payback_info:dict  
    httpstatus:int
    """

    #=====================================#
    # リクエストからベースレスポンス辞書作成 #
    #=====================================#
    interface_info = get_interface_info_dictionary(request_data)
    order_info = get_order_info_dictionary(request_data)
    payback_info = get_payback_info_dictionary(request_data)

    #===============================#
    # リクエストからオプション取得     #
    #===============================#
    mapping_str:str
    mapping_no:int
    (mapping_no, mapping_str) = get_test_option(request_data)
    
    #=====================================#
    # オプションから更新レスポンス辞書作成   #
    #=====================================#
    httpstatus:int
    res_interface_info:dict = {}
    res_order_info:dict = {}
    res_ticket_info:dict = {}
    res_payback_info:dict = {}
    # No.1_EC関連問合せ応答_マッピング
    if mapping_no == 0:
        # マッピングで指定する応答値の作成
        (res_interface_info,
         res_order_info,
         res_ticket_info,
         httpstatus) = get_ec_nomal_field(request_data, mapping_str)

    # No.2_EC関連払戻し応答_マッピング    
    elif mapping_no == 1:
        # マッピングで指定する応答値の作成
        (res_interface_info,
         res_payback_info,
         httpstatus) = get_ec_refund_field(request_data, mapping_str)

    # No.3_EC関連完了応答_マッピング          
    elif mapping_no == 2:
        (res_interface_info,
         res_order_info,
         res_ticket_info,
         httpstatus) = get_ec_complete_field(request_data, mapping_str)
    # No.4_EC関連問合せ応答(券面情報)_マッピング
    elif mapping_no == 3:
        (res_interface_info,
         res_order_info,
         res_ticket_info,
         httpstatus) = get_ec_kenmen_field(request_data, mapping_str)
    else:
        raise ValueError(f"マッピング番号が不正です。")

    #=====================#
    # 辞書の更新           #
    #=====================#
    interface_info.update(res_interface_info)
    order_info.update(res_order_info)
    payback_info.update(res_payback_info)

    return (interface_info, order_info, res_ticket_info, payback_info, httpstatus)
