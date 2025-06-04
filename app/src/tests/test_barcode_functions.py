from ec_ticket import mock_ecticket_ms_main
from in_ticket import mock_inticket_ms_main
from toto_ticket import mock_toto_register_ms_main

import xml.etree.ElementTree as ET
from flask import Flask, Response
from logger import get_logger

app = Flask(__name__)
logger = get_logger()
logger.setup_logger(app)

# ---------------------------
# 固定値
# ---------------------------
EC_TICKET = '00'
IN_TICKET = '01'
TOTO_TICKET = '02'

# Mcopyチケット ﾃﾝﾌﾟﾚｰﾄHTMLﾌｧｲﾙ名
EC_HTML_NAME_NORMAL = 'ETPI001102'
"""
Mcopyチケット マッピングNo1 ぴあ以外のﾃﾝﾌﾟﾚｰﾄHTMLﾌｧｲﾙ名
"""

EC_HTML_NAME_PIA = 'NTPM000001'
"""
Mcopyチケット マッピングNo1 ぴあのﾃﾝﾌﾟﾚｰﾄHTMLﾌｧｲﾙ名
"""

EC_HTML_NAME_A = 'ETPM000001'
"""
Mcopyチケット マッピングNo4 券面情報"A"に該当するﾃﾝﾌﾟﾚｰﾄHTMLﾌｧｲﾙ名
"""

EC_HTML_NAME_BC = 'ETDJUP0001'
"""
Mcopyチケット マッピングNo4 券面情報"B","C"に該当するﾃﾝﾌﾟﾚｰﾄHTMLﾌｧｲﾙ名
"""

EC_HTML_NAME_D = 'ETJW01001T'
"""
Mcopyチケット マッピングNo4 券面情報"D"に該当するﾃﾝﾌﾟﾚｰﾄHTMLﾌｧｲﾙ名
"""

EC_HTML_NAME_E = 'ETJW01002T'
"""
Mcopyチケット マッピングNo4 券面情報"E"に該当するﾃﾝﾌﾟﾚｰﾄHTMLﾌｧｲﾙ名
"""

EC_HTML_NAME_F = 'ETJD03020T'
"""
Mcopyチケット マッピングNo4 券面情報"F"に該当するﾃﾝﾌﾟﾚｰﾄHTMLﾌｧｲﾙ名
"""

EC_HTML_NAME_G = 'ETPI001102'
"""
Mcopyチケット マッピングNo4 券面情報"G"に該当するﾃﾝﾌﾟﾚｰﾄHTMLﾌｧｲﾙ名
"""

EC_HTML_NAME_H = 'TTOT000017'
"""
Mcopyチケット マッピングNo4 券面情報"H"に該当するﾃﾝﾌﾟﾚｰﾄHTMLﾌｧｲﾙ名
"""

EC_HTML_NAME_I = 'TTOT000178'
"""
Mcopyチケット マッピングNo4 券面情報"I"に該当するﾃﾝﾌﾟﾚｰﾄHTMLﾌｧｲﾙ名
"""


# Mcopyチケット チケットデータ
EC_TICKET_DATA_NORMAL = 'NTPI001102'
"""
Mcopyチケット マッピングNo1,3 ぴあ以外のチケットデータ
"""

EC_TICKET_DATA_PIA = 'NTPM000001'
"""
Mcopyチケット マッピングNo1,3 ぴあのチケットデータ
"""

EC_TICKET_DATA_A = 'NTPM000001_Normal'
"""
Mcopyチケット マッピングNo4 券面情報"A"に該当するチケットデータ
"""

EC_TICKET_DATA_B = 'TTDJUP0001_Normal'
"""
Mcopyチケット マッピングNo4 券面情報"B"に該当するチケットデータ
"""

EC_TICKET_DATA_C = 'TTDJUP0001_Max'
"""
Mcopyチケット マッピングNo4 券面情報"C"に該当するチケットデータ
"""

EC_TICKET_DATA_D = 'NTJW01001T_Normal'
"""
Mcopyチケット マッピングNo4 券面情報"D"に該当するチケットデータ
"""

EC_TICKET_DATA_E = 'NTJW01002T'
"""
Mcopyチケット マッピングNo4 券面情報"E"に該当するチケットデータ
"""

EC_TICKET_DATA_F = 'NTJD03020T_Normal'
"""
Mcopyチケット マッピングNo4 券面情報"F"に該当するチケットデータ
"""

EC_TICKET_DATA_G = 'NTPI001102'
"""
Mcopyチケット マッピングNo4 券面情報"G"に該当するチケットデータ
"""

EC_TICKET_DATA_H = 'TI03190100'
"""
Mcopyチケット マッピングNo4 券面情報"H"に該当するチケットデータ
"""

EC_TICKET_DATA_I = 'TI03190101'
"""
Mcopyチケット マッピングNo4 券面情報"I"に該当するチケットデータ
"""

# INチケット チケット区分
BARCODE_MAIN_TICKET = '1'
NO_BARCODE_MAIN_TICKET = '2'
BARCODE_OTHER_TICKET = '3'
NO_BARCODE_OTHER_TICKET = '4'

# INチケット HTMLテンプレートコード
TEMP_CODE_NORMAL = 'ETSNHN0001'
"""
インターネットチケット マッピングNo1 ぴあ以外の場合
"""

TEMP_CODE_PIA = 'NTPA000001'
"""
インターネットチケット マッピングNo1 ぴあの場合  
インターネットチケット マッピングNo2 下記券面情報データに該当するテンプレートコード
---
C
"""

TEMP_CODE_SHOP_30400_NO_BARCODE_MAIN = 'ETSNHN0003'
"""
インターネットチケット マッピングNo2 下記券面情報データに該当するテンプレートコード
---
A
"""

TEMP_CODE_SHOP_30400_BARCODE_MAIN = 'ETSNHQ0001'
"""
インターネットチケット マッピングNo2 下記券面情報データに該当するテンプレートコード
---
B
"""

TEMP_CODE_SHOP_30400_NO_BARCODE_OTHER = 'ETSNFN0001'
"""
インターネットチケット マッピングNo2 下記券面情報データに該当するテンプレートコード
---
D
"""

TEMP_CODE_SHOP_30501 = 'ETCN000006'
"""
インターネットチケット マッピングNo2 下記券面情報データに該当するテンプレートコード
---
E, F
"""

