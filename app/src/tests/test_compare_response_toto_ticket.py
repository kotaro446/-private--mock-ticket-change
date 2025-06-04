from test_barcode_functions import *

# ---------------------------
# スポーツ振興くじ マッピングNo1
# ---------------------------
def BARCODE_TOTO_BUY_CASE_01():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    チケット代金 : 000000
    チケット枚数 : 0
    レスポンスパターン（再送用） : "0"：再送時正常返却
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    チケット代金 : 000000
    レスポンスパターン（取消再送用） : "0"：再送時正常返却
    ショップID : 30514
    """
    return '4000000000044'
def RESPONSE_TICKET_DATA_TOTO_BUY_CASE_01():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='00',
        X_shop_id='30514',
        X_haraikomi='4000000000044',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_CASE_01_CANCEL():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='00',
        X_shop_id='30514',
        X_haraikomi='4000000000044',
    )
    return COMPARE_TOTO_TICKET_DICT(data)

def BARCODE_TOTO_BUY_CASE_02():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    チケット代金 : 003500
    チケット枚数 : 1
    レスポンスパターン（再送用） : "0"：再送時正常返却
    処理結果 : "16"：SEJセンター混雑エラー
    応答結果 : "00"：正常応答
    チケット代金 : 003500
    レスポンスパターン（取消再送用） : "0"：再送時正常返却
    ショップID : 00000
    """
    return '4000002969929'
def RESPONSE_TICKET_DATA_TOTO_BUY_CASE_02():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_haraikomi='4000002969929',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_CASE_02_CANCEL():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='01',
        X_shori_kekka='16',
        X_tc_dai='003500',
        X_haraikomi='4000002969929',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_CASE_02_CANCEL_RETRY():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='01',
        X_tc_dai='003500',
        X_haraikomi='4000002969929',
    )
    return COMPARE_TOTO_TICKET_DICT(data)

def BARCODE_TOTO_BUY_CASE_03():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    チケット代金 : 010000
    チケット枚数 : 2
    レスポンスパターン（再送用） : "0"：再送時正常返却
    処理結果 : "99"：その他エラー(400)
    応答結果 : "00"：正常応答
    チケット代金 : 010000
    レスポンスパターン（取消再送用） : "1"：再送時異常返却
    ショップID : 30514
    """
    return '4000005940048'
def RESPONSE_TICKET_DATA_TOTO_BUY_CASE_03():
    data =  ResponseTotoTicketData(
        X_tc_dai='010000',
        X_ticket_cnt='02',
        X_shop_id='30514',
        X_haraikomi='4000005940048',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_CASE_03_CANCEL():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='02',
        X_shori_kekka='99',
        X_tc_dai='010000',
        X_shop_id='30514',
        X_haraikomi='4000005940048',
    )
    return COMPARE_TOTO_TICKET_DICT(data)

def BARCODE_TOTO_BUY_CASE_04():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    チケット代金 : 999999
    チケット枚数 : 3
    レスポンスパターン（再送用） : "0"：再送時正常返却
    処理結果 : "99"：その他エラー(500)
    応答結果 : "00"：正常応答
    チケット代金 : 999999
    レスポンスパターン（取消再送用） : "0"：再送時正常返却
    ショップID : 30801
    """
    return '4000008909844'
def RESPONSE_TICKET_DATA_TOTO_BUY_CASE_04():
    data =  ResponseTotoTicketData(
        X_tc_dai='999999',
        X_ticket_cnt='03',
        X_shop_id='30801',
        X_haraikomi='4000008909844',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_CASE_04_CANCEL():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='03',
        X_shori_kekka='99',
        X_tc_dai='999999',
        X_shop_id='30801',
        X_haraikomi='4000008909844',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_CASE_04_CANCEL_RETRY():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='03',
        X_tc_dai='999999',
        X_shop_id='30801',
        X_haraikomi='4000008909844',
    )
    return COMPARE_TOTO_TICKET_DICT(data)

def BARCODE_TOTO_BUY_CASE_05():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    チケット代金 : 003500
    チケット枚数 : 4
    レスポンスパターン（再送用） : "0"：再送時正常返却
    処理結果 : "00"：タイムアウト(正常)
    応答結果 : "00"：正常応答
    チケット代金 : 003500
    レスポンスパターン（取消再送用） : "1"：再送時異常返却
    ショップID : 99999
    """
    return '4000004014689'
def RESPONSE_TICKET_DATA_TOTO_BUY_CASE_05():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='04',
        X_shop_id='99999',
        X_haraikomi='4000004014689',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_CASE_05_CANCEL():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='04',
        X_tc_dai='003500',
        X_shop_id='99999',
        X_haraikomi='4000004014689',
    )
    return COMPARE_TOTO_TICKET_DICT(data)

def BARCODE_TOTO_BUY_CASE_06():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    チケット代金 : 003500
    チケット枚数 : 5
    レスポンスパターン（再送用） : "0"：再送時正常返却
    処理結果 : "99"：タイムアウト(その他エラー500)
    応答結果 : "00"：正常応答
    チケット代金 : 003500
    レスポンスパターン（取消再送用） : "0"：再送時正常返却
    ショップID : 30514
    """
    return '4000004362605'
def RESPONSE_TICKET_DATA_TOTO_BUY_CASE_06():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='05',
        X_shop_id='30514',
        X_haraikomi='4000004362605',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_CASE_06_CANCEL():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='05',
        X_shori_kekka='99',
        X_tc_dai='003500',
        X_shop_id='30514',
        X_haraikomi='4000004362605',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_CASE_06_CANCEL_RETRY():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='05',
        X_tc_dai='003500',
        X_shop_id='30514',
        X_haraikomi='4000004362605',
    )
    return COMPARE_TOTO_TICKET_DICT(data)

def BARCODE_TOTO_BUY_CASE_07():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    チケット代金 : 049999
    チケット枚数 : 1
    レスポンスパターン（再送用） : "0"：再送時正常返却
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    チケット代金 : 049999
    レスポンスパターン（取消再送用） : "0"：再送時正常返却
    ショップID : 30514
    """
    return '4000010814761'
def RESPONSE_TICKET_DATA_TOTO_BUY_CASE_07():
    data =  ResponseTotoTicketData(
        X_tc_dai='049999',
        X_ticket_cnt='01',
        X_shop_id='30514',
        X_haraikomi='4000010814761',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_CASE_07_CANCEL():
    data =  ResponseTotoTicketData(
        X_tc_dai='049999',
        X_ticket_cnt='01',
        X_shop_id='30514',
        X_haraikomi='4000010814761',
    )
    return COMPARE_TOTO_TICKET_DICT(data)

def BARCODE_TOTO_BUY_CASE_08():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    チケット代金 : 050000
    チケット枚数 : 1
    レスポンスパターン（再送用） : "0"：再送時正常返却
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    チケット代金 : 050000
    レスポンスパターン（取消再送用） : "0"：再送時正常返却
    ショップID : 30514
    """
    return '4000013436526'
