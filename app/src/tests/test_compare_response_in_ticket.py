from test_barcode_functions import *

# ---------------------------
# INチケット マッピングNo1
# ---------------------------
def BARCODE_IN_TICKET_CASE_01():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    ショップＩＤ : "30400"：7DC
    応答結果区分 : 01：代引き
    チケット代金/発券代金/チケット購入代金/印紙基準額 : "000000"：最低値
    本券購入枚数/チケット枚数 : 1
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    成功まで失敗回数 : 0
    """
    return '2100000000005'
def HIKIKAE_IN_TICKET_CASE_01():
    return '2200000000002'
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_01():
    data =  ResponseInTicketData(
        X_shop_id='30400',
        X_outou_kekka_kbn='01',
        X_ticket_cnt='01',
        X_haraikomi='2100000000005',
        X_hikikae='2200000000002',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_01_CANCEL():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='01',
        X_ticket_cnt='01',
        X_haraikomi='2100000000005',
        X_hikikae='2200000000002',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_01_KANRYO():
    data =  ResponseInTicketData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_CASE_02():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    ショップＩＤ : "30512"：旧ソフトバンクギフトショップ/組合せクーポンショップ
    応答結果区分 : 02：前払い（後日発券）
    チケット代金/発券代金/チケット購入代金/印紙基準額 : "999999"：最大値
    本券購入枚数/チケット枚数 : 20
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    成功まで失敗回数 : 0
    """
    return '2100028180482'