TEMP_CODE_SHOP_30514_CASE_2 = 'TTPA000001'
"""
インターネットチケット マッピングNo2 下記券面情報データに該当するテンプレートコード
---
G, H01～02, J01～02, K01～04, L01～20, M01～20, N01～20
"""

TEMP_CODE_SHOP_30500 = 'TTEP101355'
"""
インターネットチケット マッピングNo2 記券面情報データに該当するテンプレートコード
---
AP01～20, R01～20, S01～20
"""

TEMP_CODE_SHOP_30701 = 'NTST000010'
"""
インターネットチケット マッピングNo2 下記券面情報データに該当するテンプレートコード
---
T, U
"""

TEMP_CODE_SHOP_30705 = 'NTSW000010'
"""
インターネットチケット マッピングNo2 下記券面情報データに該当するテンプレートコード
---
V, W
"""

TEMP_CODE_TOTO_BIG_NORMAL = 'TTNA000001'
"""
スポーツ振興くじ マッピングNo2 totoBIG一般用テンプレート
"""

TEMP_CODE_TOTO_GOAL = 'TTNA000002'
"""
スポーツ振興くじ マッピングNo2 totoGOAL用テンプレート
"""

TEMP_CODE_TOTO_MEGA_BIG = 'TTNA000003'
"""
スポーツ振興くじ マッピングNo2 MEGABIG用テンプレート
"""

# ---------------------------
# 期待値データクラス
# ---------------------------
class ResponseEcTicketData:
    """
    EC関連問合せ レスポンス期待値データ マッピングNo1, 3, 4
    """
    def __init__(self, 
                 shori_kekka: str = '00', 
                 oto_kekka: str = '00', 
                 pay_type: str = '1', 
                 dlv_type: str = '1', 
                 keijyo_type: str = ' ', 
                 inshi_kijun: str = '      ', 
                 kingaku_henko_flg: str = '1', 
                 kino_kbn: str = '3', 
                 shop_id: str = '00000', 
                 shuno_kingaku: str = '      ', 
                 ticket_count:int = 0,
                 tc_info_data:str = ' ',
                 is_cancel:bool = False,
                 ):
        self.shori_kekka: str = shori_kekka              # 処理結果
        self.oto_kekka: str = oto_kekka                  # 応答結果
        self.pay_type: str = pay_type                    # 支払種別
        self.dlv_type: str = dlv_type                    # 納品種別
        self.keijyo_type: str = keijyo_type              # 売上計上区分
        self.inshi_kijun: str = inshi_kijun              # 印紙基準額
        self.kingaku_henko_flg: str = kingaku_henko_flg  # 価格変更フラグ
        self.kino_kbn: str = kino_kbn                    # 機能区分
        self.shop_id: str = shop_id                      # SHOP-CD
        self.shuno_kingaku: str = shuno_kingaku          # 収納金額
        self.ticket_count: int = ticket_count            # チケット発券個別情報
        self.is_pia: bool = shop_id == '30731'           # ぴあか否か
        self.is_cancel: bool = is_cancel                 # 取消か否か
        self.tc_info_data:str = tc_info_data             # 券面情報 ※No4のみ使用


class ResponseEcTicketRepayData:
    """
    EC関連払戻 レスポンス期待値データ マッピングNo2
    """
    def __init__(self, 
                 shori_kekka: str = '00', 
                 oto_kekka: str = '00', 
                 payback_kingaku: str = '      ', 
                 payback_start_ymd: str = '        ', 
                 payback_end_ymd: str = '        ', 
                 svc_time_start_hm: str = '    ', 
                 svc_time_end_hm: str = '    ', 
                 hanken_yohi: str = '0', 
                 payback_tesuryo: str = '000000', 
                 ):
        self.shori_kekka: str = shori_kekka              # 処理結果
        self.oto_kekka: str = oto_kekka                  # 応答結果
        self.payback_kingaku: str = payback_kingaku      # 払戻金額
        self.payback_start_ymd: str = payback_start_ymd  # 開始日
        self.payback_end_ymd: str = payback_end_ymd      # 終了日
        self.svc_time_start_hm: str = svc_time_start_hm  # 開始時刻
        self.svc_time_end_hm: str = svc_time_end_hm      # 終了時刻
        self.hanken_yohi: str = hanken_yohi              # 半券確認要否
        self.payback_tesuryo: str = payback_tesuryo      # チケット手数料払戻金額

class ResponseEcTicketKanryoData:
    """
    EC関連完了 レスポンス期待値データ マッピングNo1, 3, 4 
    """
    def __init__(self, 
                 shori_kekka: str = '00', 
                 oto_kekka: str = '00', 
                 shiharai_hoho_kbn: str = '1', 
                 kino_kbn: str = '3', 
                 shop_id: str = '00000', 
                 shuno_kingaku: str = '      ', 
                 ):
        self.shori_kekka: str = shori_kekka              # 処理結果
        self.oto_kekka: str = oto_kekka                  # 応答結果
        self.shiharai_hoho_kbn: str = shiharai_hoho_kbn  # 支払方法区分
        self.kino_kbn: str = kino_kbn                    # 機能区分
        self.shop_id: str = shop_id                      # SHOP-CD
        self.shuno_kingaku: str = shuno_kingaku          # 収納金額


class ResponseInTicketData:
    """
    インターネットチケット　レスポンス期待値データ マッピングNo1
    """
    def __init__(self, 
                 X_shori_kekka: str = '00', 
                 X_shop_id: str = '00000', 
                 X_outou_kekka_kbn: str = '  ', 
                 X_outou_kekka: str = '00', 
                 X_haraikomi: str = '             ', 
                 X_hikikae: str = '             ', 
                 X_goukei: str = 'xxxxxx', 
                 tc_daikin: str = '000000', 
                 X_ticket_cnt:str = '00',
                 is_cancel:bool = False,
                 tc_info_data:str = None,
                 X_hansoku_jan_code:str = '',
                 ):
        self.X_shori_kekka:str = X_shori_kekka           # 処理結果
        self.X_shop_id:str = X_shop_id                   # SHOP-CD
        self.X_outou_kekka_kbn:str = X_outou_kekka_kbn   # 応答結果区分
        self.X_outou_kekka:str = X_outou_kekka           # 応答結果
        self.X_haraikomi:str = X_haraikomi               # 払込票番号
        self.X_hikikae:str = X_hikikae                   # 引換票番号
        self.X_goukei:str = X_goukei                     # 合計金額
        self.X_tc_dai:str = tc_daikin                    # チケット代金
        self.X_tc_kounyu_dai:str = tc_daikin             # チケット購入代金
        self.X_hakken_dai:str = tc_daikin                # 発券代金
        self.X_inshi_kijun:str = tc_daikin               # 印紙基準額
        self.X_ticket_cnt:str = X_ticket_cnt             # チケット枚数
        self.is_pia: bool = X_shop_id == '30514'         # ぴあか否か
        self.is_cancel: bool = is_cancel                 # 取消か否か
        self.tc_info_data:str = tc_info_data             # 券面情報
        self.X_hansoku_jan_code:str = X_hansoku_jan_code # 販促JANコード