def RESPONSE_TICKET_DATA_TOTO_BUY_CASE_08():
    data =  ResponseTotoTicketData(
        X_tc_dai='050000',
        X_ticket_cnt='01',
        X_shop_id='30514',
        X_haraikomi='4000013436526',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_CASE_08_CANCEL():
    data =  ResponseTotoTicketData(
        X_tc_dai='050000',
        X_ticket_cnt='01',
        X_shop_id='30514',
        X_haraikomi='4000013436526',
    )
    return COMPARE_TOTO_TICKET_DICT(data)

def BARCODE_TOTO_BUY_SYORI_KEKKA_14():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "14"：サービス時間帯エラー
    応答結果 : "00"：正常応答
    チケット代金 : 003500
    チケット枚数 : 1
    レスポンスパターン（再送用） : "0"：再送時正常返却
    処理結果 : "00"：正常
    応答結果 : "04"：未入金/発券エラー
    チケット代金 : 003500
    レスポンスパターン（取消再送用） : "0"：再送時正常返却
    ショップID : 00000
    """
    return '4000338496328'
def RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_14():
    data =  ResponseTotoTicketData(
        X_shori_kekka='14',
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_haraikomi='4000338496328',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_14_RETRY():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_haraikomi='4000338496328',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_14_CANCEL():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='01',
        X_outou_kekka='04',
        X_tc_dai='003500',
        X_haraikomi='4000338496328',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_14_CANCEL_RETRY():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='01',
        X_tc_dai='003500',
        X_haraikomi='4000338496328',
    )
    return COMPARE_TOTO_TICKET_DICT(data)

def BARCODE_TOTO_BUY_SYORI_KEKKA_16():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "16"：SEJセンター混雑エラー
    応答結果 : "00"：正常応答
    チケット代金 : 003500
    チケット枚数 : 1
    レスポンスパターン（再送用） : "1"：再送時異常返却
    処理結果 : "00"：正常
    応答結果 : "06"：入金/発券済みエラー
    チケット代金 : 003500
    レスポンスパターン（取消再送用） : "0"：再送時正常返却
    ショップID : 30514
    """
    return '4000674207084'
def RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_16():
    data =  ResponseTotoTicketData(
        X_shori_kekka='16',
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30514',
        X_haraikomi='4000674207084',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_16_CANCEL():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='01',
        X_outou_kekka='06',
        X_tc_dai='003500',
        X_shop_id='30514',
        X_haraikomi='4000674207084',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_16_CANCEL_RETRY():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='01',
        X_tc_dai='003500',
        X_shop_id='30514',
        X_haraikomi='4000674207084',
    )
    return COMPARE_TOTO_TICKET_DICT(data)

def BARCODE_TOTO_BUY_SYORI_KEKKA_99_400():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "99"：その他エラー(400)
    応答結果 : "00"：正常応答
    チケット代金 : 003500
    チケット枚数 : 1
    レスポンスパターン（再送用） : "0"：再送時正常返却
    処理結果 : "00"：正常
    応答結果 : "06"：入金/発券済みエラー
    チケット代金 : 003500
    レスポンスパターン（取消再送用） : "0"：再送時正常返却
    ショップID : 30514
    """
    return '4001009587567'
def RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_99_400():
    data =  ResponseTotoTicketData(
        X_shori_kekka='99',
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30514',
        X_haraikomi='4001009587567',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_99_400_RETRY():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30514',
        X_haraikomi='4001009587567',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_99_400_CANCEL():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='01',
        X_outou_kekka='06',
        X_tc_dai='003500',
        X_shop_id='30514',
        X_haraikomi='4001009587567',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_99_400_CANCEL_RETRY():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='01',
        X_tc_dai='003500',
        X_shop_id='30514',
        X_haraikomi='4001009587567',
    )
    return COMPARE_TOTO_TICKET_DICT(data)

def BARCODE_TOTO_BUY_SYORI_KEKKA_99_500():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "99"：その他エラー(500)
    応答結果 : "00"：正常応答
    チケット代金 : 003500
    チケット枚数 : 1
    レスポンスパターン（再送用） : "0"：再送時正常返却
    処理結果 : "00"：正常
    応答結果 : "06"：入金/発券済みエラー
    チケット代金 : 003500
    レスポンスパターン（取消再送用） : "0"：再送時正常返却
    ショップID : 30514
    """
    return '4001345131882'
def RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_99_500():
    data =  ResponseTotoTicketData(
        X_shori_kekka='99',
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30514',
        X_haraikomi='4001345131882',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_99_500_RETRY():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30514',
        X_haraikomi='4001345131882',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_99_500_CANCEL():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='01',
        X_outou_kekka='06',
        X_tc_dai='003500',
        X_shop_id='30514',
        X_haraikomi='4001345131882',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_99_500_CANCEL_RETRY():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='01',
        X_tc_dai='003500',
        X_shop_id='30514',
        X_haraikomi='4001345131882',
    )
    return COMPARE_TOTO_TICKET_DICT(data)

def BARCODE_TOTO_BUY_SYORI_KEKKA_TIMEOUT():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：タイムアウト(正常)
    応答結果 : "00"：正常応答
    チケット代金 : 003500
    チケット枚数 : 1
    レスポンスパターン（再送用） : "0"：再送時正常返却
    処理結果 : "00"：正常
    応答結果 : "01"：検索キーエラー
    チケット代金 : 003500
    レスポンスパターン（取消再送用） : "0"：再送時正常返却
    ショップID : 30514
    """
    return '4001680686443'
def RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_TIMEOUT():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30514',
        X_haraikomi='4001680686443',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_TIMEOUT_CANCEL():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='01',
        X_outou_kekka='01',
        X_tc_dai='003500',
        X_shop_id='30514',
        X_haraikomi='4001680686443',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_TIMEOUT_CANCEL_RETRY():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='01',
        X_tc_dai='003500',
        X_shop_id='30514',
        X_haraikomi='4001680686443',
    )
    return COMPARE_TOTO_TICKET_DICT(data)

def BARCODE_TOTO_BUY_SYORI_KEKKA_TIMEOUT_99():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "99"：タイムアウト(その他エラー500)
    応答結果 : "00"：正常応答
    チケット代金 : 003500
    チケット枚数 : 1
    レスポンスパターン（再送用） : "1"：再送時異常返却
    処理結果 : "00"：正常
    応答結果 : "06"：入金/発券済みエラー
    チケット代金 : 003500
    レスポンスパターン（取消再送用） : "0"：再送時正常返却
    ショップID : 30514
    """
    return '4002016384361'
def RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_TIMEOUT_99():
    data =  ResponseTotoTicketData(
        X_shori_kekka='99',
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30514',
        X_haraikomi='4002016384361',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_TIMEOUT_99_CANCEL():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='01',
        X_outou_kekka='06',
        X_tc_dai='003500',
        X_shop_id='30514',
        X_haraikomi='4002016384361',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_TIMEOUT_99_CANCEL_RETRY():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='01',
        X_tc_dai='003500',
        X_shop_id='30514',
        X_haraikomi='4002016384361',
    )
    return COMPARE_TOTO_TICKET_DICT(data)

def BARCODE_TOTO_BUY_OUTOU_KEKKA_01():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "01"：検索キーエラー
    チケット代金 : 003500
    チケット枚数 : 1
    レスポンスパターン（再送用） : "0"：再送時正常返却
    処理結果 : "00"：正常
    応答結果 : "07"：入金/発券期限エラー
    チケット代金 : 003500
    レスポンスパターン（取消再送用） : "1"：再送時異常返却
    ショップID : 30801
    """
    return '4000023928882'
def RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_01():
    data =  ResponseTotoTicketData(
        X_outou_kekka='01',
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4000023928882',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_01_RETRY():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4000023928882',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_01_CANCEL():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='01',
        X_outou_kekka='07',
        X_tc_dai='003500',
        X_shop_id='30801',
        X_haraikomi='4000023928882',
    )
    return COMPARE_TOTO_TICKET_DICT(data)

def BARCODE_TOTO_BUY_OUTOU_KEKKA_02():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "02"：店舗チェックエラー
    チケット代金 : 003500
    チケット枚数 : 1
    レスポンスパターン（再送用） : "0"：再送時正常返却
    処理結果 : "00"：正常
    応答結果 : "08"：取消済みエラー
    チケット代金 : 003500
    レスポンスパターン（取消再送用） : "0"：再送時正常返却
    ショップID : 30801
    """
    return '4000044902809'
def RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_02():
    data =  ResponseTotoTicketData(
        X_outou_kekka='02',
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4000044902809',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_02_RETRY():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4000044902809',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_02_CANCEL():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='01',
        X_outou_kekka='08',
        X_tc_dai='003500',
        X_shop_id='30801',
        X_haraikomi='4000044902809',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_02_CANCEL_RETRY():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='01',
        X_tc_dai='003500',
        X_shop_id='30801',
        X_haraikomi='4000044902809',
    )
    return COMPARE_TOTO_TICKET_DICT(data)

def BARCODE_TOTO_BUY_OUTOU_KEKKA_03():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "03"：取引停止中エラー
    チケット代金 : 003500
    チケット枚数 : 1
    レスポンスパターン（再送用） : "0"：再送時正常返却
    処理結果 : "00"：正常
    応答結果 : "99"：その他エラー
    チケット代金 : 003500
    レスポンスパターン（取消再送用） : "0"：再送時正常返却
    ショップID : 30801
    """
    return '4000065876882'
def RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_03():
    data =  ResponseTotoTicketData(
        X_outou_kekka='03',
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4000065876882',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_03_RETRY():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4000065876882',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_03_CANCEL():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='01',
        X_outou_kekka='99',
        X_tc_dai='003500',
        X_shop_id='30801',
        X_haraikomi='4000065876882',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_03_CANCEL_RETRY():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='01',
        X_tc_dai='003500',
        X_shop_id='30801',
        X_haraikomi='4000065876882',
    )
    return COMPARE_TOTO_TICKET_DICT(data)

def BARCODE_TOTO_BUY_OUTOU_KEKKA_05():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "05"：入金/発券中エラー
    チケット代金 : 003500
    チケット枚数 : 1
    レスポンスパターン（再送用） : "1"：再送時異常返却
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    チケット代金 : 003500
    レスポンスパターン（取消再送用） : "0"：再送時正常返却
    ショップID : 30801
    """
    return '4000086999447'
def RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_05():
    data =  ResponseTotoTicketData(
        X_outou_kekka='05',
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4000086999447',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_05_CANCEL():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='01',
        X_tc_dai='003500',
        X_shop_id='30801',
        X_haraikomi='4000086999447',
    )
    return COMPARE_TOTO_TICKET_DICT(data)

def BARCODE_TOTO_BUY_OUTOU_KEKKA_06():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "06"：入金/発券済みエラー
    チケット代金 : 003500
    チケット枚数 : 1
    レスポンスパターン（再送用） : "0"：再送時正常返却
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    チケット代金 : 003500
    レスポンスパターン（取消再送用） : "0"：再送時正常返却
    ショップID : 30801
    """
    return '4000107807126'
def RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_06():
    data =  ResponseTotoTicketData(
        X_outou_kekka='06',
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4000107807126',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_06_RETRY():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4000107807126',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_06_CANCEL():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='01',
        X_tc_dai='003500',
        X_shop_id='30801',
        X_haraikomi='4000107807126',
    )
    return COMPARE_TOTO_TICKET_DICT(data)

def BARCODE_TOTO_BUY_OUTOU_KEKKA_07():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "07"：入金/発券期限エラー
    チケット代金 : 003500
    チケット枚数 : 1
    レスポンスパターン（再送用） : "0"：再送時正常返却
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    チケット代金 : 003500
    レスポンスパターン（取消再送用） : "0"：再送時正常返却
    ショップID : 30801
    """
    return '4000128778641'
def RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_07():
    data =  ResponseTotoTicketData(
        X_outou_kekka='07',
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4000128778641',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_07_RETRY():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4000128778641',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_07_CANCEL():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='01',
        X_tc_dai='003500',
        X_shop_id='30801',
        X_haraikomi='4000128778641',
    )
    return COMPARE_TOTO_TICKET_DICT(data)

def BARCODE_TOTO_BUY_OUTOU_KEKKA_08():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "08"：取消済みエラー
    チケット代金 : 003500
    チケット枚数 : 1
    レスポンスパターン（再送用） : "1"：再送時異常返却
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    チケット代金 : 003500
    レスポンスパターン（取消再送用） : "0"：再送時正常返却
    ショップID : 30801
    """
    return '4000149914004'
def RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_08():
    data =  ResponseTotoTicketData(
        X_outou_kekka='08',
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4000149914004',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_08_CANCEL():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='01',
        X_tc_dai='003500',
        X_shop_id='30801',
        X_haraikomi='4000149914004',
    )
    return COMPARE_TOTO_TICKET_DICT(data)

def BARCODE_TOTO_BUY_OUTOU_KEKKA_99():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "99"：その他エラー
    チケット代金 : 003500
    チケット枚数 : 1
    レスポンスパターン（再送用） : "0"：再送時正常返却
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    チケット代金 : 003500
    レスポンスパターン（取消再送用） : "0"：再送時正常返却
    ショップID : 30801
    """
    return '4000170721688'
def RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_99():
    data =  ResponseTotoTicketData(
        X_outou_kekka='99',
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4000170721688',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_99_RETRY():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4000170721688',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_99_CANCEL():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='01',
        X_tc_dai='003500',
        X_shop_id='30801',
        X_haraikomi='4000170721688',
    )
    return COMPARE_TOTO_TICKET_DICT(data)


# ---------------------------
# スポーツ振興くじ マッピングNo2
# ---------------------------
def BARCODE_TOTO_VOTE_CASE_01():
    """
    正常系　払込票番号 生成時選択肢
    --------
    チケット代金 : 000000
    チケット枚数 : 1
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    券面情報データ※ : A
    投票券バーコード番号印字要否 : 印字する
    totoセンター応答結果 : 000000
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    totoセンター応答結果 : 000000
    """
    return '4002684354574'
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_01_BUY():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4002684354574',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_01_BUY_CANCEL():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4002684354574',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_01():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        tc_info_data='A',
        is_inji=True,
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_01_CANCEL():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        is_inji=True,
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)