def HIKIKAE_IN_TICKET_CASE_02():
    return '2200028180489'
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_02():
    data =  ResponseInTicketData(
        X_shop_id='30512',
        X_outou_kekka_kbn='02',
        tc_daikin='999999',
        X_ticket_cnt='20',
        X_haraikomi='2100028180482',
        X_hikikae='2200028180489',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_02_CANCEL():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='02',
        tc_daikin='999999',
        X_ticket_cnt='20',
        X_haraikomi='2100028180482',
        X_hikikae='2200028180489',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_02_KANRYO():
    data =  ResponseInTicketData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_CASE_03():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    ショップＩＤ : "30513"：組合せクーポンショップ
    応答結果区分 : 03：代済発券
    チケット代金/発券代金/チケット購入代金/印紙基準額 : "003500"：一般値
    本券購入枚数/チケット枚数 : 1
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    処理結果 : "11"：業務区分エラー 
    応答結果 : "00"：正常応答
    成功まで失敗回数 : 0
    """
    return '2100055050567'
def HIKIKAE_IN_TICKET_CASE_03():
    return '2200055050564'
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_03():
    data =  ResponseInTicketData(
        X_shop_id='30513',
        X_outou_kekka_kbn='03',
        tc_daikin='003500',
        X_ticket_cnt='01',
        X_haraikomi='2100055050567',
        X_hikikae='2200055050564',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_03_CANCEL():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='03',
        tc_daikin='003500',
        X_ticket_cnt='01',
        X_haraikomi='2100055050567',
        X_hikikae='2200055050564',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_03_KANRYO():
    data =  ResponseInTicketData(
        X_shori_kekka='11',
    )
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_CASE_04():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    ショップＩＤ : "30514"：チケットぴあ①
    応答結果区分 : 04：前払いのみ
    チケット代金/発券代金/チケット購入代金/印紙基準額 : "001000"：一般値
    本券購入枚数/チケット枚数 : 1
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    処理結果 : "14"：サービス時間帯エラー
    応答結果 : "00"：正常応答
    成功まで失敗回数 : 5
    """
    return '2100082576023'
def HIKIKAE_IN_TICKET_CASE_04():
    return '2200082576020'
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_04():
    data =  ResponseInTicketData(
        X_shop_id='30514',
        X_outou_kekka_kbn='04',
        tc_daikin='001000',
        X_ticket_cnt='01',
        X_haraikomi='2100082576023',
        X_hikikae='2200082576020',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_04_CANCEL():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='04',
        tc_daikin='001000',
        X_ticket_cnt='01',
        X_haraikomi='2100082576023',
        X_hikikae='2200082576020',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_04_KANRYO():
    data =  ResponseInTicketData(
        X_shori_kekka='14',
    )
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_CASE_05():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    ショップＩＤ : "30701"：Mコピーインターネットチケット①
    応答結果区分 : 01：代引き
    チケット代金/発券代金/チケット購入代金/印紙基準額 : "000000"：最低値
    本券購入枚数/チケット枚数 : 1
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    成功まで失敗回数 : 0
    """
    return '2100083886084'
def HIKIKAE_IN_TICKET_CASE_05():
    return '2200083886081'
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_05():
    data =  ResponseInTicketData(
        X_shop_id='30701',
        X_outou_kekka_kbn='01',
        X_ticket_cnt='01',
        X_haraikomi='2100083886084',
        X_hikikae='2200083886081',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_05_CANCEL():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='01',
        X_ticket_cnt='01',
        X_haraikomi='2100083886084',
        X_hikikae='2200083886081',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_05_KANRYO():
    data =  ResponseInTicketData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_CASE_06():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    ショップＩＤ : "30731"：チケットぴあ②
    応答結果区分 : 01：代引き
    チケット代金/発券代金/チケット購入代金/印紙基準額 : "000000"：最低値
    本券購入枚数/チケット枚数 : 1
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    成功まで失敗回数 : 0
    """
    return '2100104857604'
def HIKIKAE_IN_TICKET_CASE_06():
    return '2200104857601'
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_06():
    data =  ResponseInTicketData(
        X_shop_id='30731',
        X_outou_kekka_kbn='01',
        X_ticket_cnt='01',
        X_haraikomi='2100104857604',
        X_hikikae='2200104857601',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_06_CANCEL():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='01',
        X_ticket_cnt='01',
        X_haraikomi='2100104857604',
        X_hikikae='2200104857601',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_06_KANRYO():
    data =  ResponseInTicketData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_CASE_07():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    ショップＩＤ : "30732"：チケットぴあ③
    応答結果区分 : 01：代引き
    チケット代金/発券代金/チケット購入代金/印紙基準額 : "000000"：最低値
    本券購入枚数/チケット枚数 : 1
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    成功まで失敗回数 : 0
    """
    return '2100125829123'
def HIKIKAE_IN_TICKET_CASE_07():
    return '2200125829120'
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_07():
    data =  ResponseInTicketData(
        X_shop_id='30732',
        X_outou_kekka_kbn='01',
        X_ticket_cnt='01',
        X_haraikomi='2100125829123',
        X_hikikae='2200125829120',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_07_CANCEL():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='01',
        X_ticket_cnt='01',
        X_haraikomi='2100125829123',
        X_hikikae='2200125829120',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_07_KANRYO():
    data =  ResponseInTicketData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_CASE_08():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    ショップＩＤ : "30773"：Mコピーインターネットチケット②
    応答結果区分 : 01：代引き
    チケット代金/発券代金/チケット購入代金/印紙基準額 : "000000"：最低値
    本券購入枚数/チケット枚数 : 1
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    成功まで失敗回数 : 0
    """
    return '2100146800644'
def HIKIKAE_IN_TICKET_CASE_08():
    return '2200146800641'
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_08():
    data =  ResponseInTicketData(
        X_shop_id='30773',
        X_outou_kekka_kbn='01',
        X_ticket_cnt='01',
        X_haraikomi='2100146800644',
        X_hikikae='2200146800641',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_08_CANCEL():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='01',
        X_ticket_cnt='01',
        X_haraikomi='2100146800644',
        X_hikikae='2200146800641',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_08_KANRYO():
    data =  ResponseInTicketData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_CASE_09():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    ショップＩＤ : "30775"：JTBレジャー（TDR）
    応答結果区分 : 01：代引き
    チケット代金/発券代金/チケット購入代金/印紙基準額 : "000000"：最低値
    本券購入枚数/チケット枚数 : 1
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    成功まで失敗回数 : 0
    """
    return '2100167772166'
def HIKIKAE_IN_TICKET_CASE_09():
    return '2200167772163'
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_09():
    data =  ResponseInTicketData(
        X_shop_id='30775',
        X_outou_kekka_kbn='01',
        X_ticket_cnt='01',
        X_haraikomi='2100167772166',
        X_hikikae='2200167772163',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_09_CANCEL():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='01',
        X_ticket_cnt='01',
        X_haraikomi='2100167772166',
        X_hikikae='2200167772163',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_09_KANRYO():
    data =  ResponseInTicketData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_CASE_10():
    """
    正常系　組合せクーポンショップ
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    ショップＩＤ : "30513"：組合せクーポンショップ
    応答結果区分 : 04：前払いのみ
    チケット代金/発券代金/チケット購入代金/印紙基準額 : "000000"：最低値
    本券購入枚数/チケット枚数 : 1
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    成功まで失敗回数 : 0
    """
    return '2100057671685'
def HIKIKAE_IN_TICKET_CASE_10():
    return '2200057671682'
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_10():
    data =  ResponseInTicketData(
        X_shop_id='30513',
        X_outou_kekka_kbn='04',
        tc_daikin='000000',
        X_ticket_cnt='01',
        X_haraikomi='2100057671685',
        X_hikikae='2200057671682',
        X_hansoku_jan_code='9850100001640',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_10_CANCEL():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='04',
        tc_daikin='000000',
        X_ticket_cnt='01',
        X_haraikomi='2100057671685',
        X_hikikae='2200057671682',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_CASE_10_KANRYO():
    data =  ResponseInTicketData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_SYORI_KEKKA_11():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "11"：業務区分エラー 
    応答結果 : "00"：正常応答
    ショップＩＤ : "30400"：7DC
    応答結果区分 : 01：代引き
    チケット代金/発券代金/チケット購入代金/印紙基準額 : "000000"：最低値
    本券購入枚数/チケット枚数 : 1
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    処理結果 : "15"：タイムアウトエラー
    応答結果 : "00"：正常応答
    成功まで失敗回数 : 10
    """
    return '2105368710122'
def HIKIKAE_IN_TICKET_SYORI_KEKKA_11():
    return '2205368710129'
def RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_11():
    data =  ResponseInTicketData(
        X_shori_kekka='11',
        X_shop_id='30400',
        X_outou_kekka_kbn='01',
        X_ticket_cnt='01',
        X_haraikomi='2105368710122',
        X_hikikae='2205368710129',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_11_RETRY():
    data =  ResponseInTicketData(
        X_shop_id='30400',
        X_outou_kekka_kbn='01',
        X_ticket_cnt='01',
        X_haraikomi='2105368710122',
        X_hikikae='2205368710129',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_11_CANCEL():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='01',
        X_ticket_cnt='01',
        X_haraikomi='2105368710122',
        X_hikikae='2205368710129',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_11_KANRYO():
    data =  ResponseInTicketData(
        X_shori_kekka='15',
    )
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_SYORI_KEKKA_14():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "14"：サービス時間帯エラー
    応答結果 : "00"：正常応答
    ショップＩＤ : "30512"：旧ソフトバンクギフトショップ/組合せクーポンショップ
    応答結果区分 : 02：前払い（後日発券）
    チケット代金/発券代金/チケット購入代金/印紙基準額 : "999999"：最大値
    本券購入枚数/チケット枚数 : 1
    レスポンスパターン（再送区分用） : "1"：再送異常
    取消処理結果 : "00"：正常
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    処理結果 : "99"：その他エラー(400)
    応答結果 : "00"：正常応答
    成功まで失敗回数 : 15
    """
    return '2110765272388'
def HIKIKAE_IN_TICKET_SYORI_KEKKA_14():
    return '2210765272385'
def RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_14():
    data =  ResponseInTicketData(
        X_shori_kekka='14',
        X_shop_id='30512',
        X_outou_kekka_kbn='02',
        tc_daikin='999999',
        X_ticket_cnt='01',
        X_haraikomi='2110765272388',
        X_hikikae='2210765272385',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_14_CANCEL():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='02',
        tc_daikin='999999',
        X_ticket_cnt='01',
        X_haraikomi='2110765272388',
        X_hikikae='2210765272385',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_14_KANRYO():
    data =  ResponseInTicketData(
        X_shori_kekka='99',
    )
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_SYORI_KEKKA_15():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "15"：タイムアウトエラー
    応答結果 : "00"：正常応答
    ショップＩＤ : "30513"：組合せクーポンショップ
    応答結果区分 : 03：代済発券
    チケット代金/発券代金/チケット購入代金/印紙基準額 : "003500"：一般値
    本券購入枚数/チケット枚数 : 1
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "10"：電文区分エラー
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    処理結果 : "99"：その他エラー(500)
    応答結果 : "00"：正常応答
    成功まで失敗回数 : 0
    """
    return '2116161220169'
def HIKIKAE_IN_TICKET_SYORI_KEKKA_15():
    return '2216161220166'
def RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_15():
    data =  ResponseInTicketData(
        X_shori_kekka='15',
        X_shop_id='30513',
        X_outou_kekka_kbn='03',
        tc_daikin='003500',
        X_ticket_cnt='01',
        X_haraikomi='2116161220169',
        X_hikikae='2216161220166',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_15_RETRY():
    data =  ResponseInTicketData(
        X_shop_id='30513',
        X_outou_kekka_kbn='03',
        tc_daikin='003500',
        X_ticket_cnt='01',
        X_haraikomi='2116161220169',
        X_hikikae='2216161220166',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_15_CANCEL():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='03',
        tc_daikin='003500',
        X_ticket_cnt='01',
        X_shori_kekka='10',
        X_haraikomi='2116161220169',
        X_hikikae='2216161220166',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_15_CANCEL_RETRY():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='03',
        tc_daikin='003500',
        X_ticket_cnt='01',
        X_haraikomi='2116161220169',
        X_hikikae='2216161220166',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_15_KANRYO():
    data =  ResponseInTicketData(
        X_shori_kekka='99',
    )
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_SYORI_KEKKA_99_400():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "99"：その他エラー(400)
    応答結果 : "00"：正常応答
    ショップＩＤ : "30514"：チケットぴあ①
    応答結果区分 : 04：前払いのみ
    チケット代金/発券代金/チケット購入代金/印紙基準額 : "001000"：一般値
    本券購入枚数/チケット枚数 : 1
    レスポンスパターン（再送区分用） : "1"：再送異常
    取消処理結果 : "11"：業務区分エラー
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    処理結果 : "00"：タイムアウト(200)
    応答結果 : "00"：正常応答
    成功まで失敗回数 : 0
    """
    return '2121557823367'
def HIKIKAE_IN_TICKET_SYORI_KEKKA_99_400():
    return '2221557823364'
def RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_99_400():
    data =  ResponseInTicketData(
        X_shori_kekka='99',
        X_shop_id='30514',
        X_outou_kekka_kbn='04',
        tc_daikin='001000',
        X_ticket_cnt='01',
        X_haraikomi='2121557823367',
        X_hikikae='2221557823364',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_99_400_CANCEL():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='04',
        tc_daikin='001000',
        X_ticket_cnt='01',
        X_shori_kekka='11',
        X_haraikomi='2121557823367',
        X_hikikae='2221557823364',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_99_400_CANCEL_RETRY():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='04',
        tc_daikin='001000',
        X_ticket_cnt='01',
        X_haraikomi='2121557823367',
        X_hikikae='2221557823364',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_99_400_KANRYO():
    data =  ResponseInTicketData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_SYORI_KEKKA_99_500():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "99"：その他エラー(500)
    応答結果 : "00"：正常応答
    ショップＩＤ : "30400"：7DC
    応答結果区分 : 01：代引き
    チケット代金/発券代金/チケット購入代金/印紙基準額 : "000000"：最低値
    本券購入枚数/チケット枚数 : 1
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "14"：サービス時間帯エラー
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "1"：再送異常
    処理結果 : "99"：タイムアウト(その他エラー500)
    応答結果 : "00"：正常応答
    成功まで失敗回数 : 0
    """
    return '2126843673282'
def HIKIKAE_IN_TICKET_SYORI_KEKKA_99_500():
    return '2226843673289'
def RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_99_500():
    data =  ResponseInTicketData(
        X_shori_kekka='99',
        X_shop_id='30400',
        X_outou_kekka_kbn='01',
        X_ticket_cnt='01',
        X_haraikomi='2126843673282',
        X_hikikae='2226843673289',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_99_500_RETRY():
    data =  ResponseInTicketData(
        X_shop_id='30400',
        X_outou_kekka_kbn='01',
        X_ticket_cnt='01',
        X_haraikomi='2126843673282',
        X_hikikae='2226843673289',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_99_500_CANCEL():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='01',
        X_ticket_cnt='01',
        X_shori_kekka='14',
        X_haraikomi='2126843673282',
        X_hikikae='2226843673289',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_99_500_KANRYO():
    data =  ResponseInTicketData(
        X_shori_kekka='99',
    )
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_TIMEOUT():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：タイムアウト(200)
    応答結果 : "00"：正常応答
    ショップＩＤ : "30512"：旧ソフトバンクギフトショップ/組合せクーポンショップ
    応答結果区分 : 02：前払い（後日発券）
    チケット代金/発券代金/チケット購入代金/印紙基準額 : "999999"：最大値
    本券購入枚数/チケット枚数 : 1
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "99"：その他エラー(400)
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    処理結果 : "00"：正常
    応答結果 : "01"：検索キーエラー
    成功まで失敗回数 : 0
    """
    return '2132239943761'
def HIKIKAE_IN_TICKET_TIMEOUT():
    return '2232239943768'
def RESPONSE_TICKET_DATA_IN_TICKET_TIMEOUT():
    data =  ResponseInTicketData(
        X_shop_id='30512',
        X_outou_kekka_kbn='02',
        tc_daikin='999999',
        X_ticket_cnt='01',
        X_haraikomi='2132239943761',
        X_hikikae='2232239943768',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_TIMEOUT_CANCEL():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='02',
        tc_daikin='999999',
        X_ticket_cnt='01',
        X_shori_kekka='99',
        X_haraikomi='2132239943761',
        X_hikikae='2232239943768',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_TIMEOUT_CANCEL_RETRY():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='02',
        tc_daikin='999999',
        X_ticket_cnt='01',
        X_haraikomi='2132239943761',
        X_hikikae='2232239943768',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_TIMEOUT_KANRYO():
    data =  ResponseInTicketData(
        X_outou_kekka='01',
    )
    return COMPARE_IN_TICKET_KANRYO_DICT(data)
def BARCODE_IN_TICKET_TIMEOUT_500():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "99"：タイムアウト(その他エラー500)
    応答結果 : "00"：正常応答
    ショップＩＤ : "30513"：組合せクーポンショップ
    応答結果区分 : 03：代済発券
    チケット代金/発券代金/チケット購入代金/印紙基準額 : "003500"：一般値
    本券購入枚数/チケット枚数 : 1
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "99"：その他エラー(500)
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    処理結果 : "00"：正常
    応答結果 : "99"：その他エラー
    成功まで失敗回数 : 0
    """
    return '2137636219044'
def HIKIKAE_IN_TICKET_TIMEOUT_500():
    return '2237636219041'
def RESPONSE_TICKET_DATA_IN_TICKET_TIMEOUT_500():
    data =  ResponseInTicketData(
        X_shori_kekka='99',
        X_shop_id='30513',
        X_outou_kekka_kbn='03',
        tc_daikin='003500',
        X_ticket_cnt='01',
        X_haraikomi='2137636219044',
        X_hikikae='2237636219041',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_TIMEOUT_500_RETRY():
    data =  ResponseInTicketData(
        X_shop_id='30513',
        X_outou_kekka_kbn='03',
        tc_daikin='003500',
        X_ticket_cnt='01',
        X_haraikomi='2137636219044',
        X_hikikae='2237636219041',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_TIMEOUT_500_CANCEL():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='03',
        tc_daikin='003500',
        X_ticket_cnt='01',
        X_shori_kekka='99',
        X_haraikomi='2137636219044',
        X_hikikae='2237636219041',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_TIMEOUT_500_CANCEL_RETRY():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='03',
        tc_daikin='003500',
        X_ticket_cnt='01',
        X_haraikomi='2137636219044',
        X_hikikae='2237636219041',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_TIMEOUT_500_KANRYO():
    data =  ResponseInTicketData(
        X_outou_kekka='99',
    )
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_OUTOU_KEKKA_01():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "01"：検索キーエラー
    ショップＩＤ : "30514"：チケットぴあ①
    応答結果区分 : 04：前払いのみ
    チケット代金/発券代金/チケット購入代金/印紙基準額 : "001000"：一般値
    本券購入枚数/チケット枚数 : 1
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：タイムアウト(200)
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    成功まで失敗回数 : 0
    """
    return '2100418365444'
def HIKIKAE_IN_TICKET_OUTOU_KEKKA_01():
    return '2200418365441'
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_01():
    data =  ResponseInTicketData(
        X_outou_kekka='01',
        X_shop_id='30514',
        X_outou_kekka_kbn='04',
        tc_daikin='001000',
        X_ticket_cnt='01',
        X_haraikomi='2100418365444',
        X_hikikae='2200418365441',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_01_RETRY():
    data =  ResponseInTicketData(
        X_shop_id='30514',
        X_outou_kekka_kbn='04',
        tc_daikin='001000',
        X_ticket_cnt='01',
        X_haraikomi='2100418365444',
        X_hikikae='2200418365441',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_01_CANCEL():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='04',
        tc_daikin='001000',
        X_ticket_cnt='01',
        X_haraikomi='2100418365444',
        X_hikikae='2200418365441',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_01_KANRYO():
    data =  ResponseInTicketData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_OUTOU_KEKKA_02():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "02"：支払期限エラー
    ショップＩＤ : "30400"：7DC
    応答結果区分 : 01：代引き
    チケット代金/発券代金/チケット購入代金/印紙基準額 : "000000"：最低値
    本券購入枚数/チケット枚数 : 1
    レスポンスパターン（再送区分用） : "1"：再送異常
    取消処理結果 : "99"：タイムアウト(その他エラー500)
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    成功まで失敗回数 : 0
    """
    return '2100671703045'
def HIKIKAE_IN_TICKET_OUTOU_KEKKA_02():
    return '2200671703042'
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_02():
    data =  ResponseInTicketData(
        X_outou_kekka='02',
        X_shop_id='30400',
        X_outou_kekka_kbn='01',
        X_ticket_cnt='01',
        X_haraikomi='2100671703045',
        X_hikikae='2200671703042',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_02_CANCEL():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='01',
        X_ticket_cnt='01',
        X_shori_kekka='99',
        X_haraikomi='2100671703045',
        X_hikikae='2200671703042',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_02_CANCEL_RETRY():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='01',
        X_ticket_cnt='01',
        X_haraikomi='2100671703045',
        X_hikikae='2200671703042',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_02_KANRYO():
    data =  ResponseInTicketData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_OUTOU_KEKKA_03():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "03"：支払済みエラー
    ショップＩＤ : "30512"：旧ソフトバンクギフトショップ/組合せクーポンショップ
    応答結果区分 : 02：前払い（後日発券）
    チケット代金/発券代金/チケット購入代金/印紙基準額 : "999999"：最大値
    本券購入枚数/チケット枚数 : 1
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "01"：取消異常(検索キーエラー)
    レスポンスパターン（取消再送区分用） : "1"：再送異常
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    成功まで失敗回数 : 0
    """
    return '2101034165760'
def HIKIKAE_IN_TICKET_OUTOU_KEKKA_03():
    return '2201034165767'
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_03():
    data =  ResponseInTicketData(
        X_outou_kekka='03',
        X_shop_id='30512',
        X_outou_kekka_kbn='02',
        tc_daikin='999999',
        X_ticket_cnt='01',
        X_haraikomi='2101034165760',
        X_hikikae='2201034165767',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_03_RETRY():
    data =  ResponseInTicketData(
        X_shop_id='30512',
        X_outou_kekka_kbn='02',
        tc_daikin='999999',
        X_ticket_cnt='01',
        X_haraikomi='2101034165760',
        X_hikikae='2201034165767',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_03_CANCEL():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='02',
        tc_daikin='999999',
        X_ticket_cnt='01',
        X_outou_kekka='01',
        X_haraikomi='2101034165760',
        X_hikikae='2201034165767',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_03_KANRYO():
    data =  ResponseInTicketData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_OUTOU_KEKKA_05():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "05"：決済中止エラー
（ショップ取引停止エラー）
    ショップＩＤ : "30513"：組合せクーポンショップ
    応答結果区分 : 03：代済発券
    チケット代金/発券代金/チケット購入代金/印紙基準額 : "003500"：一般値
    本券購入枚数/チケット枚数 : 1
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "04"：取消異常(取消済み)
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    成功まで失敗回数 : 0
    """
    return '2101397237760'
def HIKIKAE_IN_TICKET_OUTOU_KEKKA_05():
    return '2201397237767'
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_05():
    data =  ResponseInTicketData(
        X_outou_kekka='05',
        X_shop_id='30513',
        X_outou_kekka_kbn='03',
        tc_daikin='003500',
        X_ticket_cnt='01',
        X_haraikomi='2101397237760',
        X_hikikae='2201397237767',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_05_RETRY():
    data =  ResponseInTicketData(
        X_shop_id='30513',
        X_outou_kekka_kbn='03',
        tc_daikin='003500',
        X_ticket_cnt='01',
        X_haraikomi='2101397237760',
        X_hikikae='2201397237767',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_05_CANCEL():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='03',
        tc_daikin='003500',
        X_ticket_cnt='01',
        X_outou_kekka='04',
        X_haraikomi='2101397237760',
        X_hikikae='2201397237767',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_05_CANCEL_RETRY():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='03',
        tc_daikin='003500',
        X_ticket_cnt='01',
        X_haraikomi='2101397237760',
        X_hikikae='2201397237767',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_05_KANRYO():
    data =  ResponseInTicketData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_OUTOU_KEKKA_07():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "07"：発券済みエラー
    ショップＩＤ : "30514"：チケットぴあ①
    応答結果区分 : 04：前払いのみ
    チケット代金/発券代金/チケット購入代金/印紙基準額 : "001000"：一般値
    本券購入枚数/チケット枚数 : 1
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "09"：発券取消済みエラー
    レスポンスパターン（取消再送区分用） : "1"：再送異常
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    成功まで失敗回数 : 0
    """
    return '2101760314883'
def HIKIKAE_IN_TICKET_OUTOU_KEKKA_07():
    return '2201760314880'
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_07():
    data =  ResponseInTicketData(
        X_outou_kekka='07',
        X_shop_id='30514',
        X_outou_kekka_kbn='04',
        tc_daikin='001000',
        X_ticket_cnt='01',
        X_haraikomi='2101760314883',
        X_hikikae='2201760314880',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_07_RETRY():
    data =  ResponseInTicketData(
        X_shop_id='30514',
        X_outou_kekka_kbn='04',
        tc_daikin='001000',
        X_ticket_cnt='01',
        X_haraikomi='2101760314883',
        X_hikikae='2201760314880',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_07_CANCEL():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='04',
        tc_daikin='001000',
        X_ticket_cnt='01',
        X_outou_kekka='09',
        X_haraikomi='2101760314883',
        X_hikikae='2201760314880',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_07_KANRYO():
    data =  ResponseInTicketData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_OUTOU_KEKKA_08():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "08"：発券期限エラー
    ショップＩＤ : "30400"：7DC
    応答結果区分 : 01：代引き
    チケット代金/発券代金/チケット購入代金/印紙基準額 : "000000"：最低値
    本券購入枚数/チケット枚数 : 1
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "60"：強制成立取消不可
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    成功まで失敗回数 : 0
    """
    return '2102013286407'
def HIKIKAE_IN_TICKET_OUTOU_KEKKA_08():
    return '2202013286404'
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_08():
    data =  ResponseInTicketData(
        X_outou_kekka='08',
        X_shop_id='30400',
        X_outou_kekka_kbn='01',
        X_ticket_cnt='01',
        X_haraikomi='2102013286407',
        X_hikikae='2202013286404',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_08_RETRY():
    data =  ResponseInTicketData(
        X_shop_id='30400',
        X_outou_kekka_kbn='01',
        X_ticket_cnt='01',
        X_haraikomi='2102013286407',
        X_hikikae='2202013286404',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_08_CANCEL():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='01',
        X_ticket_cnt='01',
        X_outou_kekka='60',
        X_haraikomi='2102013286407',
        X_hikikae='2202013286404',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_08_CANCEL_RETRY():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='01',
        X_ticket_cnt='01',
        X_haraikomi='2102013286407',
        X_hikikae='2202013286404',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_08_KANRYO():
    data =  ResponseInTicketData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_OUTOU_KEKKA_13():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "13"：入金中止エラー
    ショップＩＤ : "30512"：旧ソフトバンクギフトショップ/組合せクーポンショップ
    応答結果区分 : 02：前払い（後日発券）
    チケット代金/発券代金/チケット購入代金/印紙基準額 : "999999"：最大値
    本券購入枚数/チケット枚数 : 1
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "99"：取消異常(その他エラー)
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    成功まで失敗回数 : 0
    """
    return '2102376360967'
def HIKIKAE_IN_TICKET_OUTOU_KEKKA_13():
    return '2202376360964'
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_13():
    data =  ResponseInTicketData(
        X_outou_kekka='13',
        X_shop_id='30512',
        X_outou_kekka_kbn='02',
        tc_daikin='999999',
        X_ticket_cnt='01',
        X_haraikomi='2102376360967',
        X_hikikae='2202376360964',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_13_RETRY():
    data =  ResponseInTicketData(
        X_shop_id='30512',
        X_outou_kekka_kbn='02',
        tc_daikin='999999',
        X_ticket_cnt='01',
        X_haraikomi='2102376360967',
        X_hikikae='2202376360964',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_13_CANCEL():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='02',
        tc_daikin='999999',
        X_ticket_cnt='01',
        X_outou_kekka='99',
        X_haraikomi='2102376360967',
        X_hikikae='2202376360964',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_13_CANCEL_RETRY():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='02',
        tc_daikin='999999',
        X_ticket_cnt='01',
        X_haraikomi='2102376360967',
        X_hikikae='2202376360964',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_13_KANRYO():
    data =  ResponseInTicketData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_OUTOU_KEKKA_14():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "14"：発券開始前エラー
    ショップＩＤ : "30513"：組合せクーポンショップ
    応答結果区分 : 03：代済発券
    チケット代金/発券代金/チケット購入代金/印紙基準額 : "003500"：一般値
    本券購入枚数/チケット枚数 : 1
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    成功まで失敗回数 : 0
    """
    return '2102739404802'
def HIKIKAE_IN_TICKET_OUTOU_KEKKA_14():
    return '2202739404809'
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_14():
    data =  ResponseInTicketData(
        X_outou_kekka='14',
        X_shop_id='30513',
        X_outou_kekka_kbn='03',
        tc_daikin='003500',
        X_ticket_cnt='01',
        X_haraikomi='2102739404802',
        X_hikikae='2202739404809',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_14_RETRY():
    data =  ResponseInTicketData(
        X_shop_id='30513',
        X_outou_kekka_kbn='03',
        tc_daikin='003500',
        X_ticket_cnt='01',
        X_haraikomi='2102739404802',
        X_hikikae='2202739404809',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_14_CANCEL():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='03',
        tc_daikin='003500',
        X_ticket_cnt='01',
        X_haraikomi='2102739404802',
        X_hikikae='2202739404809',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_14_KANRYO():
    data =  ResponseInTicketData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_OUTOU_KEKKA_15():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "15"：発券中止エラー
    ショップＩＤ : "30514"：チケットぴあ①
    応答結果区分 : 04：前払いのみ
    チケット代金/発券代金/チケット購入代金/印紙基準額 : "001000"：一般値
    本券購入枚数/チケット枚数 : 1
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    成功まで失敗回数 : 0
    """
    return '2103102474248'
def HIKIKAE_IN_TICKET_OUTOU_KEKKA_15():
    return '2203102474245'
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_15():
    data =  ResponseInTicketData(
        X_outou_kekka='15',
        X_shop_id='30514',
        X_outou_kekka_kbn='04',
        tc_daikin='001000',
        X_ticket_cnt='01',
        X_haraikomi='2103102474248',
        X_hikikae='2203102474245',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_15_RETRY():
    data =  ResponseInTicketData(
        X_shop_id='30514',
        X_outou_kekka_kbn='04',
        tc_daikin='001000',
        X_ticket_cnt='01',
        X_haraikomi='2103102474248',
        X_hikikae='2203102474245',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_15_CANCEL():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='04',
        tc_daikin='001000',
        X_ticket_cnt='01',
        X_haraikomi='2103102474248',
        X_hikikae='2203102474245',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_15_KANRYO():
    data =  ResponseInTicketData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_OUTOU_KEKKA_99():
    """
    正常系　払込票番号 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "99"：その他エラー
    ショップＩＤ : "30514"：チケットぴあ①
    応答結果区分 : 01：代引き
    チケット代金/発券代金/チケット購入代金/印紙基準額 : "003500"：一般値
    本券購入枚数/チケット枚数 : 1
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    成功まで失敗回数 : 0
    """
    return '2103420979203'
def HIKIKAE_IN_TICKET_OUTOU_KEKKA_99():
    return '2203420979200'
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_99():
    data =  ResponseInTicketData(
        X_outou_kekka='99',
        X_shop_id='30514',
        X_outou_kekka_kbn='01',
        tc_daikin='003500',
        X_ticket_cnt='01',
        X_haraikomi='2103420979203',
        X_hikikae='2203420979200',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_99_RETRY():
    data =  ResponseInTicketData(
        X_shop_id='30514',
        X_outou_kekka_kbn='01',
        tc_daikin='003500',
        X_ticket_cnt='01',
        X_haraikomi='2103420979203',
        X_hikikae='2203420979200',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_99_CANCEL():
    data =  ResponseInTicketData(
        X_outou_kekka_kbn='01',
        tc_daikin='003500',
        X_ticket_cnt='01',
        X_haraikomi='2103420979203',
        X_hikikae='2203420979200',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_99_KANRYO():
    data =  ResponseInTicketData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)


# ---------------------------
# INチケット マッピングNo2
# ---------------------------
def BARCODE_IN_TICKET_DETAIL_NO_TICKET():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30400"：7DC
    応答結果区分 : 01：代引き
    チケット代金 : "999999"：最大値
    発券代金 : "000000"：最低値
    チケット購入代金 : "000000"：最低値
    印紙基準額 : "999999"：最大値
    チケット枚数 : 0
    券面情報データ : A
    """
    return '2100001331214'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_NO_TICKET():
    data =  ResponseInTicketDetailData(
        X_shop_id='30400',
        X_outou_kekka_kbn='01',
        X_tc_dai='999999',
        X_inshi_kijun='999999',
        tc_info_data='A',
        X_haraikomi='2100001331214',
        X_hikikae='2200001331211',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_NO_TICKET_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30400',
        X_outou_kekka_kbn='01',
        X_tc_dai='999999',
        X_inshi_kijun='999999',
        tc_info_data='A',
        X_haraikomi='2100001331214',
        X_hikikae='2200001331211',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_NO_TICKET_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_DETAIL_A():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30501"：CNプレイガイド
    応答結果区分 : 02：前払い（後日発券）
    チケット代金 : "000000"：最低値
    発券代金 : "999999"：最大値
    チケット購入代金 : "000000"：最低値
    印紙基準額 : "999999"：最大値
    チケット枚数 : 1
    券面情報データ : A
    """
    return '2100026563218'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_A():
    data =  ResponseInTicketDetailData(
        X_shop_id='30501',
        X_outou_kekka_kbn='02',
        X_hakken_dai='999999',
        X_inshi_kijun='999999',
        X_ticket_cnt='01',
        tc_info_data='A',
        X_haraikomi='2100026563218',
        X_hikikae='2200026563215',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_A_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30501',
        X_outou_kekka_kbn='02',
        X_hakken_dai='999999',
        X_inshi_kijun='999999',
        X_ticket_cnt='01',
        tc_info_data='A',
        X_haraikomi='2100026563218',
        X_hikikae='2200026563215',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_A_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_DETAIL_B():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30512"：旧ソフトバンクギフトショップ/組合せクーポンショップ
    応答結果区分 : 03：代済発券
    チケット代金 : "000000"：最低値
    発券代金 : "000000"：最低値
    チケット購入代金 : "999999"：最大値
    印紙基準額 : "999999"：最大値
    チケット枚数 : 2
    券面情報データ : B
    """
    return '2100052532516'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_B():
    data =  ResponseInTicketDetailData(
        X_shop_id='30512',
        X_outou_kekka_kbn='03',
        X_tc_kounyu_dai='999999',
        X_inshi_kijun='999999',
        X_ticket_cnt='02',
        tc_info_data='B',
        X_haraikomi='2100052532516',
        X_hikikae='2200052532513',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_B_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30512',
        X_outou_kekka_kbn='03',
        X_tc_kounyu_dai='999999',
        X_inshi_kijun='999999',
        X_ticket_cnt='02',
        tc_info_data='B',
        X_haraikomi='2100052532516',
        X_hikikae='2200052532513',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_B_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_DETAIL_C():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30513"：組合せクーポンショップ
    応答結果区分 : 04：前払いのみ
    チケット代金 : "001000"：一般値
    発券代金 : "001000"：一般値
    チケット購入代金 : "001000"：一般値
    印紙基準額 : "999999"：最大値
    チケット枚数 : 3
    券面情報データ : C
    """
    return '2100083826615'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_C():
    data =  ResponseInTicketDetailData(
        X_shop_id='30513',
        X_outou_kekka_kbn='04',
        X_tc_dai='001000',
        X_hakken_dai='001000',
        X_tc_kounyu_dai='001000',
        X_inshi_kijun='999999',
        X_ticket_cnt='03',
        tc_info_data='C',
        X_haraikomi='2100083826615',
        X_hikikae='2200083826612',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_C_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30513',
        X_outou_kekka_kbn='04',
        X_tc_dai='001000',
        X_hakken_dai='001000',
        X_tc_kounyu_dai='001000',
        X_inshi_kijun='999999',
        X_ticket_cnt='03',
        tc_info_data='C',
        X_haraikomi='2100083826615',
        X_hikikae='2200083826612',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_C_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_DETAIL_A_D():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30514"：チケットぴあ①
    応答結果区分 : 01：代引き
    チケット代金 : "003500"：一般値
    発券代金 : "001000"：一般値
    チケット購入代金 : "001000"：一般値
    印紙基準額 : "999999"：最大値
    チケット枚数 : 4
    券面情報データ : A+D
    """
    return '2100087759438'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_A_D():
    data =  ResponseInTicketDetailData(
        X_shop_id='30514',
        X_outou_kekka_kbn='01',
        X_tc_dai='003500',
        X_hakken_dai='001000',
        X_tc_kounyu_dai='001000',
        X_inshi_kijun='999999',
        X_ticket_cnt='04',
        tc_info_data='A_D',
        X_haraikomi='2100087759438',
        X_hikikae='2200087759435',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_A_D_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30514',
        X_outou_kekka_kbn='01',
        X_tc_dai='003500',
        X_hakken_dai='001000',
        X_tc_kounyu_dai='001000',
        X_inshi_kijun='999999',
        X_ticket_cnt='04',
        tc_info_data='A_D',
        X_haraikomi='2100087759438',
        X_hikikae='2200087759435',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_A_D_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_DETAIL_A_E():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30400"：7DC
    応答結果区分 : 02：前払い（後日発券）
    チケット代金 : "001000"：一般値
    発券代金 : "003500"：一般値
    チケット購入代金 : "001000"：一般値
    印紙基準額 : "999999"：最大値
    チケット枚数 : 5
    券面情報データ : A+E
    """
    return '2100010099938'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_A_E():
    data =  ResponseInTicketDetailData(
        X_shop_id='30400',
        X_outou_kekka_kbn='02',
        X_tc_dai='001000',
        X_hakken_dai='003500',
        X_tc_kounyu_dai='001000',
        X_inshi_kijun='999999',
        X_ticket_cnt='05',
        tc_info_data='A_E',
        X_haraikomi='2100010099938',
        X_hikikae='2200010099935',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_A_E_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30400',
        X_outou_kekka_kbn='02',
        X_tc_dai='001000',
        X_hakken_dai='003500',
        X_tc_kounyu_dai='001000',
        X_inshi_kijun='999999',
        X_ticket_cnt='05',
        tc_info_data='A_E',
        X_haraikomi='2100010099938',
        X_hikikae='2200010099935',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_A_E_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_DETAIL_A_F():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30501"：CNプレイガイド
    応答結果区分 : 03：代済発券
    チケット代金 : "001000"：一般値
    発券代金 : "001000"：一般値
    チケット購入代金 : "003500"：一般値
    印紙基準額 : "999999"：最大値
    チケット枚数 : 6
    券面情報データ : A+F
    """
    return '2100036560757'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_A_F():
    data =  ResponseInTicketDetailData(
        X_shop_id='30501',
        X_outou_kekka_kbn='03',
        X_tc_dai='001000',
        X_hakken_dai='001000',
        X_tc_kounyu_dai='003500',
        X_inshi_kijun='999999',
        X_ticket_cnt='06',
        tc_info_data='A_F',
        X_haraikomi='2100036560757',
        X_hikikae='2200036560754',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_A_F_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30501',
        X_outou_kekka_kbn='03',
        X_tc_dai='001000',
        X_hakken_dai='001000',
        X_tc_kounyu_dai='003500',
        X_inshi_kijun='999999',
        X_ticket_cnt='06',
        tc_info_data='A_F',
        X_haraikomi='2100036560757',
        X_hikikae='2200036560754',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_A_F_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_DETAIL_B_D():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30512"：旧ソフトバンクギフトショップ/組合せクーポンショップ
    応答結果区分 : 04：前払いのみ
    チケット代金 : "003500"：一般値
    発券代金 : "003500"：一般値
    チケット購入代金 : "001000"：一般値
    印紙基準額 : "999999"：最大値
    チケット枚数 : 7
    券面情報データ : B+D
    """
    return '2100061219330'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_B_D():
    data =  ResponseInTicketDetailData(
        X_shop_id='30512',
        X_outou_kekka_kbn='04',
        X_tc_dai='003500',
        X_hakken_dai='003500',
        X_tc_kounyu_dai='001000',
        X_inshi_kijun='999999',
        X_ticket_cnt='07',
        tc_info_data='B_D',
        X_haraikomi='2100061219330',
        X_hikikae='2200061219337',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_B_D_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30512',
        X_outou_kekka_kbn='04',
        X_tc_dai='003500',
        X_hakken_dai='003500',
        X_tc_kounyu_dai='001000',
        X_inshi_kijun='999999',
        X_ticket_cnt='07',
        tc_info_data='B_D',
        X_haraikomi='2100061219330',
        X_hikikae='2200061219337',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_B_D_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_DETAIL_B_E():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30513"：組合せクーポンショップ
    応答結果区分 : 01：代引き
    チケット代金 : "003500"：一般値
    発券代金 : "001000"：一般値
    チケット購入代金 : "003500"：一般値
    印紙基準額 : "999999"：最大値
    チケット枚数 : 8
    券面情報データ : B+E
    """
    return '2100066708631'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_B_E():
    data =  ResponseInTicketDetailData(
        X_shop_id='30513',
        X_outou_kekka_kbn='01',
        X_tc_dai='003500',
        X_hakken_dai='001000',
        X_tc_kounyu_dai='003500',
        X_inshi_kijun='999999',
        X_ticket_cnt='08',
        tc_info_data='B_E',
        X_haraikomi='2100066708631',
        X_hikikae='2200066708638',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_B_E_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30513',
        X_outou_kekka_kbn='01',
        X_tc_dai='003500',
        X_hakken_dai='001000',
        X_tc_kounyu_dai='003500',
        X_inshi_kijun='999999',
        X_ticket_cnt='08',
        tc_info_data='B_E',
        X_haraikomi='2100066708631',
        X_hikikae='2200066708638',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_B_E_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_DETAIL_B_F():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30514"：チケットぴあ①
    応答結果区分 : 02：前払い（後日発券）
    チケット代金 : "001000"：一般値
    発券代金 : "003500"：一般値
    チケット購入代金 : "003500"：一般値
    印紙基準額 : "999999"：最大値
    チケット枚数 : 9
    券面情報データ : B+F
    """
    return '2100093906734'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_B_F():
    data =  ResponseInTicketDetailData(
        X_shop_id='30514',
        X_outou_kekka_kbn='02',
        X_tc_dai='001000',
        X_hakken_dai='003500',
        X_tc_kounyu_dai='003500',
        X_inshi_kijun='999999',
        X_ticket_cnt='09',
        tc_info_data='B_F',
        X_haraikomi='2100093906734',
        X_hikikae='2200093906731',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_B_F_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30514',
        X_outou_kekka_kbn='02',
        X_tc_dai='001000',
        X_hakken_dai='003500',
        X_tc_kounyu_dai='003500',
        X_inshi_kijun='999999',
        X_ticket_cnt='09',
        tc_info_data='B_F',
        X_haraikomi='2100093906734',
        X_hikikae='2200093906731',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_B_F_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_DETAIL_C_D():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30400"：7DC
    応答結果区分 : 03：代済発券
    チケット代金 : "003500"：一般値
    発券代金 : "003500"：一般値
    チケット購入代金 : "003500"：一般値
    印紙基準額 : "999999"：最大値
    チケット枚数 : 10
    券面情報データ : C+D
    """
    return '2100013953473'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_C_D():
    data =  ResponseInTicketDetailData(
        X_shop_id='30400',
        X_outou_kekka_kbn='03',
        X_tc_dai='003500',
        X_hakken_dai='003500',
        X_tc_kounyu_dai='003500',
        X_inshi_kijun='999999',
        X_ticket_cnt='10',
        tc_info_data='C_D',
        X_haraikomi='2100013953473',
        X_hikikae='2200013953470',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_C_D_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30400',
        X_outou_kekka_kbn='03',
        X_tc_dai='003500',
        X_hakken_dai='003500',
        X_tc_kounyu_dai='003500',
        X_inshi_kijun='999999',
        X_ticket_cnt='10',
        tc_info_data='C_D',
        X_haraikomi='2100013953473',
        X_hikikae='2200013953470',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_C_D_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_DETAIL_C_E():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30501"：CNプレイガイド
    応答結果区分 : 04：前払いのみ
    チケット代金 : "001000"：一般値
    発券代金 : "001000"：一般値
    チケット購入代金 : "001000"：一般値
    印紙基準額 : "999999"：最大値
    チケット枚数 : 11
    券面情報データ : C+E
    """
    return '2100041888853'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_C_E():
    data =  ResponseInTicketDetailData(
        X_shop_id='30501',
        X_outou_kekka_kbn='04',
        X_tc_dai='001000',
        X_hakken_dai='001000',
        X_tc_kounyu_dai='001000',
        X_inshi_kijun='999999',
        X_ticket_cnt='11',
        tc_info_data='C_E',
        X_haraikomi='2100041888853',
        X_hikikae='2200041888850',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_C_E_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30501',
        X_outou_kekka_kbn='04',
        X_tc_dai='001000',
        X_hakken_dai='001000',
        X_tc_kounyu_dai='001000',
        X_inshi_kijun='999999',
        X_ticket_cnt='11',
        tc_info_data='C_E',
        X_haraikomi='2100041888853',
        X_hikikae='2200041888850',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_C_E_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_DETAIL_C_F():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30512"：旧ソフトバンクギフトショップ/組合せクーポンショップ
    応答結果区分 : 01：代引き
    チケット代金 : "003500"：一般値
    発券代金 : "001000"：一般値
    チケット購入代金 : "001000"：一般値
    印紙基準額 : "999999"：最大値
    チケット枚数 : 12
    券面情報データ : C+F
    """
    return '2100045821672'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_C_F():
    data =  ResponseInTicketDetailData(
        X_shop_id='30512',
        X_outou_kekka_kbn='01',
        X_tc_dai='003500',
        X_hakken_dai='001000',
        X_tc_kounyu_dai='001000',
        X_inshi_kijun='999999',
        X_ticket_cnt='12',
        tc_info_data='C_F',
        X_haraikomi='2100045821672',
        X_hikikae='2200045821679',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_C_F_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30512',
        X_outou_kekka_kbn='01',
        X_tc_dai='003500',
        X_hakken_dai='001000',
        X_tc_kounyu_dai='001000',
        X_inshi_kijun='999999',
        X_ticket_cnt='12',
        tc_info_data='C_F',
        X_haraikomi='2100045821672',
        X_hikikae='2200045821679',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_C_F_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_DETAIL_G():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30513"：組合せクーポンショップ
    応答結果区分 : 02：前払い（後日発券）
    チケット代金 : "001000"：一般値
    発券代金 : "003500"：一般値
    チケット購入代金 : "001000"：一般値
    印紙基準額 : "999999"：最大値
    チケット枚数 : 13
    券面情報データ : G
    """
    return '2100073019775'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_G():
    data =  ResponseInTicketDetailData(
        X_shop_id='30513',
        X_outou_kekka_kbn='02',
        X_tc_dai='001000',
        X_hakken_dai='003500',
        X_tc_kounyu_dai='001000',
        X_inshi_kijun='999999',
        X_ticket_cnt='13',
        tc_info_data='G',
        X_haraikomi='2100073019775',
        X_hikikae='2200073019772',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_G_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30513',
        X_outou_kekka_kbn='02',
        X_tc_dai='001000',
        X_hakken_dai='003500',
        X_tc_kounyu_dai='001000',
        X_inshi_kijun='999999',
        X_ticket_cnt='13',
        tc_info_data='G',
        X_haraikomi='2100073019775',
        X_hikikae='2200073019772',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_G_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_DETAIL_H01():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30514"：チケットぴあ①
    応答結果区分 : 03：代済発券
    チケット代金 : "001000"：一般値
    発券代金 : "001000"：一般値
    チケット購入代金 : "003500"：一般値
    印紙基準額 : "999999"：最大値
    チケット枚数 : 14
    券面情報データ : H01～02
    """
    return '2100099480597'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_H01():
    data =  ResponseInTicketDetailData(
        X_shop_id='30514',
        X_outou_kekka_kbn='03',
        X_tc_dai='001000',
        X_hakken_dai='001000',
        X_tc_kounyu_dai='003500',
        X_inshi_kijun='999999',
        X_ticket_cnt='14',
        tc_info_data='H01',
        X_haraikomi='2100099480597',
        X_hikikae='2200099480594',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_H01_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30514',
        X_outou_kekka_kbn='03',
        X_tc_dai='001000',
        X_hakken_dai='001000',
        X_tc_kounyu_dai='003500',
        X_inshi_kijun='999999',
        X_ticket_cnt='14',
        tc_info_data='H01',
        X_haraikomi='2100099480597',
        X_hikikae='2200099480594',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_H01_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)
def BARCODE_IN_TICKET_DETAIL_J01():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30400"：7DC
    応答結果区分 : 04：前払いのみ
    チケット代金 : "003500"：一般値
    発券代金 : "003500"：一般値
    チケット購入代金 : "001000"：一般値
    印紙基準額 : "999999"：最大値
    チケット枚数 : 15
    券面情報データ : J01～02
    """
    return '2100019281570'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_J01():
    data =  ResponseInTicketDetailData(
        X_shop_id='30400',
        X_outou_kekka_kbn='04',
        X_tc_dai='003500',
        X_hakken_dai='003500',
        X_tc_kounyu_dai='001000',
        X_inshi_kijun='999999',
        X_ticket_cnt='15',
        tc_info_data='J01',
        X_haraikomi='2100019281570',
        X_hikikae='2200019281577',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_J01_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30400',
        X_outou_kekka_kbn='04',
        X_tc_dai='003500',
        X_hakken_dai='003500',
        X_tc_kounyu_dai='001000',
        X_inshi_kijun='999999',
        X_ticket_cnt='15',
        tc_info_data='J01',
        X_haraikomi='2100019281570',
        X_hikikae='2200019281577',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_J01_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_DETAIL_K01():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30501"：CNプレイガイド
    応答結果区分 : 01：代引き
    チケット代金 : "003500"：一般値
    発券代金 : "001000"：一般値
    チケット購入代金 : "003500"：一般値
    印紙基準額 : "999999"：最大値
    チケット枚数 : 16
    券面情報データ : K01～04
    """
    return '2100024770878'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_K01():
    data =  ResponseInTicketDetailData(
        X_shop_id='30501',
        X_outou_kekka_kbn='01',
        X_tc_dai='003500',
        X_hakken_dai='001000',
        X_tc_kounyu_dai='003500',
        X_inshi_kijun='999999',
        X_ticket_cnt='16',
        tc_info_data='K01',
        X_haraikomi='2100024770878',
        X_hikikae='2200024770875',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_K01_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30501',
        X_outou_kekka_kbn='01',
        X_tc_dai='003500',
        X_hakken_dai='001000',
        X_tc_kounyu_dai='003500',
        X_inshi_kijun='999999',
        X_ticket_cnt='16',
        tc_info_data='K01',
        X_haraikomi='2100024770878',
        X_hikikae='2200024770875',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_K01_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_DETAIL_L01():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30512"：旧ソフトバンクギフトショップ/組合せクーポンショップ
    応答結果区分 : 02：前払い（後日発券）
    チケット代金 : "001000"：一般値
    発券代金 : "003500"：一般値
    チケット購入代金 : "003500"：一般値
    印紙基準額 : "999999"：最大値
    チケット枚数 : 17
    券面情報データ : L01～20
    """
    return '2100051968972'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_L01():
    data =  ResponseInTicketDetailData(
        X_shop_id='30512',
        X_outou_kekka_kbn='02',
        X_tc_dai='001000',
        X_hakken_dai='003500',
        X_tc_kounyu_dai='003500',
        X_inshi_kijun='999999',
        X_ticket_cnt='17',
        tc_info_data='L01',
        X_haraikomi='2100051968972',
        X_hikikae='2200051968979',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_L01_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30512',
        X_outou_kekka_kbn='02',
        X_tc_dai='001000',
        X_hakken_dai='003500',
        X_tc_kounyu_dai='003500',
        X_inshi_kijun='999999',
        X_ticket_cnt='17',
        tc_info_data='L01',
        X_haraikomi='2100051968972',
        X_hikikae='2200051968979',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_L01_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_DETAIL_M01():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30513"：組合せクーポンショップ
    応答結果区分 : 03：代済発券
    チケット代金 : "003500"：一般値
    発券代金 : "003500"：一般値
    チケット購入代金 : "003500"：一般値
    印紙基準額 : "999999"：最大値
    チケット枚数 : 18
    券面情報データ : M01～20
    """
    return '2100076873312'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_M01():
    data =  ResponseInTicketDetailData(
        X_shop_id='30513',
        X_outou_kekka_kbn='03',
        X_tc_dai='003500',
        X_hakken_dai='003500',
        X_tc_kounyu_dai='003500',
        X_inshi_kijun='999999',
        X_ticket_cnt='18',
        tc_info_data='M01',
        X_haraikomi='2100076873312',
        X_hikikae='2200076873319',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_M01_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30513',
        X_outou_kekka_kbn='03',
        X_tc_dai='003500',
        X_hakken_dai='003500',
        X_tc_kounyu_dai='003500',
        X_inshi_kijun='999999',
        X_ticket_cnt='18',
        tc_info_data='M01',
        X_haraikomi='2100076873312',
        X_hikikae='2200076873319',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_M01_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_DETAIL_N01():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30514"：チケットぴあ①
    応答結果区分 : 04：前払いのみ
    チケット代金 : "001000"：一般値
    発券代金 : "001000"：一般値
    チケット購入代金 : "001000"：一般値
    印紙基準額 : "999999"：最大値
    チケット枚数 : 19
    券面情報データ : N01～20
    """
    return '2100104808699'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_N01():
    data =  ResponseInTicketDetailData(
        X_shop_id='30514',
        X_outou_kekka_kbn='04',
        X_tc_dai='001000',
        X_hakken_dai='001000',
        X_tc_kounyu_dai='001000',
        X_inshi_kijun='999999',
        X_ticket_cnt='19',
        tc_info_data='N01',
        X_haraikomi='2100104808699',
        X_hikikae='2200104808696',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_N01_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30514',
        X_outou_kekka_kbn='04',
        X_tc_dai='001000',
        X_hakken_dai='001000',
        X_tc_kounyu_dai='001000',
        X_inshi_kijun='999999',
        X_ticket_cnt='19',
        tc_info_data='N01',
        X_haraikomi='2100104808699',
        X_hikikae='2200104808696',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_N01_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_DETAIL_P01():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30400"：7DC
    応答結果区分 : 01：代引き
    チケット代金 : "003500"：一般値
    発券代金 : "001000"：一般値
    チケット購入代金 : "001000"：一般値
    印紙基準額 : "999999"：最大値
    チケット枚数 : 20
    券面情報データ : P01～20
    """
    return '2100003883919'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_P01():
    data =  ResponseInTicketDetailData(
        X_shop_id='30400',
        X_outou_kekka_kbn='01',
        X_tc_dai='003500',
        X_hakken_dai='001000',
        X_tc_kounyu_dai='001000',
        X_inshi_kijun='999999',
        X_ticket_cnt='20',
        tc_info_data='P01',
        X_haraikomi='2100003883919',
        X_hikikae='2200003883916',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_P01_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30400',
        X_outou_kekka_kbn='01',
        X_tc_dai='003500',
        X_hakken_dai='001000',
        X_tc_kounyu_dai='001000',
        X_inshi_kijun='999999',
        X_ticket_cnt='20',
        tc_info_data='P01',
        X_haraikomi='2100003883919',
        X_hikikae='2200003883916',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_P01_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_DETAIL_R01():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30501"：CNプレイガイド
    応答結果区分 : 02：前払い（後日発券）
    チケット代金 : "001000"：一般値
    発券代金 : "003500"：一般値
    チケット購入代金 : "001000"：一般値
    印紙基準額 : "999999"：最大値
    チケット枚数 : 1
    券面情報データ : R01～20
    """
    return '2100031069217'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_R01():
    data =  ResponseInTicketDetailData(
        X_shop_id='30501',
        X_outou_kekka_kbn='02',
        X_tc_dai='001000',
        X_hakken_dai='003500',
        X_tc_kounyu_dai='001000',
        X_inshi_kijun='999999',
        X_ticket_cnt='01',
        tc_info_data='R01',
        X_haraikomi='2100031069217',
        X_hikikae='2200031069214',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_R01_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30501',
        X_outou_kekka_kbn='02',
        X_tc_dai='001000',
        X_hakken_dai='003500',
        X_tc_kounyu_dai='001000',
        X_inshi_kijun='999999',
        X_ticket_cnt='01',
        tc_info_data='R01',
        X_haraikomi='2100031069217',
        X_hikikae='2200031069214',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_R01_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_DETAIL_S01():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30512"：旧ソフトバンクギフトショップ/組合せクーポンショップ
    応答結果区分 : 03：代済発券
    チケット代金 : "001000"：一般値
    発券代金 : "001000"：一般値
    チケット購入代金 : "003500"：一般値
    印紙基準額 : "999999"：最大値
    チケット枚数 : 2
    券面情報データ : S01～20
    """
    return '2100057530036'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_S01():
    data =  ResponseInTicketDetailData(
        X_shop_id='30512',
        X_outou_kekka_kbn='03',
        X_tc_dai='001000',
        X_hakken_dai='001000',
        X_tc_kounyu_dai='003500',
        X_inshi_kijun='999999',
        X_ticket_cnt='02',
        tc_info_data='S01',
        X_haraikomi='2100057530036',
        X_hikikae='2200057530033',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_S01_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30512',
        X_outou_kekka_kbn='03',
        X_tc_dai='001000',
        X_hakken_dai='001000',
        X_tc_kounyu_dai='003500',
        X_inshi_kijun='999999',
        X_ticket_cnt='02',
        tc_info_data='S01',
        X_haraikomi='2100057530036',
        X_hikikae='2200057530033',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_S01_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_DETAIL_TU():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30701"：Mコピーインターネットチケット①
    応答結果区分 : 01：代引き
    チケット代金 : "003500"：一般値
    発券代金 : "001000"：一般値
    チケット購入代金 : "003500"：一般値
    印紙基準額 : "003500"：一般値
    チケット枚数 : 2
    券面情報データ : T+U
    """
    return '2100119154378'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_TU():
    data =  ResponseInTicketDetailData(
        X_shop_id='30701',
        X_outou_kekka_kbn='03',
        X_tc_dai='003500',
        X_hakken_dai='001000',
        X_tc_kounyu_dai='003500',
        X_inshi_kijun='003500',
        X_ticket_cnt='02',
        tc_info_data='T_U',
        X_haraikomi='2100119154378',
        X_hikikae='2200119154375',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_TU_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30701',
        X_outou_kekka_kbn='03',
        X_tc_dai='003500',
        X_hakken_dai='001000',
        X_tc_kounyu_dai='003500',
        X_inshi_kijun='003500',
        X_ticket_cnt='02',
        tc_info_data='T_U',
        X_haraikomi='2100119154378',
        X_hikikae='2200119154375',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_TU_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_DETAIL_VW():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30705"：WEBインターネットチケット①
    応答結果区分 : 01：代引き
    チケット代金 : "003500"：一般値
    発券代金 : "001000"：一般値
    チケット購入代金 : "003500"：一般値
    印紙基準額 : "003500"：一般値
    チケット枚数 : 2
    券面情報データ : V+W
    """
    return '2100213526231'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_VW():
    data =  ResponseInTicketDetailData(
        X_shop_id='30705',
        X_outou_kekka_kbn='01',
        X_tc_dai='003500',
        X_hakken_dai='001000',
        X_tc_kounyu_dai='003500',
        X_inshi_kijun='003500',
        X_ticket_cnt='02',
        tc_info_data='V_W',
        X_haraikomi='2100213526231',
        X_hikikae='2200213526238',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_VW_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30705',
        X_outou_kekka_kbn='01',
        X_tc_dai='003500',
        X_hakken_dai='001000',
        X_tc_kounyu_dai='003500',
        X_inshi_kijun='003500',
        X_ticket_cnt='02',
        tc_info_data='V_W',
        X_haraikomi='2100213526231',
        X_hikikae='2200213526238',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_VW_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_DETAIL_CASE_01():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30701"：Mコピーインターネットチケット①
    応答結果区分 : 01：代引き
    チケット代金 : "999999"：最大値
    発券代金 : "000000"：最低値
    チケット購入代金 : "000000"：最低値
    印紙基準額 : "999999"：最大値
    チケット枚数 : 0
    券面情報データ : A
    """
    return '2100106188812'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_01():
    data =  ResponseInTicketDetailData(
        X_shop_id='30701',
        X_outou_kekka_kbn='01',
        X_tc_dai='999999',
        X_inshi_kijun='999999',
        tc_info_data='A',
        X_haraikomi='2100106188812',
        X_hikikae='2200106188819',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_01_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30701',
        X_outou_kekka_kbn='01',
        X_tc_dai='999999',
        X_inshi_kijun='999999',
        tc_info_data='A',
        X_haraikomi='2100106188812',
        X_hikikae='2200106188819',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_01_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_DETAIL_CASE_02():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30731"：チケットぴあ②
    応答結果区分 : 01：代引き
    チケット代金 : "999999"：最大値
    発券代金 : "000000"：最低値
    チケット購入代金 : "000000"：最低値
    印紙基準額 : "999999"：最大値
    チケット枚数 : 0
    券面情報データ : A
    """
    return '2100127160330'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_02():
    data =  ResponseInTicketDetailData(
        X_shop_id='30731',
        X_outou_kekka_kbn='01',
        X_tc_dai='999999',
        X_inshi_kijun='999999',
        tc_info_data='A',
        X_haraikomi='2100127160330',
        X_hikikae='2200127160337',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_02_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30731',
        X_outou_kekka_kbn='01',
        X_tc_dai='999999',
        X_inshi_kijun='999999',
        tc_info_data='A',
        X_haraikomi='2100127160330',
        X_hikikae='2200127160337',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_02_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_DETAIL_CASE_03():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30732"：チケットぴあ③
    応答結果区分 : 01：代引き
    チケット代金 : "999999"：最大値
    発券代金 : "000000"：最低値
    チケット購入代金 : "000000"：最低値
    印紙基準額 : "999999"：最大値
    チケット枚数 : 0
    券面情報データ : A
    """
    return '2100148131852'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_03():
    data =  ResponseInTicketDetailData(
        X_shop_id='30732',
        X_outou_kekka_kbn='01',
        X_tc_dai='999999',
        X_inshi_kijun='999999',
        tc_info_data='A',
        X_haraikomi='2100148131852',
        X_hikikae='2200148131859',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_03_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30732',
        X_outou_kekka_kbn='01',
        X_tc_dai='999999',
        X_inshi_kijun='999999',
        tc_info_data='A',
        X_haraikomi='2100148131852',
        X_hikikae='2200148131859',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_03_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_DETAIL_CASE_04():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30773"：Mコピーインターネットチケット②
    応答結果区分 : 01：代引き
    チケット代金 : "999999"：最大値
    発券代金 : "000000"：最低値
    チケット購入代金 : "000000"：最低値
    印紙基準額 : "999999"：最大値
    チケット枚数 : 0
    券面情報データ : A
    """
    return '2100169103371'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_04():
    data =  ResponseInTicketDetailData(
        X_shop_id='30773',
        X_outou_kekka_kbn='01',
        X_tc_dai='999999',
        X_inshi_kijun='999999',
        tc_info_data='A',
        X_haraikomi='2100169103371',
        X_hikikae='2200169103378',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_04_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30773',
        X_outou_kekka_kbn='01',
        X_tc_dai='999999',
        X_inshi_kijun='999999',
        tc_info_data='A',
        X_haraikomi='2100169103371',
        X_hikikae='2200169103378',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_04_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

def BARCODE_IN_TICKET_DETAIL_CASE_05():
    """
    正常系　払込票番号 生成時選択肢
    --------
    ショップＩＤ : "30775"：JTBレジャー（TDR）
    応答結果区分 : 01：代引き
    チケット代金 : "999999"：最大値
    発券代金 : "000000"：最低値
    チケット購入代金 : "000000"：最低値
    印紙基準額 : "999999"：最大値
    チケット枚数 : 0
    券面情報データ : A
    """
    return '2100190074893'
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_05():
    data =  ResponseInTicketDetailData(
        X_shop_id='30775',
        X_outou_kekka_kbn='01',
        X_tc_dai='999999',
        X_inshi_kijun='999999',
        tc_info_data='A',
        X_haraikomi='2100190074893',
        X_hikikae='2200190074890',
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_05_CANCEL():
    data =  ResponseInTicketDetailData(
        X_shop_id='30775',
        X_outou_kekka_kbn='01',
        X_tc_dai='999999',
        X_inshi_kijun='999999',
        tc_info_data='A',
        X_haraikomi='2100190074893',
        X_hikikae='2200190074890',
        is_cancel=True,
    )
    return COMPARE_IN_TICKET_DICT(data)
def RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_05_KANRYO():
    data =  ResponseInTicketDetailData()
    return COMPARE_IN_TICKET_KANRYO_DICT(data)

