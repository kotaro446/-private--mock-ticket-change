from logger import get_logger
logger = get_logger()
from ticket_library import (
    split_bits,
)
from in_ticket_kenmen_register import get_in_ticket_kenmen_register
from in_ticket_kenmen_cancel import get_in_ticket_kenmen_cancel
from in_ticket_kenmen_complete import get_in_ticket_kenmen_complete

def get_in_kenmen_field(req:dict, mapping_str:str) -> tuple[int,dict,dict,list]:
    common_dict:dict
    httpstatus:int
    success_dict = {}
    ticket_list = []
    mapping = split_bits(mapping_str, [
        8, # reserved
        4, # mapping[1] ショップID
        2, # mapping[2] 応答結果区分
        2, # mapping[3] チケット代金
        2, # mapping[4] 発券代金
        2, # mapping[5] チケット購入代金
        2, # mapping[6] 印紙基準額
        5, # mapping[7] チケット枚数
        5, # mapping[8] 券面情報データ
        1, # NoCare
    ]) # 33bit (内、9bitが未使用、23bitがオプション、1bitがマップ番号)

    # 要求区分が01の場合⇒レスポンス解析
    if (req["X_yokyu_kbn"] == "01"):
        (httpstatus,
         common_dict,
         success_dict,
         ticket_list) = get_in_ticket_kenmen_register(req, mapping)

    elif (req["X_yokyu_kbn"] == "21"):
        (httpstatus,
         common_dict,
         success_dict) = get_in_ticket_kenmen_cancel(req, mapping)

    # 要求区分が02または12の場合⇒レスポンス解析
    elif (req["X_yokyu_kbn"] == "02" or
          req["X_yokyu_kbn"] == "12"):
        (common_dict, httpstatus) = get_in_ticket_kenmen_complete(req)

    else:
        raise ValueError(f"要求区分が不正です。{req["X_yokyu_kbn"]}")

    return (httpstatus, common_dict, success_dict, ticket_list)