def BARCODE_TOTO_VOTE_CASE_02():
    """
    正常系　払込票番号 生成時選択肢
    --------
    チケット代金 : 003500
    チケット枚数 : 2
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    券面情報データ※ : B
    投票券バーコード番号印字要否 : 印字しない
    totoセンター応答結果 : 000000
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    totoセンター応答結果 : 000000
    """
    return '4016106188814'
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_02_BUY():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='02',
        X_shop_id='30801',
        X_haraikomi='4016106188814',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_02_BUY_CANCEL():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='02',
        X_shop_id='30801',
        X_haraikomi='4016106188814',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_02():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='02',
        tc_info_data='B',
        is_inji=False,
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_02_CANCEL():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='02',
        is_inji=False,
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)

def BARCODE_TOTO_VOTE_CASE_03():
    """
    正常系　払込票番号 生成時選択肢
    --------
    チケット代金 : 010000
    チケット枚数 : 5
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    券面情報データ※ : C
    投票券バーコード番号印字要否 : 印字する
    totoセンター応答結果 : 000000
    処理結果 : "15"：タイムアウトエラー
    応答結果 : "00"：正常応答
    totoセンター応答結果 : 000000
    """
    return '4029527983371'
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_03_BUY():
    data =  ResponseTotoTicketData(
        X_tc_dai='010000',
        X_ticket_cnt='05',
        X_shop_id='30801',
        X_haraikomi='4029527983371',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_03_BUY_CANCEL():
    data =  ResponseTotoTicketData(
        X_tc_dai='010000',
        X_ticket_cnt='05',
        X_shop_id='30801',
        X_haraikomi='4029527983371',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_03():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='05',
        tc_info_data='C',
        is_inji=True,
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_03_CANCEL():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='05',
        is_inji=True,
        X_shori_kekka='15',
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)

def BARCODE_TOTO_VOTE_CASE_04():
    """
    正常系　払込票番号 生成時選択肢
    --------
    チケット代金 : 999999
    チケット枚数 : 1
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    券面情報データ※ : D
    投票券バーコード番号印字要否 : 印字しない
    totoセンター応答結果 : 000000
    処理結果 : "16"：SEJセンター混雑エラー
    応答結果 : "00"：正常応答
    totoセンター応答結果 : 000000
    """
    return '4034896755214'
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_04_BUY():
    data =  ResponseTotoTicketData(
        X_tc_dai='999999',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4034896755214',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_04_BUY_CANCEL():
    data =  ResponseTotoTicketData(
        X_tc_dai='999999',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4034896755214',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_04():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        tc_info_data='D',
        is_inji=False,
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_04_CANCEL():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        is_inji=False,
        X_shori_kekka='16',
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)

def BARCODE_TOTO_VOTE_CASE_05():
    """
    正常系　払込票番号 生成時選択肢
    --------
    チケット代金 : 000000
    チケット枚数 : 1
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    券面情報データ※ : E
    投票券バーコード番号印字要否 : 印字する
    totoセンター応答結果 : 000000
    処理結果 : "99"：その他エラー(400)
    応答結果 : "00"：正常応答
    totoセンター応答結果 : 000000
    """
    return '4002684522256'
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_05_BUY():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4002684522256',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_05_BUY_CANCEL():
    data =  ResponseTotoTicketData(
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4002684522256',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_05():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        tc_info_data='E',
        is_inji=True,
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_05_CANCEL():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        is_inji=True,
        X_shori_kekka='99',
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)

def BARCODE_TOTO_VOTE_CASE_06():
    """
    正常系　払込票番号 生成時選択肢
    --------
    チケット代金 : 003500
    チケット枚数 : 1
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    券面情報データ※ : F
    投票券バーコード番号印字要否 : 印字しない
    totoセンター応答結果 : 000000
    処理結果 : "99"：その他エラー(500)
    応答結果 : "00"：正常応答
    totoセンター応答結果 : 000000
    """
    return '4013422003210'
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_06_BUY():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4013422003210',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_06_BUY_CANCEL():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4013422003210',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_06():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        tc_info_data='F',
        is_inji=False,
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_06_CANCEL():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        is_inji=False,
        X_shori_kekka='99',
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)

def BARCODE_TOTO_VOTE_CASE_07():
    """
    正常系　払込票番号 生成時選択肢
    --------
    チケット代金 : 010000
    チケット枚数 : 2
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    券面情報データ※ : A
    投票券バーコード番号印字要否 : 印字する
    totoセンター応答結果 : 000000
    処理結果 : "00"：タイムアウト(正常)
    応答結果 : "00"：正常応答
    totoセンター応答結果 : 000000
    """
    return '4026843552014'
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_07_BUY():
    data =  ResponseTotoTicketData(
        X_tc_dai='010000',
        X_ticket_cnt='02',
        X_shop_id='30801',
        X_haraikomi='4026843552014',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_07_BUY_CANCEL():
    data =  ResponseTotoTicketData(
        X_tc_dai='010000',
        X_ticket_cnt='02',
        X_shop_id='30801',
        X_haraikomi='4026843552014',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_07():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='02',
        tc_info_data='A',
        is_inji=True,
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_07_CANCEL():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='02',
        is_inji=True,
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)

def BARCODE_TOTO_VOTE_CASE_08():
    """
    正常系　払込票番号 生成時選択肢
    --------
    チケット代金 : 049999
    チケット枚数 : 1
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    券面情報データ※ : A
    投票券バーコード番号印字要否 : 印字しない
    totoセンター応答結果 : 000000
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    totoセンター応答結果 : 000000
    """
    return '4045634048017'
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_08_BUY():
    data =  ResponseTotoTicketData(
        X_tc_dai='049999',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4045634048017',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_08_BUY_CANCEL():
    data =  ResponseTotoTicketData(
        X_tc_dai='049999',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4045634048017',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_08():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        tc_info_data='A',
        is_inji=False,
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_08_CANCEL():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        is_inji=False,
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)

def BARCODE_TOTO_VOTE_CASE_09():
    """
    正常系　払込票番号 生成時選択肢
    --------
    チケット代金 : 050000
    チケット枚数 : 1
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    券面情報データ※ : A
    投票券バーコード番号印字要否 : 印字しない
    totoセンター応答結果 : 000000
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    totoセンター応答結果 : 000000
    """
    return '4056371466255'
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_09_BUY():
    data =  ResponseTotoTicketData(
        X_tc_dai='050000',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4056371466255',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_09_BUY_CANCEL():
    data =  ResponseTotoTicketData(
        X_tc_dai='050000',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4056371466255',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_09():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        tc_info_data='A',
        is_inji=False,
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_09_CANCEL():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        is_inji=False,
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)

def BARCODE_TOTO_VOTE_SYORI_KEKKA_15():
    """
    正常系　払込票番号 生成時選択肢
    --------
    チケット代金 : 999999
    チケット枚数 : 5
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    処理結果 : "15"：タイムアウトエラー
    応答結果 : "00"：正常応答
    券面情報データ※ : A
    投票券バーコード番号印字要否 : 印字する
    totoセンター応答結果 : 000000
    処理結果 : "99"：タイムアウト(その他エラー500)
    応答結果 : "00"：正常応答
    totoセンター応答結果 : 000000
    """
    return '4040270568974'
def RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_15_BUY():
    data =  ResponseTotoTicketData(
        X_tc_dai='999999',
        X_ticket_cnt='05',
        X_shop_id='30801',
        X_haraikomi='4040270568974',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_15_BUY_CANCEL():
    data =  ResponseTotoTicketData(
        X_tc_dai='999999',
        X_ticket_cnt='05',
        X_shop_id='30801',
        X_haraikomi='4040270568974',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_15():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='05',
        X_shori_kekka='15',
        tc_info_data='A',
        is_inji=True,
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_15_CANCEL():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='05',
        is_inji=True,
        X_shori_kekka='99',
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)

def BARCODE_TOTO_VOTE_SYORI_KEKKA_16():
    """
    正常系　払込票番号 生成時選択肢
    --------
    チケット代金 : 003500
    チケット枚数 : 1
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    処理結果 : "16"：SEJセンター混雑エラー
    応答結果 : "00"：正常応答
    券面情報データ※ : A
    投票券バーコード番号印字要否 : 印字する
    totoセンター応答結果 : 000000
    処理結果 : "00"：正常
    応答結果 : "01"：検索キーエラー
    totoセンター応答結果 : 000000
    """
    return '4013432258655'
def RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_16_BUY():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4013432258655',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_16_BUY_CANCEL():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4013432258655',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_16():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        X_shori_kekka='16',
        tc_info_data='A',
        is_inji=True,
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_16_CANCEL():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        is_inji=True,
        X_outou_kekka='01',
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)

def BARCODE_TOTO_VOTE_SYORI_KEKKA_99_400():
    """
    正常系　払込票番号 生成時選択肢
    --------
    チケット代金 : 003500
    チケット枚数 : 1
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    処理結果 : "99"：その他エラー(400)
    応答結果 : "00"：正常応答
    券面情報データ※ : A
    投票券バーコード番号印字要否 : 印字する
    totoセンター応答結果 : 000000
    処理結果 : "00"：正常
    応答結果 : "04"：未払戻エラー
    totoセンター応答結果 : 000000
    """
    return '4013437501619'
def RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_99_400_BUY():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4013437501619',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_99_400_BUY_CANCEL():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4013437501619',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_99_400():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        X_shori_kekka='99',
        tc_info_data='A',
        is_inji=True,
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_99_400_CANCEL():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        is_inji=True,
        X_outou_kekka='04',
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)

def BARCODE_TOTO_VOTE_SYORI_KEKKA_99_500():
    """
    正常系　払込票番号 生成時選択肢
    --------
    チケット代金 : 003500
    チケット枚数 : 1
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    処理結果 : "99"：その他エラー(500)
    応答結果 : "00"：正常応答
    券面情報データ※ : A
    投票券バーコード番号印字要否 : 印字する
    totoセンター応答結果 : 000000
    処理結果 : "00"：正常
    応答結果 : "06"：入金/発券済みエラー
    totoセンター応答結果 : 000000
    """
    return '4013442744575'
def RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_99_500_BUY():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4013442744575',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_99_500_BUY_CANCEL():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4013442744575',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_99_500():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        X_shori_kekka='99',
        tc_info_data='A',
        is_inji=True,
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_99_500_CANCEL():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        is_inji=True,
        X_outou_kekka='06',
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)
def BARCODE_TOTO_VOTE_SYORI_KEKKA_TIMEOUT():
    """
    正常系　払込票番号 生成時選択肢
    --------
    チケット代金 : 003500
    チケット枚数 : 2
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    処理結果 : "00"：タイムアウト(正常)
    応答結果 : "00"：正常応答
    券面情報データ※ : A
    投票券バーコード番号印字要否 : 印字する
    totoセンター応答結果 : 000000
    処理結果 : "00"：正常
    応答結果 : "07"：入金/発券期限エラー
    totoセンター応答結果 : 000000
    """
    return '4016132342099'
def RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_TIMEOUT_BUY():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='02',
        X_shop_id='30801',
        X_haraikomi='4016132342099',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_TIMEOUT_BUY_CANCEL():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='02',
        X_shop_id='30801',
        X_haraikomi='4016132342099',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_TIMEOUT():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='02',
        tc_info_data='A',
        is_inji=True,
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_TIMEOUT_CANCEL():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='02',
        is_inji=True,
        X_outou_kekka='07',
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)

def BARCODE_TOTO_VOTE_SYORI_KEKKA_TIMEOUT_99():
    """
    正常系　払込票番号 生成時選択肢
    --------
    チケット代金 : 003500
    チケット枚数 : 5
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    処理結果 : "99"：タイムアウト(その他エラー500)
    応答結果 : "00"：正常応答
    券面情報データ※ : A
    投票券バーコード番号印字要否 : 印字する
    totoセンター応答結果 : 000000
    処理結果 : "00"：正常
    応答結果 : "08"：取消済みエラー
    totoセンター応答結果 : 000000
    """
    return '4018821939610'
def RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_TIMEOUT_99_BUY():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='05',
        X_shop_id='30801',
        X_haraikomi='4018821939610',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_TIMEOUT_99_BUY_CANCEL():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='05',
        X_shop_id='30801',
        X_haraikomi='4018821939610',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_TIMEOUT_99():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='05',
        X_shori_kekka='99',
        tc_info_data='A',
        is_inji=True,
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_TIMEOUT_99_CANCEL():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='05',
        is_inji=True,
        X_outou_kekka='08',
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)

