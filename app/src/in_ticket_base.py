from ticket_library import split_bits
from in_ticket_library import calculate_CD
from in_ticket_base_register import get_in_ticket_base_register
from in_ticket_base_cancel import get_in_ticket_base_cancel
from in_ticket_base_complete import get_in_ticket_base_complete

def get_in_base_field(req:dict, mapping_str:str) -> tuple[int,dict,dict,list]:
    mapping = split_bits(mapping_str, [
        1, # reserved
        3, # mapping[1]処理結果
        4, # mapping[2]応答結果
        4, # mapping[3]ショップID
        2, # mapping[4]応答結果区分
        2, # mapping[5]チケット代金/発券代金/チケット購入代金/印紙基準額
        1, # mapping[6]本件購入枚数/チケット枚数
        1, # mapping[7]レスポンスパターン（再送区分用）
        3, # mapping[8]取消処理結果
        3, # mapping[9]取消応答結果
        1, # mapping[10]レスポンスパターン（取消再送区分用）
        3, # mapping[11]処理結果（完了通知）
        2, # mapping[12]応答結果（完了通知）
        2, # mapping[13]成功までの失敗回数（未使用）
        1, # NoCare
    ]) # 33bit（内、3bitが未使用、29bitがオプション、1bitがマップ番号）
    httpstatus:int
    common_dict:dict
    success_dict = {}
    ticket_list = []

    # 要求区分が01の場合⇒レスポンス解析  発券
    if req["X_yokyu_kbn"] == "01":
        (httpstatus, common_dict, success_dict, ticket_list) = get_in_ticket_base_register(req, mapping)
    # 要求区分が21の場合⇒レスポンス解析　取消
    elif req["X_yokyu_kbn"] == "21":
        (httpstatus, common_dict, success_dict) = get_in_ticket_base_cancel(req, mapping)
    # 要求区分が02または12の場合⇒レスポンス解析
    elif (req["X_yokyu_kbn"] == "02" or
          req["X_yokyu_kbn"] == "12"):
        (httpstatus, common_dict) = get_in_ticket_base_complete(req, mapping)
    else:
        raise ValueError(f"要求区分が不正です。{req["X_yokyu_kbn"]}")
    
    return (httpstatus, common_dict, success_dict, ticket_list)





