from test_request_response_dict_ecticket import *
from test_request_response_dict_in_ticket import *
from test_request_response_dict_toto_ticket import *
from flask import Flask
from logger import get_logger

app = Flask(__name__)
logger = get_logger()
logger.setup_logger(app)

def test_res_ecticket():
    reqres_dict = get_reqres_ecticket()
    """
    Mcotyチケット マッピングNo1 問合せ 通常/取消
    """
    mock_ticket_ms_main(reqres_dict, EC_TICKET) 

def test_res_ecticket_kanryo():
    """
    Mcotyチケット マッピングNo1 完了通知
    """
    reqres_dict = get_reqres_ecticket_kanryo()
    mock_ticket_ms_main(reqres_dict, EC_TICKET) 

def test_res_ecticket_repay():
    """
    Mcotyチケット マッピングNo2 払戻/払戻取消
    """
    reqres_dict = get_reqres_ecticket_repay()
    mock_ticket_ms_main(reqres_dict, EC_TICKET) 

def test_res_ecticket_map3():
    reqres_dict = get_reqres_ecticket_map3()
    """
    Mcotyチケット マッピングNo3 問合せ 通常/取消
    """
    mock_ticket_ms_main(reqres_dict, EC_TICKET) 

def test_res_ecticket_kanryo_map3():
    """
    Mcotyチケット マッピングNo3 完了通知
    """
    reqres_dict = get_reqres_ecticket_kanryo_map3()
    mock_ticket_ms_main(reqres_dict, EC_TICKET) 

def test_res_ecticket_map4():
    reqres_dict = get_reqres_ecticket_map4()
    """
    Mcotyチケット マッピングNo4 問合せ 通常/取消
    """
    mock_ticket_ms_main(reqres_dict, EC_TICKET) 

def test_res_ecticket_kanryo_map4():
    """
    Mcotyチケット マッピングNo4 完了通知
    """
    reqres_dict = get_reqres_ecticket_kanryo_map4()
    mock_ticket_ms_main(reqres_dict, EC_TICKET) 

def test_res_ecticket_error():
    """
    Mcotyチケット 異常系
    """
    reqres_dict = get_reqres_ecticket_error()
    mock_ticket_ms_main(reqres_dict, EC_TICKET) 

def test_res_in_ticket():
    """
    インターネットチケット マッピングNo1 入金発券問合せ 通常/取消
    """
    reqres_dict = get_reqres_in_ticket()
    mock_ticket_ms_main(reqres_dict, IN_TICKET) 

def test_res_in_ticket_kanryo():
    """
    インターネットチケット マッピングNo1 完了通知
    """
    reqres_dict = get_reqres_in_ticket_kanryo()
    mock_ticket_ms_main(reqres_dict, IN_TICKET) 

def test_res_in_ticket_detail():
    """
    インターネットチケット マッピングNo2 入金発券問合せ 通常/取消
    """
    reqres_dict = get_reqres_in_ticket_detail()
    mock_ticket_ms_main(reqres_dict, IN_TICKET) 

def test_res_in_ticket_detail_kanryo():
    """
    インターネットチケット マッピングNo2 完了通知
    """
    reqres_dict = get_reqres_in_ticket_detail_kanryo()
    mock_ticket_ms_main(reqres_dict, IN_TICKET) 

def test_res_in_ticket_error():
    """
    インターネットチケット 異常系
    """
    reqres_dict = get_reqres_in_ticket_error()
    mock_ticket_ms_main(reqres_dict, IN_TICKET) 

def test_res_toto_ticket():
    """
    スポーツ振興くじ マッピングNo1 購入要求/購入取消要求
    """
    reqres_dict = get_reqres_toto_ticket()
    mock_ticket_ms_main(reqres_dict, TOTO_TICKET) 

def test_res_toto_ticket_vote():
    """
    スポーツ振興くじ マッピングNo2 本投票要求/本投票取消要求
    """
    reqres_dict = get_reqres_toto_ticket_vote()
    mock_ticket_ms_main(reqres_dict, TOTO_TICKET) 

def test_res_toto_ticket_repay():
    """
    スポーツ振興くじ マッピングNo3 払戻要求/払戻取消要求
    """
    reqres_dict = get_reqres_toto_ticket_repay()
    mock_ticket_ms_main(reqres_dict, TOTO_TICKET) 

def test_res_toto_ticket_clearing():
    """
    スポーツ振興くじ マッピングNo4 当せん返還消込
    """
    reqres_dict = get_reqres_toto_ticket_clearing()
    mock_ticket_ms_main(reqres_dict, TOTO_TICKET) 

def test_res_toto_ticket_error():
    """
    スポーツ振興くじ 異常系
    """
    reqres_dict = get_reqres_toto_ticket_error()
    mock_ticket_ms_main(reqres_dict, TOTO_TICKET) 