class ResponseInTicketDetailData(ResponseInTicketData):
    """
    インターネットチケット　レスポンス期待値データ マッピングNo2
    """
    def __init__(self, 
                 X_shop_id: str = '00000', 
                 X_outou_kekka_kbn: str = '  ', 
                 X_haraikomi: str = '             ', 
                 X_hikikae: str = '             ', 
                 X_tc_dai: str = '000000', 
                 X_tc_kounyu_dai: str = '000000', 
                 X_hakken_dai: str = '000000', 
                 X_inshi_kijun: str = '000000', 
                 X_ticket_cnt:str = '00',
                 tc_info_data:str = None,
                 is_cancel:bool = False,
                 ):
        super().__init__(
            X_shop_id=X_shop_id,
            X_outou_kekka_kbn=X_outou_kekka_kbn,
            X_haraikomi=X_haraikomi,
            X_hikikae=X_hikikae,
            X_ticket_cnt=X_ticket_cnt,
            tc_info_data=tc_info_data,
            is_cancel=is_cancel,
        )
        self.X_tc_dai:str = X_tc_dai                        # チケット代金
        self.X_tc_kounyu_dai:str = X_tc_kounyu_dai          # チケット購入代金
        self.X_hakken_dai:str = X_hakken_dai                # 発券代金
        self.X_inshi_kijun:str = X_inshi_kijun              # 印紙基準額

class ResponseTotoTicketData:
    """
    スポーツ振興くじ レスポンス期待値データ マッピングNo1
    """
    def __init__(self, 
                 X_shori_kekka: str = '00', 
                 X_outou_kekka: str = '00', 
                 X_shop_id: str = '00000', 
                 X_haraikomi: str = '             ', 
                 X_tc_dai: str = '000000', 
                 X_ticket_cnt:str = '00',
                 ):
        self.X_shori_kekka:str = X_shori_kekka    # 処理結果
        self.X_outou_kekka:str = X_outou_kekka    # 応答結果
        self.X_shop_id:str = X_shop_id            # SHOP-CD
        self.X_haraikomi:str = X_haraikomi        # 払込票番号
        self.X_tc_dai:str = X_tc_dai              # チケット代金
        self.X_ticket_cnt:str = X_ticket_cnt      # チケット枚数

class ResponseTotoTicketVoteData(ResponseTotoTicketData):
    """
    スポーツ振興くじ レスポンス期待値データ マッピングNo2
    """
    def __init__(self, 
                 X_shori_kekka: str = '00', 
                 X_outou_kekka: str = '00', 
                 X_shop_id: str = '00000', 
                 X_tc_dai: str = '000000', 
                 X_ticket_cnt:str = '  ',
                 X_toto_kekka:str = '000000',
                 tc_info_data:str = None,
                 is_inji:bool = False,
                 ):
        super().__init__(
            X_shori_kekka=X_shori_kekka,
            X_outou_kekka=X_outou_kekka,
            X_shop_id=X_shop_id,
            X_tc_dai=X_tc_dai,
            X_ticket_cnt=X_ticket_cnt,
        )
        self.X_toto_kekka:str = X_toto_kekka    # totoセンター応答結果
        self.tc_info_data:str = tc_info_data    # 券面情報
        self.is_inji: bool = is_inji            # 投票券バーコード番号印字要否
        
class ResponseTotoTicketRepayData(ResponseTotoTicketData):
    """
    スポーツ振興くじ レスポンス期待値データ マッピングNo3
    """
    def __init__(self, 
                 X_shori_kekka: str = '00', 
                 X_outou_kekka: str = '00', 
                 X_shop_id: str = '00000', 
                 X_haraimodoshi:str = '             ',
                 X_payback_amt: str = '0000000000', 
                 ):
        super().__init__(
            X_shori_kekka=X_shori_kekka,
            X_outou_kekka=X_outou_kekka,
            X_shop_id=X_shop_id,
        )
        self.X_haraimodoshi:str = X_haraimodoshi    # 払戻受付票番号
        self.X_payback_amt:str = X_payback_amt      # 払戻金額

        
class ResponseTotoTicketClearingData(ResponseTotoTicketRepayData):
    """
    スポーツ振興くじ レスポンス期待値データ マッピングNo4
    """
    def __init__(self, 
                 X_shori_kekka: str = '00', 
                 X_outou_kekka: str = '00', 
                 X_haraimodoshi:str = '             ',
                 X_payback_amt: str = '0000000000', 
                 X_toto_kekka:str = None,
                 ):
        super().__init__(
            X_shori_kekka=X_shori_kekka,
            X_outou_kekka=X_outou_kekka,
            X_haraimodoshi=X_haraimodoshi,
            X_shop_id='30801',
            X_payback_amt=X_payback_amt,
        )
        self.X_toto_kekka:str = X_toto_kekka    # totoセンター応答結果

# ---------------------------
# リクエストデータディクショナリ
# ---------------------------
def DEFAULT_DICT_EC():
    return {
        'denbun_kubun': '20',
        'syori_kekka': '00',
        'gyomu_kubun': '0067',
        'kigyo_id': '07',
        'tuban': 'SQ',
        'mise_no': '111111',
        'regi_no': '1',
        'ticket_regi_no': '1',
        'syohin_info_kbn': ' ',
        'riyo_time_ymdhms': '20250205152400',
        'syori_tuban': '20250205001',
        'retry_flg': '0',
        'yokyu_kubun': 'A',
        'toiawase_kanryo_kubun': '1', 
        'bar_code_no': '             ',

        'order_type': ' ',
        'cvs_code': '8037110000004',
        'item_pointer': ' ',
    }