def BARCODE_TOTO_VOTE_OUTOU_KEKKA_01():
    """
    正常系　払込票番号 生成時選択肢
    --------
    チケット代金 : 003500
    チケット枚数 : 1
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    処理結果 : "00"：正常
    応答結果 : "01"：検索キーエラー
    券面情報データ※ : A
    投票券バーコード番号印字要否 : 印字する
    totoセンター応答結果 : 000000
    処理結果 : "00"：正常
    応答結果 : "09"：取消期限エラー
    totoセンター応答結果 : 000000
    """
    return '4013422100971'
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_01_BUY():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4013422100971',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_01_BUY_CANCEL():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4013422100971',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_01():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        X_outou_kekka='01',
        tc_info_data='A',
        is_inji=True,
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_01_CANCEL():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        is_inji=True,
        X_outou_kekka='09',
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)

def BARCODE_TOTO_VOTE_OUTOU_KEKKA_04():
    """
    正常系　払込票番号 生成時選択肢
    --------
    チケット代金 : 003500
    チケット枚数 : 1
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    処理結果 : "00"：正常
    応答結果 : "04"：未払戻エラー
    券面情報データ※ : A
    投票券バーコード番号印字要否 : 印字する
    totoセンター応答結果 : 000000
    処理結果 : "00"：正常
    応答結果 : "11"：totoセンター接続エラー
    totoセンター応答結果 : 000001
    """
    return '4013422428778'
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_04_BUY():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4013422428778',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_04_BUY_CANCEL():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4013422428778',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_04():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        X_outou_kekka='04',
        tc_info_data='A',
        is_inji=True,
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_04_CANCEL():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        is_inji=True,
        X_outou_kekka='11',
        X_toto_kekka='000001',
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)

def BARCODE_TOTO_VOTE_OUTOU_KEKKA_06():
    """
    正常系　払込票番号 生成時選択肢
    --------
    チケット代金 : 003500
    チケット枚数 : 1
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    処理結果 : "00"：正常
    応答結果 : "06"：入金/発券済みエラー
    券面情報データ※ : A
    投票券バーコード番号印字要否 : 印字する
    totoセンター応答結果 : 000000
    処理結果 : "00"：正常
    応答結果 : "12"：totoセンター混雑エラー
    totoセンター応答結果 : 000001
    """
    return '4013422756536'
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_06_BUY():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4013422756536',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_06_BUY_CANCEL():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4013422756536',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_06():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        X_outou_kekka='06',
        tc_info_data='A',
        is_inji=True,
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_06_CANCEL():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        is_inji=True,
        X_outou_kekka='12',
        X_toto_kekka='000001',
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)

def BARCODE_TOTO_VOTE_OUTOU_KEKKA_07():
    """
    正常系　払込票番号 生成時選択肢
    --------
    チケット代金 : 003500
    チケット枚数 : 1
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    処理結果 : "00"：正常
    応答結果 : "07"：入金/発券期限エラー
    券面情報データ※ : A
    投票券バーコード番号印字要否 : 印字する
    totoセンター応答結果 : 000000
    処理結果 : "00"：正常
    応答結果 : "13"：totoセンターアプリエラー
    totoセンター応答結果 : 000001
    """
    return '4013423084294'
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_07_BUY():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4013423084294',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_07_BUY_CANCEL():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4013423084294',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_07():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        X_outou_kekka='07',
        tc_info_data='A',
        is_inji=True,
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_07_CANCEL():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        is_inji=True,
        X_outou_kekka='13',
        X_toto_kekka='000001',
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)