def DEFAULT_DICT_EC_CANCEL():
    return {
        **DEFAULT_DICT_EC(),
        'yokyu_kubun': 'B',
    }

def DEFAULT_DICT_EC_KANRYO():
    ec_dict = {
        **DEFAULT_DICT_EC(),
        'shiharai_hoho_kbn': '1',
        'toiawase_kanryo_kubun': '2', 
        'kino_kbn': '3',
        'shop_id': '00000',
        'shuno_kingaku': '000000',
        'kanryo_tuchi_kubun': '1',
        'otoKekka_kubun': '00',
        'oto_kekka': '00',
    }
    del ec_dict['syohin_info_kbn']
    del ec_dict['order_type']
    del ec_dict['item_pointer']
    return ec_dict


def DEFAULT_DICT_EC_REPAY():
    return {
        'denbun_kubun': '20',
        'syori_kekka': '00',
        'gyomu_kubun': '0067',
        'kigyo_id': '07',
        'mise_no': '111111',
        'tuban': 'SQ',
        'regi_no': '1',
        'ticket_regi_no': ' ',
        'riyo_time_ymdhms': '20250205152400',
        'syori_tuban': '20250205001',
        'retry_flg': '0',
        'yokyu_kubun': 'E',
        'toiawase_kanryo_kubun': '1', 
        "shop_id": '00767',
        'torikeshi_riyu': '  ',
    }

def DEFAULT_DICT_EC_REPAY_CANCEL():
    return {
        **DEFAULT_DICT_EC_REPAY(),
        'yokyu_kubun': 'L',
        'torikeshi_riyu': '01',
    }

def DEFAULT_DICT_IN_TICKET():
    return {
        'X_shori_kekka': '00',
        'X_gyomu_kbn': '0060',
        'X_kigyo_id': '07',
        'X_mise_no': '111111',
        'X_regi_no': '1',
        'X_hakken_regi_no': '1',
        'X_regi_date_min': '20250205152400',
        'X_shori_tuban': '20250205001',
        'X_saiso_kbn': '0',
        'X_yokyu_kbn': '01',
        'X_cvs_code': '03711',
    }


def DEFAULT_DICT_IN_TICKET_CANCEL():
    return {
        **DEFAULT_DICT_IN_TICKET(),
        'X_yokyu_kbn': '21',
        'X_shop_id': '00000',
        'X_order_id': '123456789012',
        'X_torikeshi_riyu': '01',
        'X_kaishu_cnt': '05',
    }

def DEFAULT_DICT_IN_TICKET_KANRYO():
    return {
        **DEFAULT_DICT_IN_TICKET(),
        'X_yokyu_kbn': '02',
        'X_shop_id': '00000',
        'X_order_id': '123456789012',
        'X_nyuukin': '000000',
    }

def DEFAULT_DICT_TOTO():
    return {
        'X_shori_kekka': '00',
        'X_kigyo_id': '07',
        'X_mise_no': '111111',
        'X_regi_no': '1',
        'X_regi_date_min': '20250205152400',
        'X_shori_tuban': '20250205001',
    }

def DEFAULT_DICT_TOTO_BUY():
    return {
        **DEFAULT_DICT_TOTO(),
        'X_saiso_kbn': '0',
        'X_hakken_regi_no': '1',
        'X_yokyu_kbn': '01',
    }
def DEFAULT_DICT_TOTO_BUY_CANCEL():
    return {
        **DEFAULT_DICT_TOTO_BUY(),
        'X_yokyu_kbn': '11',
        'X_torikeshi_riyu': '01',
    }

def DEFAULT_DICT_TOTO_VOTE():
    return {
        **DEFAULT_DICT_TOTO(),
        'X_saiso_kbn': '0',
        'X_hakken_regi_no': '1',
        'X_yokyu_kbn': '02',
        'X_toto_terminal_id': '005123',
        'X_toto_terminal_kbn': '20',
        'X_toto_julian_date': '220',
        'X_toto_julian_time': '01512',
        'X_toto_soukan_id': 'af98a9b8f5135cd2af98a9b8f5135cd2',
    }
def DEFAULT_DICT_TOTO_VOTE_CANCEL():
    return {
        **DEFAULT_DICT_TOTO_VOTE(),
        'X_yokyu_kbn': '12',
        'X_torikeshi_riyu': '01',
        'X_torikeshi_riyu_kbn': '02',
    }


def DEFAULT_DICT_TOTO_REPAY():
    return {
        **DEFAULT_DICT_TOTO(),
        'X_saiso_kbn': '0',
        'X_yokyu_kbn': '03',
        'X_vote_ticket_barcode': '1234567890123',
    }
def DEFAULT_DICT_TOTO_REPAY_CANCEL():
    return {
        **DEFAULT_DICT_TOTO_REPAY(),
        'X_yokyu_kbn': '13',
        'X_torikeshi_riyu': '01',
    }

def DEFAULT_DICT_TOTO_CLEARING():
    return {
        **DEFAULT_DICT_TOTO(),
        'X_yokyu_kbn': '04',
        'X_vote_ticket_barcode': '1234567890123',
        'X_toto_terminal_id': '005123',
        'X_toto_terminal_kbn': '20',
        'X_toto_julian_date': '220',
        'X_toto_julian_time': '01512',
        'X_pos_trade_no': '1234567890123456',
        'X_payback_flg': '1',
    }

# ---------------------------
# 期待値ディクショナリ
# ---------------------------
def COMPARE_EC_DICT(pattern:ResponseEcTicketData):
    return {
        'interface_info' :{
            'syori_kekka': pattern.shori_kekka,
        },
        **get_order_info(pattern),
        **get_tiket_info(pattern)
    }

def COMPARE_EC_REPAY_DICT(pattern:ResponseEcTicketRepayData):
    return {
        'interface_info' :{
            'syori_kekka': pattern.shori_kekka,
        },
        **get_payback_info(pattern),
    }

def COMPARE_EC_KANRYO_DICT(pattern:ResponseEcTicketKanryoData):
    return {
        'interface_info' :{
            'syori_kekka': pattern.shori_kekka,
        },
        **get_order_info_kanryo(pattern),
    }

def COMPARE_IN_TICKET_DICT(pattern:ResponseInTicketData):
    return {
        **get_in_ticket_response(pattern),
    }

def COMPARE_IN_TICKET_KANRYO_DICT(pattern:ResponseInTicketData):
    return {
        **get_in_ticket_kanryo_response(pattern),
    }

def COMPARE_TOTO_TICKET_DICT(pattern:ResponseTotoTicketData):
    return {
        **get_toto_ticket_response(pattern),
    }

def COMPARE_TOTO_TICKET_VOTE_DICT(pattern:ResponseTotoTicketVoteData):
    return {
        **get_toto_ticket_vote_response(pattern),
    }

def COMPARE_TOTO_TICKET_REPAY_DICT(pattern:ResponseTotoTicketRepayData):
    return {
        **get_toto_ticket_repay_response(pattern),
    }

def COMPARE_TOTO_TICKET_CLEARING_DICT(pattern:ResponseTotoTicketClearingData):
    return {
        **get_toto_ticket_clearing_response(pattern),
    }

# ---------------------------
# 期待値作成処理
# ---------------------------
def get_order_info(pattern:ResponseEcTicketData):
    # 処理結果 00 以外なら 処理結果のみ
    if pattern.shori_kekka != '00':
        return {'order_info': "------"}

    if pattern.oto_kekka == '00':
        return {
            'order_info': {
                "oto_kekka": pattern.oto_kekka,
                "pay_type": pattern.pay_type,
                "dlv_type": pattern.dlv_type,
                "keijyo_type": pattern.keijyo_type,
                "inshi_kijun": pattern.inshi_kijun,
                "kingaku_henko_flg": pattern.kingaku_henko_flg,
                "kino_kbn": pattern.kino_kbn,
                "shop_id": pattern.shop_id,
                "shuno_kingaku": pattern.shuno_kingaku
            },
        }
    else:
        # 応答結果 00 以外なら 処理結果、応答結果のみ
        return {
            'order_info': {
                "oto_kekka": pattern.oto_kekka,
            },
        }
        
def get_tiket_info(pattern:ResponseEcTicketData):
    # 処理結果 00 以外なら作成不要
    if pattern.shori_kekka != '00':
        return {'ticket_info': "------"}

    # 取り消しの場合は作成不要
    if pattern.is_cancel:
        return {'ticket_info': None}

    ticket_info = get_normal_ticket_info_from_map(pattern)
    
    ticket_count = pattern.ticket_count
    return {
        'ticket_info': {
            **{f'html_name{i}': ticket_info['html_name'] for i in range(1, ticket_count)},
            **{f'barcode{i}': ticket_info['barcode'] for i in range(1, ticket_count)},
            **{f'ticket_data{i}': ticket_info['ticket_data'] for i in range(1, ticket_count)},
        } 
    }

def get_normal_ticket_info_from_map(pattern:ResponseEcTicketData):
    retdict = {
        'barcode': 'xxxxxx' if pattern.is_pia else '             ',
    }
    template_mapping = {
        'A': {
            'html_name' : EC_HTML_NAME_A,
            'ticket_data' : EC_TICKET_DATA_A,
        },
        'B': {
            'html_name' : EC_HTML_NAME_BC,
            'ticket_data' : EC_TICKET_DATA_B,
        },
        'C': {
            'html_name' : EC_HTML_NAME_BC,
            'ticket_data' : EC_TICKET_DATA_C,
        },
        'D': {
            'html_name' : EC_HTML_NAME_D,
            'ticket_data' : EC_TICKET_DATA_D,
        },
        'E': {
            'html_name' : EC_HTML_NAME_E,
            'ticket_data' : EC_TICKET_DATA_E,
        },
        'F': {
            'html_name' : EC_HTML_NAME_F,
            'ticket_data' : EC_TICKET_DATA_F,
        },
        'G': {
            'html_name' : EC_HTML_NAME_G,
            'ticket_data' : EC_TICKET_DATA_G,
        },
        'H': {
            'html_name' : EC_HTML_NAME_H,
            'ticket_data' : EC_TICKET_DATA_H,
        },
        'I': {
            'html_name' : EC_HTML_NAME_I,
            'ticket_data' : EC_TICKET_DATA_I,
        },
        ' ': {
            'html_name' : EC_HTML_NAME_PIA if pattern.is_pia else EC_HTML_NAME_NORMAL,
            'ticket_data' : EC_TICKET_DATA_PIA if pattern.is_pia else EC_TICKET_DATA_NORMAL,
        },
    }

    retdict.update(template_mapping.get(pattern.tc_info_data))
    return retdict


def get_payback_info(pattern:ResponseEcTicketRepayData):
    # 処理結果 00 以外なら 処理結果のみ
    if pattern.shori_kekka != '00':
        return {'payback_info': "------"}

    if pattern.oto_kekka == '00':
        return {
            'payback_info': {
                "oto_kekka": pattern.oto_kekka,
                "shop_id": '00767',
                "payback_kingaku": pattern.payback_kingaku,
                "payback_start_ymd": pattern.payback_start_ymd,
                "payback_end_ymd": pattern.payback_end_ymd,
                "svc_time_start_hm": pattern.svc_time_start_hm,
                "svc_time_end_hm": pattern.svc_time_end_hm,
                "hanken_yohi": pattern.hanken_yohi,
                "payback_tesuryo": pattern.payback_tesuryo
            },
        }
    else:
        # 応答結果 00 以外なら 処理結果、応答結果のみ
        return {
            'payback_info': {
                "oto_kekka": pattern.oto_kekka,
            },
        }
    
def get_order_info_kanryo(pattern:ResponseEcTicketKanryoData):
    # 処理結果 00 以外なら 処理結果のみ
    if pattern.shori_kekka != '00':
        return {'order_info': "------"}


    if pattern.oto_kekka == '00':
        return {
            'order_info': {
                "oto_kekka": pattern.oto_kekka,
                "kino_kbn": pattern.kino_kbn,
                "shop_id": pattern.shop_id,
                "shuno_kingaku": pattern.shuno_kingaku
            },
        }
    else:
        # 応答結果 00 以外なら 処理結果、応答結果のみ
        return {
            'order_info': {
                "oto_kekka": pattern.oto_kekka,
            },
        }