def BARCODE_TOTO_VOTE_OUTOU_KEKKA_08():
    """
    正常系　払込票番号 生成時選択肢
    --------
    チケット代金 : 003500
    チケット枚数 : 1
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    処理結果 : "00"：正常
    応答結果 : "08"：取消済みエラー
    券面情報データ※ : A
    投票券バーコード番号印字要否 : 印字する
    totoセンター応答結果 : 000000
    処理結果 : "00"：正常
    応答結果 : "14"：totoセンター通信その他エラー
    totoセンター応答結果 : 000001
    """
    return '4013423412059'
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_08_BUY():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4013423412059',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_08_BUY_CANCEL():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4013423412059',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_08():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        X_outou_kekka='08',
        tc_info_data='A',
        is_inji=True,
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_08_CANCEL():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        is_inji=True,
        X_outou_kekka='14',
        X_toto_kekka='000001',
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)

def BARCODE_TOTO_VOTE_OUTOU_KEKKA_11():
    """
    正常系　払込票番号 生成時選択肢
    --------
    チケット代金 : 003500
    チケット枚数 : 1
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    処理結果 : "00"：正常
    応答結果 : "11"：totoセンター接続エラー
    券面情報データ※ : A
    投票券バーコード番号印字要否 : 印字する
    totoセンター応答結果 : 000000
    処理結果 : "00"：正常
    応答結果 : "99"：その他エラー
    totoセンター応答結果 : 000000
    """
    return '4013423739774'
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_11_BUY():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4013423739774',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_11_BUY_CANCEL():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4013423739774',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_11():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        X_outou_kekka='11',
        tc_info_data='A',
        is_inji=True,
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_11_CANCEL():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        is_inji=True,
        X_outou_kekka='99',
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)

def BARCODE_TOTO_VOTE_OUTOU_KEKKA_12():
    """
    正常系　払込票番号 生成時選択肢
    --------
    チケット代金 : 003500
    チケット枚数 : 1
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    処理結果 : "00"：正常
    応答結果 : "12"：totoセンター混雑エラー
    券面情報データ※ : A
    投票券バーコード番号印字要否 : 印字する
    totoセンター応答結果 : 000001
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    totoセンター応答結果 : 000000
    """
    return '4013424076816'
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_12_BUY():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4013424076816',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_12_BUY_CANCEL():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4013424076816',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_12():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        X_outou_kekka='12',
        tc_info_data='A',
        is_inji=True,
        X_toto_kekka='000001',
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_12_CANCEL():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        is_inji=True,
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)

def BARCODE_TOTO_VOTE_OUTOU_KEKKA_13():
    """
    正常系　払込票番号 生成時選択肢
    --------
    チケット代金 : 003500
    チケット枚数 : 1
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    処理結果 : "00"：正常
    応答結果 : "13"：totoセンターアプリエラー
    券面情報データ※ : A
    投票券バーコード番号印字要否 : 印字する
    totoセンター応答結果 : 000001
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    totoセンター応答結果 : 000000
    """
    return '4013424404497'
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_13_BUY():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4013424404497',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_13_BUY_CANCEL():
    data =  ResponseTotoTicketData(
        X_tc_dai='003500',
        X_ticket_cnt='01',
        X_shop_id='30801',
        X_haraikomi='4013424404497',
    )
    return COMPARE_TOTO_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_13():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        X_outou_kekka='13',
        tc_info_data='A',
        is_inji=True,
        X_toto_kekka='000001',
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_13_CANCEL():
    data =  ResponseTotoTicketVoteData(
        X_ticket_cnt='01',
        is_inji=True,
        X_shop_id='30801',
    )
    return COMPARE_TOTO_TICKET_VOTE_DICT(data)

# ---------------------------
# スポーツ振興くじ マッピングNo3
# ---------------------------
def BARCODE_TOTO_REPAY_CASE_01():
    """
    払戻受付票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    払戻金額 : 0000000000
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    払戻金額 : 9999999999
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    ショップID : 00000
    """
    return '9000000000988'