def get_in_ticket_response(pattern:ResponseInTicketData):
    retdict = {
        'X_shori_kekka': pattern.X_shori_kekka,
        'X_outou_kekka': "------",
    }

    # 処理結果 00 以外なら 処理結果のみ
    if pattern.X_shori_kekka != '00':
        return retdict

    # 応答結果 00 以外なら 処理結果、応答結果のみ
    retdict['X_outou_kekka'] = pattern.X_outou_kekka
    if pattern.X_outou_kekka != '00':
        return retdict
        
    retdict.update(
        {
            'X_shop_id': pattern.X_shop_id,
            'X_outou_kekka_kbn': pattern.X_outou_kekka_kbn,
            'X_haraikomi': pattern.X_haraikomi,
            'X_hikikae': pattern.X_hikikae,
            'X_goukei': pattern.X_goukei,
            'X_tc_dai': pattern.X_tc_dai,
            'X_tc_kounyu_dai': pattern.X_tc_kounyu_dai,
            'X_hakken_dai': pattern.X_hakken_dai,
            'X_inshi_kijun': pattern.X_inshi_kijun,
            'X_ticket_hon_cnt': 'xxxxxx',
            'X_ticket_cnt': pattern.X_ticket_cnt,
        }
    )

    # 応答結果区分 01 のデータ加工
    if pattern.X_outou_kekka_kbn == '01':
        del retdict['X_hikikae']

    # 応答結果区分 02 のデータ加工
    if pattern.X_outou_kekka_kbn == '02':
        retdict['X_ticket_hon_cnt'] = '00'
        retdict['X_ticket_cnt'] = '00'

    # 応答結果区分 03 のデータ加工
    if pattern.X_outou_kekka_kbn == '03':
        del retdict['X_haraikomi']
        retdict['X_tc_dai'] = '000000'
        retdict['X_tc_kounyu_dai'] = '000000'

    # 応答結果区分 04 のデータ加工
    if pattern.X_outou_kekka_kbn == '04':
        del retdict['X_hikikae']
        retdict['X_hakken_dai'] = '000000'
        retdict['X_ticket_hon_cnt'] = '00'
        retdict['X_ticket_cnt'] = '00'

    retdict.update(get_tc_info(pattern))
    # if pattern.is_cancel:
    #     # 取消時はリクエストの値
    #     retdict['X_shop_id'] = '00000'

    return retdict

def get_in_ticket_kanryo_response(pattern:ResponseInTicketData):
    retdict = {
        'X_shori_kekka': pattern.X_shori_kekka,
        'X_outou_kekka': "------",
    }

    # 処理結果 00 以外なら 処理結果のみ
    if pattern.X_shori_kekka != '00':
        return retdict

    # 応答結果 00 以外なら 処理結果、応答結果のみ
    retdict['X_outou_kekka'] = pattern.X_outou_kekka
    if pattern.X_outou_kekka != '00':
        return retdict
        
    retdict.update(
        {
            'X_shop_id': '00000',
            # 'X_shop_id': pattern.X_shop_id,
            'X_outou_kekka_kbn': '99',
            'X_nyuukin': '000000',
        }
    )

    return retdict

def get_tc_info(pattern:ResponseInTicketData):
    # 取消なら作成不要
    if pattern.is_cancel:
        return {'tc_info': "------"}

    # 応答結果区分 02, 04 なら作成不要
    if pattern.X_outou_kekka_kbn in ('02', '04'):
        return {'tc_info': "------"}

    # チケット0枚なら作成不要
    num = int(pattern.X_ticket_cnt)
    if num == 0:
        return {'tc_info': "------"}

    # チケット情報 期待値取得
    tc_info_list = get_tc_info_list(pattern)

    return {'tc_info': tc_info_list}


def get_tc_info_list(pattern:ResponseInTicketData) -> list[dict]:

    # X_ticket_cnt を整数に変換
    ticket_cnt = int(pattern.X_ticket_cnt)

    if pattern.tc_info_data == None:
        tc_template = TEMP_CODE_PIA if pattern.is_pia else TEMP_CODE_NORMAL
        return [
            {
                'X_tc_barcode_no': 'xxxxxx',
                'X_tc_kbn': '1',
                'X_tc_template': tc_template,
            }
            for i in range(1, ticket_cnt + 1)
        ]

    template_mapping = {
        'A': {
            'X_tc_barcode_no' : None,
            'X_tc_template' : TEMP_CODE_SHOP_30400_NO_BARCODE_MAIN,
            'X_tc_kbn' : NO_BARCODE_MAIN_TICKET,
        },
        'B': {
            'X_tc_barcode_no' : 'xxxxxx',
            'X_tc_template' : TEMP_CODE_SHOP_30400_BARCODE_MAIN,
            'X_tc_kbn' : BARCODE_MAIN_TICKET,
        },
        'C': {
            'X_tc_barcode_no' : 'xxxxxx',
            'X_tc_template' : TEMP_CODE_PIA,
            'X_tc_kbn' : BARCODE_MAIN_TICKET,
        },
        'D': {
            'X_tc_barcode_no' : None,
            'X_tc_template' : TEMP_CODE_SHOP_30400_NO_BARCODE_OTHER,
            'X_tc_kbn' : NO_BARCODE_OTHER_TICKET,
        },
        'E': {
            'X_tc_barcode_no' : 'xxxxxx',
            'X_tc_template' : TEMP_CODE_SHOP_30501,
            'X_tc_kbn' : BARCODE_OTHER_TICKET,
        },
        'F': {
            'X_tc_barcode_no' : 'xxxxxx',
            'X_tc_template' : TEMP_CODE_SHOP_30501,
            'X_tc_kbn' : BARCODE_OTHER_TICKET,
        },
        'P01': {
            'X_tc_barcode_no' : 'xxxxxx',
            'X_tc_template' : TEMP_CODE_SHOP_30500,
            'X_tc_kbn' : BARCODE_MAIN_TICKET,
        },
        'R01': {
            'X_tc_barcode_no' : 'xxxxxx',
            'X_tc_template' : TEMP_CODE_SHOP_30500,
            'X_tc_kbn' : BARCODE_MAIN_TICKET,
        },
        'S01': {
            'X_tc_barcode_no' : 'xxxxxx',
            'X_tc_template' : TEMP_CODE_SHOP_30500,
            'X_tc_kbn' : BARCODE_MAIN_TICKET,
        },
        'T': {
            'X_tc_barcode_no' : 'xxxxxx',
            'X_tc_template' : TEMP_CODE_SHOP_30701,
            'X_tc_kbn' : BARCODE_MAIN_TICKET,
        },
        'U': {
            'X_tc_barcode_no' : None,
            'X_tc_template' : TEMP_CODE_SHOP_30701,
            'X_tc_kbn' : NO_BARCODE_OTHER_TICKET,
        },
        'V': {
            'X_tc_barcode_no' : 'xxxxxx',
            'X_tc_template' : TEMP_CODE_SHOP_30705,
            'X_tc_kbn' : BARCODE_MAIN_TICKET,
        },
        'W': {
            'X_tc_barcode_no' : None,
            'X_tc_template' : TEMP_CODE_SHOP_30705,
            'X_tc_kbn' : NO_BARCODE_OTHER_TICKET,
        },
    }

    other_mapping = {
        'X_tc_barcode_no' : 'xxxxxx',
        'X_tc_template' : TEMP_CODE_SHOP_30514_CASE_2,
        'X_tc_kbn' : BARCODE_MAIN_TICKET,
    }

    # info_data を _ で分割してキーを取得
    keys = pattern.tc_info_data.split('_')


    # 抽出された情報を繰り返してリストを作成
    result_list = []

    # カウンタを用意して処理
    counter = 0
    for _ in range(ticket_cnt):
        for key in keys:
            mapdata = template_mapping.get(key, other_mapping)
            result_list.append(mapdata)
            counter += 1
            if counter >= ticket_cnt:
                break
        if counter >= ticket_cnt:
            break

    return result_list


def get_toto_ticket_response(pattern:ResponseTotoTicketData):
    retdict = {
        'X_shori_kekka': pattern.X_shori_kekka,
        'X_outou_kekka': "------",
    }

    # 処理結果 00 以外なら 処理結果のみ
    if pattern.X_shori_kekka != '00':
        return retdict

    # 応答結果 00 以外なら 処理結果、応答結果のみ
    retdict['X_outou_kekka'] = pattern.X_outou_kekka
    if pattern.X_outou_kekka != '00':
        return retdict
        
    retdict.update(
        {
            'X_shop_id': pattern.X_shop_id,
            'X_haraikomi': pattern.X_haraikomi,
            'X_tc_dai': pattern.X_tc_dai,
            'X_ticket_cnt': pattern.X_ticket_cnt,
        }
    )
    return retdict

def get_toto_ticket_vote_response(pattern:ResponseTotoTicketVoteData):
    retdict = {
        'X_shori_kekka': pattern.X_shori_kekka,
        'X_outou_kekka': "------",
    }

    # 処理結果 00 以外なら 処理結果のみ
    if pattern.X_shori_kekka != '00':
        return retdict

    retdict['X_outou_kekka'] = pattern.X_outou_kekka
    retdict['X_toto_kekka'] = pattern.X_toto_kekka

    # 応答結果 00 以外なら 処理結果、応答結果、TOTOセンター応答結果のみ
    if pattern.X_outou_kekka != '00':
        # 13 以外の場合は空タグ
        if pattern.X_outou_kekka != '13':
            retdict['X_toto_kekka'] = None
        return retdict
        
    retdict.update(
        {
            'X_ticket_cnt': pattern.X_ticket_cnt,
            'X_toto_kekka': '000000',
            **get_toto_tc_info(pattern)
        }
    )

    return retdict


def get_toto_tc_info(pattern:ResponseTotoTicketVoteData):
    # 取消(券面データが空)なら作成不要
    if pattern.tc_info_data == None:
        return {'tc_info': "------"}

    # チケット0枚なら作成不要
    num = int(pattern.X_ticket_cnt)
    if num == 0:
        return {'tc_info': "------"}

    # 辞書を作成
    tc_info_list = []

    vote_barcode = 'xxxxxx' if pattern.is_inji else None

    tc_template = get_toto_tc_template(pattern.tc_info_data)

    # チケット枚数分のループで辞書を作成してリストに追加
    tc_info_list = [
        {
            'X_vote_ticket_barcode': vote_barcode,
            'X_tc_template': tc_template,
        }
        for i in range(1, num + 1)
    ]

    return {'tc_info': tc_info_list}

def get_toto_tc_template(tc_info_data):
    # テンプレートマッピング
    template_mapping = {
        'A': TEMP_CODE_TOTO_BIG_NORMAL,
        'B': TEMP_CODE_TOTO_BIG_NORMAL,
        'C': TEMP_CODE_TOTO_BIG_NORMAL,
        'D': TEMP_CODE_TOTO_GOAL,
        'E': TEMP_CODE_TOTO_GOAL,
        'F': TEMP_CODE_TOTO_MEGA_BIG,
    }
    return template_mapping.get(tc_info_data)

def get_toto_ticket_repay_response(pattern:ResponseTotoTicketRepayData):
    retdict = {
        'X_shori_kekka': pattern.X_shori_kekka,
        'X_outou_kekka': "------",
    }

    # 処理結果 00 以外なら 処理結果のみ
    if pattern.X_shori_kekka != '00':
        return retdict

    # 応答結果 00 以外なら 処理結果、応答結果のみ
    retdict['X_outou_kekka'] = pattern.X_outou_kekka
    if pattern.X_outou_kekka != '00':
        return retdict
        
    retdict.update(
        {
            'X_shop_id': pattern.X_shop_id,
            'X_haraimodoshi': pattern.X_haraimodoshi,
            'X_payback_amt': pattern.X_payback_amt,
        }
    )
    return retdict

def get_toto_ticket_clearing_response(pattern:ResponseTotoTicketClearingData):
    retdict = {
        'X_shori_kekka': pattern.X_shori_kekka,
        'X_outou_kekka': "------",
    }

    # 処理結果 00 以外なら 処理結果のみ
    if pattern.X_shori_kekka != '00':
        return retdict

    retdict['X_outou_kekka'] = pattern.X_outou_kekka

    # 応答結果 に応じたセンター応答結果を期待値に指定
    if pattern.X_outou_kekka == '00':
        # 00 の場合は 000000
        retdict['X_toto_kekka'] = '000000'
    elif pattern.X_outou_kekka != '13':
        # 13 以外の場合は空タグ
        retdict['X_toto_kekka'] = None
    else:
        retdict['X_toto_kekka'] = pattern.X_toto_kekka

    return retdict