def RESPONSE_TICKET_DATA_TOTO_REPAY_CASE_01():
    data =  ResponseTotoTicketRepayData(
        X_haraimodoshi='9000000000988',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_CASE_01_CANCEL():
    data =  ResponseTotoTicketRepayData(
        X_payback_amt='9999999999',
        X_haraimodoshi='9000000000988',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)

def BARCODE_TOTO_REPAY_CASE_02():
    """
    払戻受付票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    払戻金額 : 0000003500
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    払戻金額 : 0000000000
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    ショップID : 30514
    """
    return '9000000163904'
def RESPONSE_TICKET_DATA_TOTO_REPAY_CASE_02():
    data =  ResponseTotoTicketRepayData(
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000000163904',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_CASE_02_CANCEL():
    data =  ResponseTotoTicketRepayData(
        X_shop_id='30514',
        X_haraimodoshi='9000000163904',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)

def BARCODE_TOTO_REPAY_CASE_03():
    """
    払戻受付票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    払戻金額 : 0000005000
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    処理結果 : "16"：SEJセンター混雑エラー
    応答結果 : "00"：正常応答
    払戻金額 : 0000003500
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    ショップID : 30801
    """
    return '9000000338340'
def RESPONSE_TICKET_DATA_TOTO_REPAY_CASE_03():
    data =  ResponseTotoTicketRepayData(
        X_payback_amt='0000005000',
        X_shop_id='30801',
        X_haraimodoshi='9000000338340',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_CASE_03_CANCEL():
    data =  ResponseTotoTicketRepayData(
        X_shori_kekka='16',
        X_payback_amt='0000003500',
        X_shop_id='30801',
        X_haraimodoshi='9000000338340',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_CASE_03_CANCEL_RETRY():
    data =  ResponseTotoTicketRepayData(
        X_payback_amt='0000003500',
        X_shop_id='30801',
        X_haraimodoshi='9000000338340',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)

def BARCODE_TOTO_REPAY_CASE_04():
    """
    払戻受付票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    払戻金額 : 9999999999
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    処理結果 : "99"：その他エラー(400)
    応答結果 : "00"：正常応答
    払戻金額 : 0000005000
    レスポンスパターン（再送用） : "1"：再送時処理結果が異常
    ショップID : 99999
    """
    return '9000000512948'
def RESPONSE_TICKET_DATA_TOTO_REPAY_CASE_04():
    data =  ResponseTotoTicketRepayData(
        X_payback_amt='9999999999',
        X_shop_id='99999',
        X_haraimodoshi='9000000512948',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_CASE_04_CANCEL():
    data =  ResponseTotoTicketRepayData(
        X_shori_kekka='99',
        X_payback_amt='0000005000',
        X_shop_id='99999',
        X_haraimodoshi='9000000512948',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)

def BARCODE_TOTO_REPAY_SYORI_KEKKA_14():
    """
    払戻受付票番号 生成時選択肢
    --------
    処理結果 : "14"：サービス時間帯エラー
    応答結果 : "00"：正常応答
    払戻金額 : 0000003500
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    処理結果 : "99"：その他エラー(500)
    応答結果 : "00"：正常応答
    払戻金額 : 9999999999
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    ショップID : 30514
    """
    return '9000010681344'
def RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_14():
    data =  ResponseTotoTicketRepayData(
        X_shori_kekka='14',
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000010681344',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_14_RETRY():
    data =  ResponseTotoTicketRepayData(
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000010681344',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_14_CANCEL():
    data =  ResponseTotoTicketRepayData(
        X_shori_kekka='99',
        X_payback_amt='9999999999',
        X_shop_id='30514',
        X_haraimodoshi='9000010681344',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_14_CANCEL_RETRY():
    data =  ResponseTotoTicketRepayData(
        X_payback_amt='9999999999',
        X_shop_id='30514',
        X_haraimodoshi='9000010681344',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)

def BARCODE_TOTO_REPAY_SYORI_KEKKA_16():
    """
    払戻受付票番号 生成時選択肢
    --------
    処理結果 : "16"：SEJセンター混雑エラー
    応答結果 : "00"：正常応答
    払戻金額 : 0000003500
    レスポンスパターン（再送用） : "1"：再送時処理結果が異常
    処理結果 : "00"：タイムアウト(正常)
    応答結果 : "00"：正常応答
    払戻金額 : 0000000000
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    ショップID : 30514
    """
    return '9000021258306'
def RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_16():
    data =  ResponseTotoTicketRepayData(
        X_shori_kekka='16',
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000021258306',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_16_CANCEL():
    data =  ResponseTotoTicketRepayData(
        X_shop_id='30514',
        X_haraimodoshi='9000021258306',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)

def BARCODE_TOTO_REPAY_SYORI_KEKKA_99_400():
    """
    払戻受付票番号 生成時選択肢
    --------
    処理結果 : "99"：その他エラー(400)
    応答結果 : "00"：正常応答
    払戻金額 : 0000003500
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    処理結果 : "99"：タイムアウト(その他エラー500)
    応答結果 : "00"：正常応答
    払戻金額 : 0000003500
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    ショップID : 30514
    """
    return '9000031672703'
def RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_99_400():
    data =  ResponseTotoTicketRepayData(
        X_shori_kekka='99',
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000031672703',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_99_400_RETRY():
    data =  ResponseTotoTicketRepayData(
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000031672703',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_99_400_CANCEL():
    data =  ResponseTotoTicketRepayData(
        X_shori_kekka='99',
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000031672703',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_99_400_CANCEL_RETRY():
    data =  ResponseTotoTicketRepayData(
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000031672703',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)

def BARCODE_TOTO_REPAY_SYORI_KEKKA_99_500():
    """
    払戻受付票番号 生成時選択肢
    --------
    処理結果 : "99"：その他エラー(500)
    応答結果 : "00"：正常応答
    払戻金額 : 0000003500
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    払戻金額 : 0000005000
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    ショップID : 30514
    """
    return '9000042107584'
def RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_99_500():
    data =  ResponseTotoTicketRepayData(
        X_shori_kekka='99',
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000042107584',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_99_500_RETRY():
    data =  ResponseTotoTicketRepayData(
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000042107584',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_99_500_CANCEL():
    data =  ResponseTotoTicketRepayData(
        X_payback_amt='0000005000',
        X_shop_id='30514',
        X_haraimodoshi='9000042107584',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)

def BARCODE_TOTO_REPAY_SYORI_KEKKA_TIMEOUT():
    """
    払戻受付票番号 生成時選択肢
    --------
    処理結果 : "00"：タイムアウト(正常)
    応答結果 : "00"：正常応答
    払戻金額 : 0000003500
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    処理結果 : "00"：正常
    応答結果 : "04"：未払戻エラー
    払戻金額 : 9999999999
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    ショップID : 30514
    """
    return '9000052594947'
def RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_TIMEOUT():
    data =  ResponseTotoTicketRepayData(
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000052594947',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_TIMEOUT_CANCEL():
    data =  ResponseTotoTicketRepayData(
        X_outou_kekka='04',
        X_payback_amt='9999999999',
        X_shop_id='30514',
        X_haraimodoshi='9000052594947',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_TIMEOUT_CANCEL_RETRY():
    data =  ResponseTotoTicketRepayData(
        X_payback_amt='9999999999',
        X_shop_id='30514',
        X_haraimodoshi='9000052594947',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)

def BARCODE_TOTO_REPAY_SYORI_KEKKA_TIMEOUT_99():
    """
    払戻受付票番号 生成時選択肢
    --------
    処理結果 : "99"：タイムアウト(その他エラー500)
    応答結果 : "00"：正常応答
    払戻金額 : 0000003500
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    処理結果 : "00"：正常
    応答結果 : "06"：払戻済エラー
    払戻金額 : 0000000000
    レスポンスパターン（再送用） : "1"：再送時処理結果が異常
    ショップID : 30514
    """
    return '9000063081184'
def RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_TIMEOUT_99():
    data =  ResponseTotoTicketRepayData(
        X_shori_kekka='99',
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000063081184',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_TIMEOUT_99_RETRY():
    data =  ResponseTotoTicketRepayData(
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000063081184',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_TIMEOUT_99_CANCEL():
    data =  ResponseTotoTicketRepayData(
        X_outou_kekka='06',
        X_shop_id='30514',
        X_haraimodoshi='9000063081184',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)

def BARCODE_TOTO_REPAY_OUTOU_KEKKA_01():
    """
    払戻受付票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "01"：検索キーエラー
    払戻金額 : 0000003500
    レスポンスパターン（再送用） : "1"：再送時処理結果が異常
    処理結果 : "00"：正常
    応答結果 : "07"：払戻期限切れエラー
    払戻金額 : 0000003500
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    ショップID : 30514
    """
    return '9000000905344'
def RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_01():
    data =  ResponseTotoTicketRepayData(
        X_outou_kekka='01',
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000000905344',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_01_CANCEL():
    data =  ResponseTotoTicketRepayData(
        X_outou_kekka='07',
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000000905344',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_01_CANCEL_RETRY():
    data =  ResponseTotoTicketRepayData(
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000000905344',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def BARCODE_TOTO_REPAY_OUTOU_KEKKA_02():
    """
    払戻受付票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "02"：店舗チェックエラー
    払戻金額 : 0000003500
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    処理結果 : "00"：正常
    応答結果 : "08"：取消済みエラー
    払戻金額 : 0000005000
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    ショップID : 30514
    """
    return '9000001480383'
def RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_02():
    data =  ResponseTotoTicketRepayData(
        X_outou_kekka='02',
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000001480383',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_02_RETRY():
    data =  ResponseTotoTicketRepayData(
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000001480383',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_02_CANCEL():
    data =  ResponseTotoTicketRepayData(
        X_outou_kekka='08',
        X_payback_amt='0000005000',
        X_shop_id='30514',
        X_haraimodoshi='9000001480383',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_02_CANCEL_RETRY():
    data =  ResponseTotoTicketRepayData(
        X_payback_amt='0000005000',
        X_shop_id='30514',
        X_haraimodoshi='9000001480383',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)

def BARCODE_TOTO_REPAY_OUTOU_KEKKA_03():
    """
    払戻受付票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "03"：取引停止中エラー
    払戻金額 : 0000003500
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    処理結果 : "00"：正常
    応答結果 : "99"：その他エラー
    払戻金額 : 9999999999
    レスポンスパターン（再送用） : "1"：再送時処理結果が異常
    ショップID : 30514
    """
    return '9000002137507'
def RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_03():
    data =  ResponseTotoTicketRepayData(
        X_outou_kekka='03',
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000002137507',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_03_RETRY():
    data =  ResponseTotoTicketRepayData(
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000002137507',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_03_CANCEL():
    data =  ResponseTotoTicketRepayData(
        X_outou_kekka='99',
        X_payback_amt='9999999999',
        X_shop_id='30514',
        X_haraimodoshi='9000002137507',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)

def BARCODE_TOTO_REPAY_OUTOU_KEKKA_05():
    """
    払戻受付票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "05"：払戻中エラー
    払戻金額 : 0000003500
    レスポンスパターン（再送用） : "1"：再送時処理結果が異常
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    払戻金額 : 0000000000
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    ショップID : 30514
    """
    return '9000002867268'
def RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_05():
    data =  ResponseTotoTicketRepayData(
        X_outou_kekka='05',
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000002867268',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_05_CANCEL():
    data =  ResponseTotoTicketRepayData(
        X_shop_id='30514',
        X_haraimodoshi='9000002867268',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)

def BARCODE_TOTO_REPAY_OUTOU_KEKKA_06():
    """
    払戻受付票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "06"：払戻済エラー
    払戻金額 : 0000003500
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    払戻金額 : 0000003500
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    ショップID : 30514
    """
    return '9000003441023'
def RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_06():
    data =  ResponseTotoTicketRepayData(
        X_outou_kekka='06',
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000003441023',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_06_RETRY():
    data =  ResponseTotoTicketRepayData(
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000003441023',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_06_CANCEL():
    data =  ResponseTotoTicketRepayData(
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000003441023',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)

def BARCODE_TOTO_REPAY_OUTOU_KEKKA_07():
    """
    払戻受付票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "07"：払戻期限切れエラー
    払戻金額 : 0000003500
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    払戻金額 : 0000005000
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    ショップID : 30514
    """
    return '9000004096703'
def RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_07():
    data =  ResponseTotoTicketRepayData(
        X_outou_kekka='07',
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000004096703',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_07_RETRY():
    data =  ResponseTotoTicketRepayData(
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000004096703',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_07_CANCEL():
    data =  ResponseTotoTicketRepayData(
        X_payback_amt='0000005000',
        X_shop_id='30514',
        X_haraimodoshi='9000004096703',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)

def BARCODE_TOTO_REPAY_OUTOU_KEKKA_08():
    """
    払戻受付票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "08"：取消済みエラー
    払戻金額 : 0000003500
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    払戻金額 : 9999999999
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    ショップID : 30514
    """
    return '9000004752388'
def RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_08():
    data =  ResponseTotoTicketRepayData(
        X_outou_kekka='08',
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000004752388',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_08_RETRY():
    data =  ResponseTotoTicketRepayData(
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000004752388',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_08_CANCEL():
    data =  ResponseTotoTicketRepayData(
        X_payback_amt='9999999999',
        X_shop_id='30514',
        X_haraimodoshi='9000004752388',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)

def BARCODE_TOTO_REPAY_OUTOU_KEKKA_99():
    """
    払戻受付票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "99"：その他エラー
    払戻金額 : 0000003500
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    払戻金額 : 0000000000
    レスポンスパターン（再送用） : "0"：再送時処理結果が正常
    ショップID : 30514
    """
    return '9000005406785'
def RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_99():
    data =  ResponseTotoTicketRepayData(
        X_outou_kekka='99',
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000005406785',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_99_RETRY():
    data =  ResponseTotoTicketRepayData(
        X_payback_amt='0000003500',
        X_shop_id='30514',
        X_haraimodoshi='9000005406785',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_99_CANCEL():
    data =  ResponseTotoTicketRepayData(
        X_shop_id='30514',
        X_haraimodoshi='9000005406785',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)


# ---------------------------
# スポーツ振興くじ マッピングNo4
# ---------------------------
def BARCODE_TOTO_CLEARING_CASE_01():
    """
    正常系　払込票番号 生成時選択肢
    --------
    払戻金額 : 0000000000
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    払戻金額 : 9999999999
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    totoセンター応答結果 : 空タグ
    """
    return '9000000061477'
def RESPONSE_TICKET_DATA_TOTO_CLEARING_CASE_01_REPAY():
    data =  ResponseTotoTicketClearingData(
        X_haraimodoshi='9000000061477',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_CASE_01_REPAY_CANCEL():
    data =  ResponseTotoTicketClearingData(
        X_payback_amt='9999999999',
        X_haraimodoshi='9000000061477',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_CASE_01():
    data =  ResponseTotoTicketClearingData()
    return COMPARE_TOTO_TICKET_CLEARING_DICT(data)

def BARCODE_TOTO_CLEARING_CASE_02():
    """
    正常系　払込票番号 生成時選択肢
    --------
    払戻金額 : 0000003500
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    払戻金額 : 0000000000
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    totoセンター応答結果 : 000000
    """
    return '9000005242956'
def RESPONSE_TICKET_DATA_TOTO_CLEARING_CASE_02_REPAY():
    data =  ResponseTotoTicketClearingData(
        X_payback_amt='0000003500',
        X_haraimodoshi='9000005242956',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_CASE_02_REPAY_CANCEL():
    data =  ResponseTotoTicketClearingData(
        X_haraimodoshi='9000005242956',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_CASE_02():
    data =  ResponseTotoTicketClearingData(
        X_toto_kekka='000000',
    )
    return COMPARE_TOTO_TICKET_CLEARING_DICT(data)

def BARCODE_TOTO_CLEARING_CASE_03():
    """
    正常系　払込票番号 生成時選択肢
    --------
    払戻金額 : 0000005000
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    払戻金額 : 0000003500
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    totoセンター応答結果 : 000001
    """
    return '9000010506357'
def RESPONSE_TICKET_DATA_TOTO_CLEARING_CASE_03_REPAY():
    data =  ResponseTotoTicketClearingData(
        X_payback_amt='0000005000',
        X_haraimodoshi='9000010506357',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_CASE_03_REPAY_CANCEL():
    data =  ResponseTotoTicketClearingData(
        X_payback_amt='0000003500',
        X_haraimodoshi='9000010506357',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_CASE_03():
    data =  ResponseTotoTicketClearingData(
        X_toto_kekka='000001',
    )
    return COMPARE_TOTO_TICKET_CLEARING_DICT(data)

def BARCODE_TOTO_CLEARING_CASE_04():
    """
    正常系　払込票番号 生成時選択肢
    --------
    払戻金額 : 9999999999
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    払戻金額 : 0000005000
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    totoセンター応答結果 : 000002
    """
    return '9000015769757'
def RESPONSE_TICKET_DATA_TOTO_CLEARING_CASE_04_REPAY():
    data =  ResponseTotoTicketClearingData(
        X_payback_amt='9999999999',
        X_haraimodoshi='9000015769757',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_CASE_04_REPAY_CANCEL():
    data =  ResponseTotoTicketClearingData(
        X_payback_amt='0000005000',
        X_haraimodoshi='9000015769757',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_CASE_04():
    data =  ResponseTotoTicketClearingData(
        X_toto_kekka='000002',
    )
    return COMPARE_TOTO_TICKET_CLEARING_DICT(data)

def BARCODE_TOTO_CLEARING_SYORI_KEKKA_15():
    """
    正常系　払込票番号 生成時選択肢
    --------
    払戻金額 : 0000003500
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    払戻金額 : 9999999999
    処理結果 : "15"：タイムアウトエラー
    応答結果 : "00"：正常応答
    totoセンター応答結果 : 空タグ
    """
    return '9000005306917'
def RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_15_REPAY():
    data =  ResponseTotoTicketClearingData(
        X_payback_amt='0000003500',
        X_haraimodoshi='9000005306917',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_15_REPAY_CANCEL():
    data =  ResponseTotoTicketClearingData(
        X_payback_amt='9999999999',
        X_haraimodoshi='9000005306917',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_15():
    data =  ResponseTotoTicketClearingData(
        X_shori_kekka='15',
    )
    return COMPARE_TOTO_TICKET_CLEARING_DICT(data)

def BARCODE_TOTO_CLEARING_SYORI_KEKKA_16():
    """
    正常系　払込票番号 生成時選択肢
    --------
    払戻金額 : 0000005000
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    払戻金額 : 0000003500
    処理結果 : "16"：SEJセンター混雑エラー
    応答結果 : "00"：正常応答
    totoセンター応答結果 : 空タグ
    """
    return '9000010511399'
def RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_16_REPAY():
    data =  ResponseTotoTicketClearingData(
        X_payback_amt='0000005000',
        X_haraimodoshi='9000010511399',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_16_REPAY_CANCEL():
    data =  ResponseTotoTicketClearingData(
        X_payback_amt='0000003500',
        X_haraimodoshi='9000010511399',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_16():
    data =  ResponseTotoTicketClearingData(
        X_shori_kekka='16',
    )
    return COMPARE_TOTO_TICKET_CLEARING_DICT(data)

def BARCODE_TOTO_CLEARING_SYORI_KEKKA_99():
    """
    正常系　払込票番号 生成時選択肢
    --------
    払戻金額 : 9999999999
    処理結果 : "16"：SEJセンター混雑エラー
    応答結果 : "00"：正常応答
    払戻金額 : 0000003500
    処理結果 : "99"：その他エラー(400)
    応答結果 : "00"：正常応答
    totoセンター応答結果 : 空タグ
    """
    return '9000016412195'
def RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_99_REPAY():
    data =  ResponseTotoTicketClearingData(
        X_payback_amt='9999999999',
        X_haraimodoshi='9000016412195',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_99_REPAY_CANCEL():
    data =  ResponseTotoTicketClearingData(
        X_shori_kekka='16',
        X_payback_amt='0000003500',
        X_haraimodoshi='9000016412195',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_99():
    data =  ResponseTotoTicketClearingData(
        X_shori_kekka='99',
    )
    return COMPARE_TOTO_TICKET_CLEARING_DICT(data)

def BARCODE_TOTO_CLEARING_SYORI_KEKKA_99():
    """
    正常系　払込票番号 生成時選択肢
    --------
    払戻金額 : 0000003500
    処理結果 : "99"：その他エラー(400)
    応答結果 : "00"：正常応答
    払戻金額 : 0000003500
    処理結果 : "99"：その他エラー(500)
    応答結果 : "00"：正常応答
    totoセンター応答結果 : 空タグ
    """
    return '9000006584352'
def RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_99_REPAY():
    data =  ResponseTotoTicketClearingData(
        X_payback_amt='0000003500',
        X_haraimodoshi='9000006584352',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_99_REPAY_CANCEL():
    data =  ResponseTotoTicketClearingData(
        X_shori_kekka='99',
        X_payback_amt='0000003500',
        X_haraimodoshi='9000006584352',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_99():
    data =  ResponseTotoTicketClearingData(
        X_shori_kekka='99',
    )
    return COMPARE_TOTO_TICKET_CLEARING_DICT(data)

def BARCODE_TOTO_CLEARING_SYORI_KEKKA_TIMEOUT():
    """
    正常系　払込票番号 生成時選択肢
    --------
    払戻金額 : 0000005000
    処理結果 : "99"：その他エラー(500)
    応答結果 : "00"：正常応答
    払戻金額 : 0000003500
    処理結果 : "00"：タイムアウト(正常)
    応答結果 : "00"：正常応答
    totoセンター応答結果 : 空タグ
    """
    return '9000012485155'
def RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_TIMEOUT_REPAY():
    data =  ResponseTotoTicketClearingData(
        X_payback_amt='0000005000',
        X_haraimodoshi='9000012485155',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_TIMEOUT_REPAY_CANCEL():
    data =  ResponseTotoTicketClearingData(
        X_shori_kekka='99',
        X_payback_amt='0000003500',
        X_haraimodoshi='9000012485155',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_TIMEOUT():
    data =  ResponseTotoTicketClearingData()
    return COMPARE_TOTO_TICKET_CLEARING_DICT(data)

def BARCODE_TOTO_CLEARING_SYORI_KEKKA_TIMEOUT_99():
    """
    正常系　払込票番号 生成時選択肢
    --------
    払戻金額 : 9999999999
    処理結果 : "00"：タイムアウト(正常)
    応答結果 : "00"：正常応答
    払戻金額 : 0000003500
    処理結果 : "99"：タイムアウト(その他エラー500)
    応答結果 : "00"：正常応答
    totoセンター応答結果 : 空タグ
    """
    return '9000018385954'
def RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_TIMEOUT_99_REPAY():
    data =  ResponseTotoTicketClearingData(
        X_payback_amt='9999999999',
        X_haraimodoshi='9000018385954',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_TIMEOUT_99_REPAY_CANCEL():
    data =  ResponseTotoTicketClearingData(
        X_payback_amt='0000003500',
        X_haraimodoshi='9000018385954',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_TIMEOUT_99():
    data =  ResponseTotoTicketClearingData(
        X_shori_kekka='99',
    )
    return COMPARE_TOTO_TICKET_CLEARING_DICT(data)

def BARCODE_TOTO_CLEARING_OUTOU_KEKKA_00():
    """
    正常系　払込票番号 生成時選択肢
    --------
    払戻金額 : 0000003500
    処理結果 : "99"：タイムアウト(その他エラー500)
    応答結果 : "00"：正常応答
    払戻金額 : 0000003500
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    totoセンター応答結果 : 空タグ
    """
    return '9000008540196'
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_00_REPAY():
    data =  ResponseTotoTicketClearingData(
        X_payback_amt='0000003500',
        X_haraimodoshi='9000008540196',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_00_REPAY_CANCEL():
    data =  ResponseTotoTicketClearingData(
        X_shori_kekka='99',
        X_payback_amt='0000003500',
        X_haraimodoshi='9000008540196',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_00():
    data =  ResponseTotoTicketClearingData()
    return COMPARE_TOTO_TICKET_CLEARING_DICT(data)

def BARCODE_TOTO_CLEARING_OUTOU_KEKKA_01():
    """
    正常系　払込票番号 生成時選択肢
    --------
    払戻金額 : 0000005000
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    払戻金額 : 0000003500
    処理結果 : "00"：正常
    応答結果 : "01"：検索キーエラー
    totoセンター応答結果 : 空タグ
    """
    return '9000010506432'
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_01_REPAY():
    data =  ResponseTotoTicketClearingData(
        X_payback_amt='0000005000',
        X_haraimodoshi='9000010506432',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_01_REPAY_CANCEL():
    data =  ResponseTotoTicketClearingData(
        X_payback_amt='0000003500',
        X_haraimodoshi='9000010506432',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_01():
    data =  ResponseTotoTicketClearingData(
        X_outou_kekka='01',
    )
    return COMPARE_TOTO_TICKET_CLEARING_DICT(data)

def BARCODE_TOTO_CLEARING_OUTOU_KEKKA_04():
    """
    正常系　払込票番号 生成時選択肢
    --------
    払戻金額 : 9999999999
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    払戻金額 : 0000003500
    処理結果 : "00"：正常
    応答結果 : "04"：未払戻エラー
    totoセンター応答結果 : 空タグ
    """
    return '9000015749476'
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_04_REPAY():
    data =  ResponseTotoTicketClearingData(
        X_payback_amt='9999999999',
        X_haraimodoshi='9000015749476',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_04_REPAY_CANCEL():
    data =  ResponseTotoTicketClearingData(
        X_payback_amt='0000003500',
        X_haraimodoshi='9000015749476',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_04():
    data =  ResponseTotoTicketClearingData(
        X_outou_kekka='04',
    )
    return COMPARE_TOTO_TICKET_CLEARING_DICT(data)

def BARCODE_TOTO_CLEARING_OUTOU_KEKKA_06():
    """
    正常系　払込票番号 生成時選択肢
    --------
    払戻金額 : 0000003500
    処理結果 : "00"：正常
    応答結果 : "04"：未払戻エラー
    払戻金額 : 0000003500
    処理結果 : "00"：正常
    応答結果 : "06"：払戻済エラー
    totoセンター応答結果 : 空タグ
    """
    return '9000005345794'
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_06_REPAY():
    data =  ResponseTotoTicketClearingData(
        X_payback_amt='0000003500',
        X_haraimodoshi='9000005345794',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_06_REPAY_CANCEL():
    data =  ResponseTotoTicketClearingData(
        X_outou_kekka='04',
        X_payback_amt='0000003500',
        X_haraimodoshi='9000005345794',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_06():
    data =  ResponseTotoTicketClearingData(
        X_outou_kekka='06',
    )
    return COMPARE_TOTO_TICKET_CLEARING_DICT(data)

def BARCODE_TOTO_CLEARING_OUTOU_KEKKA_07():
    """
    正常系　払込票番号 生成時選択肢
    --------
    払戻金額 : 0000005000
    処理結果 : "00"：正常
    応答結果 : "06"：払戻済エラー
    払戻金額 : 0000003500
    処理結果 : "00"：正常
    応答結果 : "07"：払戻期限切れエラー
    totoセンター応答結果 : 空タグ
    """
    return '9000010670751'
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_07_REPAY():
    data =  ResponseTotoTicketClearingData(
        X_payback_amt='0000005000',
        X_haraimodoshi='9000010670751',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_07_REPAY_CANCEL():
    data =  ResponseTotoTicketClearingData(
        X_outou_kekka='06',
        X_payback_amt='0000003500',
        X_haraimodoshi='9000010670751',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_07():
    data =  ResponseTotoTicketClearingData(
        X_outou_kekka='07',
    )
    return COMPARE_TOTO_TICKET_CLEARING_DICT(data)

def BARCODE_TOTO_CLEARING_OUTOU_KEKKA_08():
    """
    正常系　払込票番号 生成時選択肢
    --------
    払戻金額 : 9999999999
    処理結果 : "00"：正常
    応答結果 : "07"：払戻期限切れエラー
    払戻金額 : 0000003500
    処理結果 : "00"：正常
    応答結果 : "08"：取消済みエラー
    totoセンター応答結果 : 空タグ
    """
    return '9000015995712'
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_08_REPAY():
    data =  ResponseTotoTicketClearingData(
        X_payback_amt='9999999999',
        X_haraimodoshi='9000015995712',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_08_REPAY_CANCEL():
    data =  ResponseTotoTicketClearingData(
        X_outou_kekka='07',
        X_payback_amt='0000003500',
        X_haraimodoshi='9000015995712',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_08():
    data =  ResponseTotoTicketClearingData(
        X_outou_kekka='08',
    )
    return COMPARE_TOTO_TICKET_CLEARING_DICT(data)

def BARCODE_TOTO_CLEARING_OUTOU_KEKKA_11():
    """
    正常系　払込票番号 生成時選択肢
    --------
    払戻金額 : 0000003500
    処理結果 : "00"：正常
    応答結果 : "08"：取消済みエラー
    払戻金額 : 0000003500
    処理結果 : "00"：正常
    応答結果 : "11"：totoセンター接続エラー
    totoセンター応答結果 : 空タグ
    """
    return '9000005592037'
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_11_REPAY():
    data =  ResponseTotoTicketClearingData(
        X_payback_amt='0000003500',
        X_haraimodoshi='9000005592037',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_11_REPAY_CANCEL():
    data =  ResponseTotoTicketClearingData(
        X_outou_kekka='08',
        X_payback_amt='0000003500',
        X_haraimodoshi='9000005592037',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_11():
    data =  ResponseTotoTicketClearingData(
        X_outou_kekka='11',
    )
    return COMPARE_TOTO_TICKET_CLEARING_DICT(data)

def BARCODE_TOTO_CLEARING_OUTOU_KEKKA_12():
    """
    正常系　払込票番号 生成時選択肢
    --------
    払戻金額 : 0000005000
    処理結果 : "00"：正常
    応答結果 : "99"：その他エラー
    払戻金額 : 0000003500
    処理結果 : "00"：正常
    応答結果 : "12"：totoセンター混雑エラー
    totoセンター応答結果 : 000000
    """
    return '9000010917030'
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_12_REPAY():
    data =  ResponseTotoTicketClearingData(
        X_payback_amt='0000005000',
        X_haraimodoshi='9000010917030',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_12_REPAY_CANCEL():
    data =  ResponseTotoTicketClearingData(
        X_outou_kekka='99',
        X_payback_amt='0000003500',
        X_haraimodoshi='9000010917030',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_12():
    data =  ResponseTotoTicketClearingData(
        X_outou_kekka='12',
        X_toto_kekka='000000',
    )
    return COMPARE_TOTO_TICKET_CLEARING_DICT(data)

def BARCODE_TOTO_CLEARING_OUTOU_KEKKA_13():
    """
    正常系　払込票番号 生成時選択肢
    --------
    払戻金額 : 9999999999
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    払戻金額 : 0000003500
    処理結果 : "00"：正常
    応答結果 : "13"：totoセンターアプリエラー
    totoセンター応答結果 : 000001
    """
    return '9000015750519'
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_13_REPAY():
    data =  ResponseTotoTicketClearingData(
        X_payback_amt='9999999999',
        X_haraimodoshi='9000015750519',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_13_REPAY_CANCEL():
    data =  ResponseTotoTicketClearingData(
        X_payback_amt='0000003500',
        X_haraimodoshi='9000015750519',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_13():
    data =  ResponseTotoTicketClearingData(
        X_outou_kekka='13',
        X_toto_kekka='000001',
    )
    return COMPARE_TOTO_TICKET_CLEARING_DICT(data)

def BARCODE_TOTO_CLEARING_OUTOU_KEKKA_14():
    """
    正常系　払込票番号 生成時選択肢
    --------
    払戻金額 : 0000000000
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    払戻金額 : 0000003500
    処理結果 : "00"：正常
    応答結果 : "14"：totoセンター通信その他エラー
    totoセンター応答結果 : 000002
    """
    return '9000000022072'
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_14_REPAY():
    data =  ResponseTotoTicketClearingData(
        X_haraimodoshi='9000000022072',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_14_REPAY_CANCEL():
    data =  ResponseTotoTicketClearingData(
        X_payback_amt='0000003500',
        X_haraimodoshi='9000000022072',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_14():
    data =  ResponseTotoTicketClearingData(
        X_outou_kekka='14',
        X_toto_kekka='000002',
    )
    return COMPARE_TOTO_TICKET_CLEARING_DICT(data)

def BARCODE_TOTO_CLEARING_OUTOU_KEKKA_99():
    """
    正常系　払込票番号 生成時選択肢
    --------
    払戻金額 : 0000000000
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    払戻金額 : 0000003500
    処理結果 : "00"：正常
    応答結果 : "99"：その他エラー
    totoセンター応答結果 : 空タグ
    """
    return '9000000022119'
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_99_REPAY():
    data =  ResponseTotoTicketClearingData(
        X_haraimodoshi='9000000022119',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_99_REPAY_CANCEL():
    data =  ResponseTotoTicketClearingData(
        X_payback_amt='0000003500',
        X_haraimodoshi='9000000022119',
    )
    return COMPARE_TOTO_TICKET_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_99():
    data =  ResponseTotoTicketClearingData(
        X_outou_kekka='99',
    )
    return COMPARE_TOTO_TICKET_CLEARING_DICT(data)