# ---------------------------
# 共通処理
# ---------------------------
def mock_ticket_ms_main(reqres_dict:list[dict], response_type:str):
    error_case:str
    try:
        if response_type == EC_TICKET:
            import in_const
            in_const.TIMEOUT_SEC = 1
            for reqres in reqres_dict:
                req = reqres['req']

                error_case = reqres.get('case_name')
                logger.info(f"[mock_ticket_ms_main] case_name: {error_case}")
                res:Response = mock_ecticket_ms_main(req)
                dict_res = response_to_dict(res, response_type)
                
                compare_dicts(reqres['res'], dict_res)
        elif response_type == IN_TICKET:
            import in_const
            in_const.TIMEOUT_SEC = 1
            for reqres in reqres_dict:
                req = reqres['req']

                error_case = reqres.get('case_name')
                logger.info(f"[mock_ticket_ms_main] case_name: {error_case}")
                res:Response = mock_inticket_ms_main(req)
                dict_res = response_to_dict(res, response_type)
                
                compare_dicts(reqres['res'], dict_res)
        elif response_type == TOTO_TICKET:
            import toto_constant
            toto_constant.TIMEOUT_SEC = 1
            for reqres in reqres_dict:
                req = reqres['req']

                error_case = reqres.get('case_name')
                logger.info(f"[mock_ticket_ms_main] case_name: {error_case}")
                res:Response = mock_toto_register_ms_main(req, logger)
                dict_res = response_to_dict(res, response_type)
                
                compare_dicts(reqres['res'], dict_res)

    except Exception as e: # pragma: no cover
        # エラーとなったcase_nameと、リクエスト情報を表示
        logger.error(f"[error case] case_name: {error_case}")
        logger.error(f"error request: {req}")
        raise   

# XMLを辞書形式に変換する関数
def xml_to_dict(element):
    result = {}
    stack = [(element, result)]

    while stack:
        current_element, current_dict = stack.pop()
        for child in current_element:
            tag = strip_ns(child.tag)
            if len(child) == 0:
                child_dict = child.text
            else:
                child_dict = {}

            if tag == "tc_info":
                if tag not in current_dict:
                    current_dict[tag] = []
                current_dict[tag].append(child_dict)
            else:
                if tag in current_dict:
                    if isinstance(current_dict[tag], list):
                        current_dict[tag].append(child_dict)
                    else:
                        current_dict[tag] = [current_dict[tag], child_dict]
                else:
                    current_dict[tag] = child_dict
            
            if isinstance(child_dict, dict):
                stack.append((child, child_dict))
    return result


# 名前空間を無視する
def strip_ns(tag):
    return tag.split('}', 1)[-1] if '}' in tag else tag

def response_to_dict(response, response_type:str = EC_TICKET):
    
    try:
        # レスポンスからXML部分を抽出し、UTF-8に変換
        xml_content_bytes = response.get_data()
        xml_content = xml_content_bytes.decode('cp932')

        # XMLを解析
        root = ET.fromstring(xml_content)

        # 取得する階層決定
        search_str = ''
        if response_type == EC_TICKET:
            search_str = './/{http://sej.co.jp/}response'
        elif response_type == IN_TICKET:
            search_str = './/{http://regifront.sej.co.jp/}body'
        elif response_type == TOTO_TICKET:
            search_str = './/{http://sej.co.jp/}body'

        # `response'/'body`階層を取得
        response_element = root.find(search_str)

        # `response'/'body`階層を辞書に変換
        return xml_to_dict(response_element)

    except AttributeError as e: # pragma: no cover
        print(f"[response_to_dict error response]: {response}")
        raise

def compare_dicts(expected, actual):
    """
    2つの辞書を比較し、expectedの項目がactualに含まれているか確認
    """

    try:
        stack = [(expected, actual)]

        while stack:
            exp, act = stack.pop()
            for key, value in exp.items():
                if value == "------":
                    assert key not in act, f"不要なキーが存在する: {key}"
                    continue
                else:
                    assert key in act, f"必要なキーが不足している: {key}"
                if isinstance(value, dict):
                    stack.append((value, act[key]))
                elif isinstance(value, list):
                    assert isinstance(act[key], list), f"Type mismatch at {key}: expected list, got {type(act[key])}"
                    assert len(value) == len(act[key]), f"Length mismatch at {key}: expected {len(value)}, got {len(act[key])}"
                    for i in range(len(value)):
                        stack.append((value[i], act[key][i]))
                else:
                    if act[key] != value:
                        print(f"Value mismatch at {key}: expected {value}, got {act[key]}")
                    if value == "xxxxxx":
                        try:
                            actual_value = float(act.get(key))
                        except ValueError: # pragma: no cover
                            # 文字列が数値に変換できない場合はAssertionError
                            assert False, f"'{key}' を数値に変換できない. Expected: {value}, Actual: {act.get(key)}"
                        # xxxxxx が期待値に指定されている場合、 0 以上の数値であればOKとする
                        assert actual_value >= 0
                    else:
                        assert act.get(key) == value, f"'{key}' が期待値と一致しない. Expected: {value}, Actual: {act.get(key)}"


    except (AssertionError, TypeError) as e: # pragma: no cover
        # AssertionError, TypeErrorをキャッチして、比較対象を表示
        print(f"[compare_dicts error response]")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        raise


# ---------------------------
# 異常系レスポンス
# ---------------------------
def RESPONSE_SHORI_KEKKA_10():
    data =  ResponseEcTicketData(
        shori_kekka='10',
    )
    return COMPARE_EC_DICT(data)

def RESPONSE_SHORI_KEKKA_11():
    data =  ResponseEcTicketData(
        shori_kekka='11',
    )
    return COMPARE_EC_DICT(data)

def RESPONSE_SHORI_KEKKA_14():
    data =  ResponseEcTicketData(
        shori_kekka='14',
    )
    return COMPARE_EC_DICT(data)

def RESPONSE_SHORI_KEKKA_99():
    data =  ResponseEcTicketData(
        shori_kekka='99',
    )
    return COMPARE_EC_DICT(data)


def RESPONSE_X_SHORI_KEKKA_99():
    data =  ResponseInTicketData(
        X_shori_kekka='99',
    )
    return COMPARE_IN_TICKET_DICT(data)