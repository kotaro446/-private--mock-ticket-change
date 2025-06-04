from test_barcode_functions import *

# ---------------------------
# Mcopyチケット マッピングNo1 EC関連問合せ
# ---------------------------
def BARCODE_MCOPY_TICKET_CASE_01():
    return '6000013358086'
def KESSAI_KEY_MCOPY_TICKET_CASE_01():
    """
    正常系　決済キー 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常（決済可能）
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : " "（半角空白）：預り金計上
    印紙基準額 : "001000"：一般値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00236"：オリンピックチケット
    収納金額 : "001000"：一般値
    チケット発券個別情報 : 1件
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    """
    return BARCODE_MCOPY_TICKET_CASE_01()[1:12]
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_01():
    data =  ResponseEcTicketData(
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_01_CANCEL():
    data =  ResponseEcTicketData(
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_01_KANRYO():
    data =  ResponseEcTicketData(
        shop_id='00236',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_MCOPY_TICKET_CASE_02():
    return '6000264852487'
def KESSAI_KEY_MCOPY_TICKET_CASE_02():
    """
    正常系　決済キー 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常（決済可能）
    支払種別 : "2"：代金引換
    納品種別 : "2"：宅配
    売上計上区分 : " "（半角空白）：預り金計上
    印紙基準額 : "001000"：一般値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00000"：オリンピックチケット以外
    収納金額 : "001000"：一般値
    チケット発券個別情報 : 1件
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    """
    return BARCODE_MCOPY_TICKET_CASE_02()[1:12]
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_02():
    data =  ResponseEcTicketData(
        pay_type='2',
        dlv_type='2',
        inshi_kijun='001000',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_02_CANCEL():
    data =  ResponseEcTicketData(
        pay_type='2',
        dlv_type='2',
        inshi_kijun='001000',
        shuno_kingaku='001000',
        ticket_count=1,
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_02_KANRYO():
    data =  ResponseEcTicketData(
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_MCOPY_TICKET_CASE_03():
    return '6000370037761'
def KESSAI_KEY_MCOPY_TICKET_CASE_03():
    """
    正常系　決済キー 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常（決済可能）
    支払種別 : "3"：後払い
    納品種別 : "1"：店渡し
    売上計上区分 : "1"：売上計上
    印紙基準額 : "001000"：一般値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00245"：一般値
    収納金額 : "001000"：一般値
    チケット発券個別情報 : 1件
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    """
    return BARCODE_MCOPY_TICKET_CASE_03()[1:12]
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_03():
    data =  ResponseEcTicketData(
        pay_type='3',
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00245',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_03_CANCEL():
    data =  ResponseEcTicketData(
        pay_type='3',
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00245',
        shuno_kingaku='001000',
        ticket_count=1,
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_03_KANRYO():
    data =  ResponseEcTicketData(
        shop_id='00245',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_MCOPY_TICKET_CASE_04():
    return '6000034657601'
def KESSAI_KEY_MCOPY_TICKET_CASE_04():
    """
    正常系　決済キー 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常（決済可能）
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : "1"：売上計上
    印紙基準額 : "001000"：一般値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00745"：一般値
    収納金額 : "001000"：一般値
    チケット発券個別情報 : 1件
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "10"：電文区分エラー
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    """
    return BARCODE_MCOPY_TICKET_CASE_04()[1:12]
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_04():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00745',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_04_CANCEL():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00745',
        shuno_kingaku='001000',
        ticket_count=1,
        shori_kekka='10',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_04_CANCEL_RETRY():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00745',
        shuno_kingaku='001000',
        ticket_count=1,
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_04_KANRYO():
    data =  ResponseEcTicketData(
        shop_id='00745',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_MCOPY_TICKET_CASE_05():
    return '6000210422405'
def KESSAI_KEY_MCOPY_TICKET_CASE_05():
    """
    正常系　決済キー 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常（決済可能）
    支払種別 : "2"：代金引換
    納品種別 : "1"：店渡し
    売上計上区分 : "2"：売上計上/未収入金計上
    印紙基準額 : "      "（ALL半角空白）
    価格変更フラグ : " "（半角空白）：下記以外の場合
    機能区分 : "3"：チケット発券
    SHOPCD : "30731"：ぴあ
    収納金額 : "000000"：最低値
    チケット発券個別情報 : 2件
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "11"：業務区分エラー
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    """
    return BARCODE_MCOPY_TICKET_CASE_05()[1:12]
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_05():
    data =  ResponseEcTicketData(
        pay_type='2',
        keijyo_type='2',
        kingaku_henko_flg=' ',
        shop_id='30731',
        shuno_kingaku='000000',
        ticket_count=2,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_05_CANCEL():
    data =  ResponseEcTicketData(
        pay_type='2',
        keijyo_type='2',
        kingaku_henko_flg=' ',
        shop_id='30731',
        shuno_kingaku='000000',
        ticket_count=2,
        shori_kekka='11',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_05_CANCEL_RETRY():
    data =  ResponseEcTicketData(
        pay_type='2',
        keijyo_type='2',
        kingaku_henko_flg=' ',
        shop_id='30731',
        shuno_kingaku='000000',
        ticket_count=2,
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_05_KANRYO():
    data =  ResponseEcTicketData(
        shop_id='30731',
        shuno_kingaku='000000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_MCOPY_TICKET_CASE_06():
    return '6000386965447'
def KESSAI_KEY_MCOPY_TICKET_CASE_06():
    """
    正常系　決済キー 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常（決済可能）
    支払種別 : "3"：後払い
    納品種別 : "1"：店渡し
    売上計上区分 : "2"：売上計上/未収入金計上
    印紙基準額 : "000000"：最低値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "5"：新プリペイドサービス
    SHOPCD : "00236"：オリンピックチケット
    収納金額 : "999999"：最大値
    チケット発券個別情報 : 10件
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "14"：サービス時間帯エラー
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    """
    return BARCODE_MCOPY_TICKET_CASE_06()[1:12]
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_06():
    data =  ResponseEcTicketData(
        pay_type='3',
        keijyo_type='2',
        inshi_kijun='000000',
        kino_kbn='5',
        shop_id='00236',
        shuno_kingaku='999999',
        ticket_count=10,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_06_CANCEL():
    data =  ResponseEcTicketData(
        pay_type='3',
        keijyo_type='2',
        inshi_kijun='000000',
        kino_kbn='5',
        shop_id='00236',
        shuno_kingaku='999999',
        ticket_count=10,
        shori_kekka='14',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_06_CANCEL_RETRY():
    data =  ResponseEcTicketData(
        pay_type='3',
        keijyo_type='2',
        inshi_kijun='000000',
        kino_kbn='5',
        shop_id='00236',
        shuno_kingaku='999999',
        ticket_count=10,
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_06_KANRYO():
    data =  ResponseEcTicketData(
        kino_kbn='5',
        shop_id='00236',
        shuno_kingaku='999999',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_MCOPY_TICKET_CASE_07():
    return '6000040736048'
def KESSAI_KEY_MCOPY_TICKET_CASE_07():
    """
    正常系　決済キー 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常（決済可能）
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : "1"：売上計上
    印紙基準額 : "999999"：最大値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "5"：新プリペイドサービス
    SHOPCD : "00000"：オリンピックチケット以外
    収納金額 : "001000"：一般値
    チケット発券個別情報 : 20件
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "99"：その他エラー(400)
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "1"：再送異常
    """
    return BARCODE_MCOPY_TICKET_CASE_07()[1:12]
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_07():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='999999',
        kino_kbn='5',
        shuno_kingaku='001000',
        ticket_count=20,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_07_CANCEL():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='999999',
        kino_kbn='5',
        shuno_kingaku='001000',
        ticket_count=20,
        shori_kekka='99',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_07_KANRYO():
    data =  ResponseEcTicketData(
        kino_kbn='5',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_MCOPY_TICKET_CASE_08():
    return '6000035800686'
def KESSAI_KEY_MCOPY_TICKET_CASE_08():
    """
    正常系　決済キー 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常（決済可能）
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : "1"：売上計上
    印紙基準額 : "001000"：一般値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "5"：新プリペイドサービス
    SHOPCD : "00245"：一般値
    収納金額 : "001000"：一般値
    チケット発券個別情報 : 0件
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "99"：その他エラー(500)
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "1"：再送異常
    """
    return BARCODE_MCOPY_TICKET_CASE_08()[1:12]
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_08():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        kino_kbn='5',
        shop_id='00245',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_08_CANCEL():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        kino_kbn='5',
        shop_id='00245',
        shuno_kingaku='001000',
        shori_kekka='99',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_08_KANRYO():
    data =  ResponseEcTicketData(
        kino_kbn='5',
        shop_id='00245',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_MCOPY_TICKET_CASE_09():
    return '6000034659209'
def KESSAI_KEY_MCOPY_TICKET_CASE_09():
    """
    正常系　決済キー 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常（決済可能）
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : "1"：売上計上
    印紙基準額 : "001000"：一般値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00745"：一般値
    収納金額 : "001000"：一般値
    チケット発券個別情報 : 1件
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：タイムアウト(正常)
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    """
    return BARCODE_MCOPY_TICKET_CASE_09()[1:12]
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_09():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00745',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_09_CANCEL():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00745',
        shuno_kingaku='001000',
        ticket_count=1,
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_09_KANRYO():
    data =  ResponseEcTicketData(
        shop_id='00745',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_MCOPY_TICKET_CASE_10():
    return '6000034823365'
def KESSAI_KEY_MCOPY_TICKET_CASE_10():
    """
    正常系　決済キー 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常（決済可能）
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : "1"：売上計上
    印紙基準額 : "001000"：一般値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "3"：チケット発券
    SHOPCD : "30731"：ぴあ
    収納金額 : "001000"：一般値
    チケット発券個別情報 : 1件
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "99"：タイムアウト(その他エラー500)
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    """
    return BARCODE_MCOPY_TICKET_CASE_10()[1:12]
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_10():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='30731',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_10_CANCEL():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='30731',
        shuno_kingaku='001000',
        ticket_count=1,
        shori_kekka='99',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_10_CANCEL_RETRY():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='30731',
        shuno_kingaku='001000',
        ticket_count=1,
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_10_KANRYO():
    data =  ResponseEcTicketData(
        shop_id='30731',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_MCOPY_TICKET_SYORI_KEKKA_10():
    return '6010771747848'
def KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_10():
    """
    正常系　決済キー 生成時選択肢
    --------
    処理結果 : "10"：電文区分エラー
    応答結果 : "00"：正常（決済可能）
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : "1"：売上計上
    印紙基準額 : "001000"：一般値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00236"：オリンピックチケット
    収納金額 : "001000"：一般値
    チケット発券個別情報 : 1件
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    """
    return BARCODE_MCOPY_TICKET_SYORI_KEKKA_10()[1:12]
def RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_10():
    data =  ResponseEcTicketData(
        shori_kekka='10',
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_10_RETRY():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_10_CANCEL():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_10_KANRYO():
    data =  ResponseEcTicketData(
        shop_id='00236',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_MCOPY_TICKET_SYORI_KEKKA_11():
    return '6021509166169'
def KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_11():
    """
    正常系　決済キー 生成時選択肢
    --------
    処理結果 : "11"：業務区分エラー
    応答結果 : "00"：正常（決済可能）
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : "1"：売上計上
    印紙基準額 : "001000"：一般値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00236"：オリンピックチケット
    収納金額 : "001000"：一般値
    チケット発券個別情報 : 1件
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "01"：取消異常(検索キーエラー)
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    """
    return BARCODE_MCOPY_TICKET_SYORI_KEKKA_11()[1:12]
def RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_11():
    data =  ResponseEcTicketData(
        shori_kekka='11',
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_11_RETRY():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_11_CANCEL():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
        oto_kekka='01',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_11_CANCEL_RETRY():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_11_KANRYO():
    data =  ResponseEcTicketData(
        shop_id='00236',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_MCOPY_TICKET_SYORI_KEKKA_14():
    return '6032246584482'
def KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_14():
    """
    正常系　決済キー 生成時選択肢
    --------
    処理結果 : "14"：サービス時間帯エラー
    応答結果 : "00"：正常（決済可能）
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : "1"：売上計上
    印紙基準額 : "001000"：一般値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00236"：オリンピックチケット
    収納金額 : "001000"：一般値
    チケット発券個別情報 : 1件
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "04"：取消異常(取消済み)
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    """
    return BARCODE_MCOPY_TICKET_SYORI_KEKKA_14()[1:12]
def RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_14():
    data =  ResponseEcTicketData(
        shori_kekka='14',
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_14_RETRY():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_14_CANCEL():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
        oto_kekka='04',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_14_CANCEL_RETRY():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_14_KANRYO():
    data =  ResponseEcTicketData(
        shop_id='00236',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_MCOPY_TICKET_SYORI_KEKKA_99_400():
    return '6042984002803'
def KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_99_400():
    """
    正常系　決済キー 生成時選択肢
    --------
    処理結果 : "99"：その他エラー(400)
    応答結果 : "00"：正常（決済可能）
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : "1"：売上計上
    印紙基準額 : "001000"：一般値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00236"：オリンピックチケット
    収納金額 : "001000"：一般値
    チケット発券個別情報 : 1件
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "99"：取消異常(その他エラー)
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    """
    return BARCODE_MCOPY_TICKET_SYORI_KEKKA_99_400()[1:12]
def RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_99_400():
    data =  ResponseEcTicketData(
        shori_kekka='99',
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_99_400_RETRY():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_99_400_CANCEL():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
        oto_kekka='99',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_99_400_CANCEL_RETRY():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_99_400_KANRYO():
    data =  ResponseEcTicketData(
        shop_id='00236',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_MCOPY_TICKET_SYORI_KEKKA_99_500():
    return '6053721423362'
def KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_99_500():
    """
    正常系　決済キー 生成時選択肢
    --------
    処理結果 : "99"：その他エラー(500)
    応答結果 : "00"：正常（決済可能）
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : "1"：売上計上
    印紙基準額 : "001000"：一般値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00236"：オリンピックチケット
    収納金額 : "001000"：一般値
    チケット発券個別情報 : 1件
    レスポンスパターン（再送区分用） : "1"：再送異常
    取消処理結果 : "00"：正常
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    """
    return BARCODE_MCOPY_TICKET_SYORI_KEKKA_99_500()[1:12]
def RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_99_500():
    data =  ResponseEcTicketData(
        shori_kekka='99',
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_99_500_CANCEL():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_99_500_KANRYO():
    data =  ResponseEcTicketData(
        shop_id='00236',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)
def BARCODE_MCOPY_TICKET_SYORI_KEKKA_TIMEOUT():
    return '6064458839043'
def KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_TIMEOUT():
    """
    正常系　決済キー 生成時選択肢
    --------
    処理結果 : "00"：タイムアウト(正常)
    応答結果 : "00"：正常（決済可能）
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : "1"：売上計上
    印紙基準額 : "001000"：一般値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00236"：オリンピックチケット
    収納金額 : "001000"：一般値
    チケット発券個別情報 : 1件
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    """
    return BARCODE_MCOPY_TICKET_SYORI_KEKKA_TIMEOUT()[1:12]
def RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_TIMEOUT():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_TIMEOUT_CANCEL():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_TIMEOUT_KANRYO():
    data =  ResponseEcTicketData(
        shop_id='00236',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_MCOPY_TICKET_SYORI_KEKKA_TIMEOUT_99():
    return '6075196257723'
def KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_TIMEOUT_99():
    """
    正常系　決済キー 生成時選択肢
    --------
    処理結果 : "99"：タイムアウト(その他エラー500)
    応答結果 : "00"：正常（決済可能）
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : "1"：売上計上
    印紙基準額 : "001000"：一般値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00236"：オリンピックチケット
    収納金額 : "001000"：一般値
    チケット発券個別情報 : 1件
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "10"：電文区分エラー
    取消応答結果 : "01"：取消異常(検索キーエラー)
    レスポンスパターン（取消再送区分用） : "1"：再送異常
    """
    return BARCODE_MCOPY_TICKET_SYORI_KEKKA_TIMEOUT_99()[1:12]
def RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_TIMEOUT_99():
    data =  ResponseEcTicketData(
        shori_kekka='99',
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_TIMEOUT_99_RETRY():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_TIMEOUT_99_CANCEL():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
        shori_kekka='10',
        oto_kekka='01',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_TIMEOUT_99_KANRYO():
    data =  ResponseEcTicketData(
        shop_id='00236',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_MCOPY_TICKET_OTO_KEKKA_01():
    return '6000705418968'
def KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_01():
    """
    正常系　決済キー 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "01"：検索キーエラー
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : "1"：売上計上
    印紙基準額 : "001000"：一般値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00236"：オリンピックチケット
    収納金額 : "001000"：一般値
    チケット発券個別情報 : 1件
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "11"：業務区分エラー
    取消応答結果 : "01"：取消異常(検索キーエラー)
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    """
    return BARCODE_MCOPY_TICKET_OTO_KEKKA_01()[1:12]
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_01():
    data =  ResponseEcTicketData(
        oto_kekka='01',
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_01_RETRY():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_01_CANCEL():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
        shori_kekka='11',
        oto_kekka='01',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_01_CANCEL_RETRY():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_01_KANRYO():
    data =  ResponseEcTicketData(
        shop_id='00236',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_MCOPY_TICKET_OTO_KEKKA_02():
    return '6001376507968'
def KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_02():
    """
    正常系　決済キー 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "02"：支払期限エラー
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : "1"：売上計上
    印紙基準額 : "001000"：一般値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00236"：オリンピックチケット
    収納金額 : "001000"：一般値
    チケット発券個別情報 : 1件
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "14"：サービス時間帯エラー
    取消応答結果 : "01"：取消異常(検索キーエラー)
    レスポンスパターン（取消再送区分用） : "1"：再送異常
    """
    return BARCODE_MCOPY_TICKET_OTO_KEKKA_02()[1:12]
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_02():
    data =  ResponseEcTicketData(
        oto_kekka='02',
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_02_RETRY():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_02_CANCEL():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
        shori_kekka='14',
        oto_kekka='01',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_02_KANRYO():
    data =  ResponseEcTicketData(
        shop_id='00236',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_MCOPY_TICKET_OTO_KEKKA_03():
    return '6002047598162'
def KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_03():
    """
    正常系　決済キー 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "03"：支払済み
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : "1"：売上計上
    印紙基準額 : "001000"：一般値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00236"：オリンピックチケット
    収納金額 : "001000"：一般値
    チケット発券個別情報 : 1件
    レスポンスパターン（再送区分用） : "1"：再送異常
    取消処理結果 : "00"：正常
    取消応答結果 : "01"：取消異常(検索キーエラー)
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    """
    return BARCODE_MCOPY_TICKET_OTO_KEKKA_03()[1:12]
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_03():
    data =  ResponseEcTicketData(
        oto_kekka='03',
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_03_CANCEL():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
        oto_kekka='01',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_03_CANCEL_RETRY():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_03_KANRYO():
    data =  ResponseEcTicketData(
        shop_id='00236',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_MCOPY_TICKET_OTO_KEKKA_05():
    return '6002718684323'
def KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_05():
    """
    正常系　決済キー 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "05"：決済中止
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : "1"：売上計上
    印紙基準額 : "001000"：一般値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00236"：オリンピックチケット
    収納金額 : "001000"：一般値
    チケット発券個別情報 : 1件
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "04"：取消異常(取消済み)
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    """
    return BARCODE_MCOPY_TICKET_OTO_KEKKA_05()[1:12]
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_05():
    data =  ResponseEcTicketData(
        oto_kekka='05',
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_05_RETRY():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_05_CANCEL():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
        oto_kekka='04',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_05_CANCEL_RETRY():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_05_KANRYO():
    data =  ResponseEcTicketData(
        shop_id='00236',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_MCOPY_TICKET_OTO_KEKKA_11():
    return '6003389773040'
def KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_11():
    """
    正常系　決済キー 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "11"：店舗指定エラー
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : "1"：売上計上
    印紙基準額 : "001000"：一般値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00236"：オリンピックチケット
    収納金額 : "001000"：一般値
    チケット発券個別情報 : 1件
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "99"：取消異常(その他エラー)
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    """
    return BARCODE_MCOPY_TICKET_OTO_KEKKA_11()[1:12]
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_11():
    data =  ResponseEcTicketData(
        oto_kekka='11',
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_11_RETRY():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_11_CANCEL():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
        oto_kekka='99',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_11_CANCEL_RETRY():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_11_KANRYO():
    data =  ResponseEcTicketData(
        shop_id='00236',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_MCOPY_TICKET_OTO_KEKKA_12():
    return '6004060861520'
def KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_12():
    """
    正常系　決済キー 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "12"：店舗引渡中止
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : "1"：売上計上
    印紙基準額 : "001000"：一般値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00236"：オリンピックチケット
    収納金額 : "001000"：一般値
    チケット発券個別情報 : 1件
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "01"：取消異常(検索キーエラー)
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    """
    return BARCODE_MCOPY_TICKET_OTO_KEKKA_12()[1:12]
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_12():
    data =  ResponseEcTicketData(
        oto_kekka='12',
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_12_RETRY():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_12_CANCEL():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
        oto_kekka='01',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_12_CANCEL_RETRY():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_12_KANRYO():
    data =  ResponseEcTicketData(
        shop_id='00236',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_MCOPY_TICKET_OTO_KEKKA_16():
    return '6004731950164'
def KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_16():
    """
    正常系　決済キー 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "16"：受付中
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : "1"：売上計上
    印紙基準額 : "001000"：一般値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00236"：オリンピックチケット
    収納金額 : "001000"：一般値
    チケット発券個別情報 : 1件
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "01"：取消異常(検索キーエラー)
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    """
    return BARCODE_MCOPY_TICKET_OTO_KEKKA_16()[1:12]
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_16():
    data =  ResponseEcTicketData(
        oto_kekka='16',
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_16_RETRY():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_16_CANCEL():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
        oto_kekka='01',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_16_CANCEL_RETRY():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_16_KANRYO():
    data =  ResponseEcTicketData(
        shop_id='00236',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_MCOPY_TICKET_OTO_KEKKA_99():
    return '6005403038807'
def KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_99():
    """
    正常系　決済キー 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "99"：その他エラー
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : "1"：売上計上
    印紙基準額 : "001000"：一般値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00236"：オリンピックチケット
    収納金額 : "001000"：一般値
    チケット発券個別情報 : 1件
    レスポンスパターン（再送区分用） : "0"：再送正常
    取消処理結果 : "00"：正常
    取消応答結果 : "01"：取消異常(検索キーエラー)
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    """
    return BARCODE_MCOPY_TICKET_OTO_KEKKA_99()[1:12]
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_99():
    data =  ResponseEcTicketData(
        oto_kekka='99',
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_99_RETRY():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_99_CANCEL():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
        oto_kekka='01',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_99_CANCEL_RETRY():
    data =  ResponseEcTicketData(
        keijyo_type='1',
        inshi_kijun='001000',
        shop_id='00236',
        shuno_kingaku='001000',
        ticket_count=1,
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_99_KANRYO():
    data =  ResponseEcTicketData(
        shop_id='00236',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)


# ---------------------------
# Mcopyチケット マッピングNo2 EC関連払戻
# ---------------------------
def BARCODE_TICKET_REPAY_CASE_01():
    """
    正常系　払戻バーコード 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常（決済可能）
    払戻金額 : "      "（ALL半角空白）
    開始日・終了日 : "20250101"、"20250131"
    開始時刻・終了時刻 : "0000"、"2359"
    半券確認要否 : "0"：不要
    チケット手数料払戻金額 : "000000"：最低値
    取消処理結果 : "00"：正常
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    チケット種別選択： : プリペイドサービスチケット
    """
    return '8000000002570'
def RESPONSE_TICKET_DATA_TICKET_REPAY_CASE_01():
    data =  ResponseEcTicketRepayData(
        payback_start_ymd='20250101',
        payback_end_ymd='20250131',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
    )
    return COMPARE_EC_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TICKET_REPAY_CASE_01_CANCEL():
    data =  ResponseEcTicketRepayData(
        payback_start_ymd='20250101',
        payback_end_ymd='20250131',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
    )
    return COMPARE_EC_REPAY_DICT(data)

def BARCODE_TICKET_REPAY_CASE_02():
    """
    正常系　払戻バーコード 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常（決済可能）
    払戻金額 : "000000"：最低値
    開始日・終了日 : "20250201"、"99999999"
    開始時刻・終了時刻 : "0930"、"1259"
    半券確認要否 : "1"：要
    チケット手数料払戻金額 : "003000"：一般値
    取消処理結果 : "00"：正常
    取消応答結果 : "01"：取消異常(検索キーエラー)
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    チケット種別選択： : プリペイドサービスチケット
    """
    return '8000000445537'
def RESPONSE_TICKET_DATA_TICKET_REPAY_CASE_02():
    data =  ResponseEcTicketRepayData(
        payback_kingaku='000000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0930',
        svc_time_end_hm='1259',
        hanken_yohi='1',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TICKET_REPAY_CASE_02_CANCEL():
    data =  ResponseEcTicketRepayData(
        oto_kekka='01',
        payback_kingaku='000000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0930',
        svc_time_end_hm='1259',
        hanken_yohi='1',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TICKET_REPAY_CASE_02_CANCEL_RETRY():
    data =  ResponseEcTicketRepayData(
        payback_kingaku='000000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0930',
        svc_time_end_hm='1259',
        hanken_yohi='1',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)

def BARCODE_TICKET_REPAY_CASE_03():
    """
    正常系　払戻バーコード 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常（決済可能）
    払戻金額 : "001000"：一般値
    開始日・終了日 : "99999999"、"20250131"
    開始時刻・終了時刻 : "1830"、"2200"
    半券確認要否 : "1"：要
    チケット手数料払戻金額 : "      "（ALL半角空白）
    取消処理結果 : "00"：正常
    取消応答結果 : "54"：取消異常(払戻未済み)
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    チケット種別選択： : プリペイドサービスチケット
    """
    return '8000000870575'
def RESPONSE_TICKET_DATA_TICKET_REPAY_CASE_03():
    data =  ResponseEcTicketRepayData(
        payback_kingaku='001000',
        payback_start_ymd='99999999',
        payback_end_ymd='20250131',
        svc_time_start_hm='1830',
        svc_time_end_hm='2200',
        hanken_yohi='1',
        payback_tesuryo='      ',
    )
    return COMPARE_EC_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TICKET_REPAY_CASE_03_CANCEL():
    data =  ResponseEcTicketRepayData(
        oto_kekka='54',
        payback_kingaku='001000',
        payback_start_ymd='99999999',
        payback_end_ymd='20250131',
        svc_time_start_hm='1830',
        svc_time_end_hm='2200',
        hanken_yohi='1',
        payback_tesuryo='      ',
    )
    return COMPARE_EC_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TICKET_REPAY_CASE_03_CANCEL_RETRY():
    data =  ResponseEcTicketRepayData(
        payback_kingaku='001000',
        payback_start_ymd='99999999',
        payback_end_ymd='20250131',
        svc_time_start_hm='1830',
        svc_time_end_hm='2200',
        hanken_yohi='1',
        payback_tesuryo='      ',
    )
    return COMPARE_EC_REPAY_DICT(data)

def BARCODE_TICKET_REPAY_CASE_04():
    """
    正常系　払戻バーコード 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常（決済可能）
    払戻金額 : "999999"：最大値
    開始日・終了日 : "20000101"、"99999999"
    開始時刻・終了時刻 : "0000"、"9999"
    半券確認要否 : "0"：不要
    チケット手数料払戻金額 : "999999"：最大値
    取消処理結果 : "00"：正常
    取消応答結果 : "99"：取消異常(その他エラー)
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    チケット種別選択： : プリペイドサービスチケット
    """
    return '8000001298170'
def RESPONSE_TICKET_DATA_TICKET_REPAY_CASE_04():
    data =  ResponseEcTicketRepayData(
        payback_kingaku='999999',
        payback_start_ymd='20000101',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='9999',
        payback_tesuryo='999999',
    )
    return COMPARE_EC_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TICKET_REPAY_CASE_04_CANCEL():
    data =  ResponseEcTicketRepayData(
        oto_kekka='99',
        payback_kingaku='999999',
        payback_start_ymd='20000101',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='9999',
        payback_tesuryo='999999',
    )
    return COMPARE_EC_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TICKET_REPAY_CASE_04_CANCEL_RETRY():
    data =  ResponseEcTicketRepayData(
        payback_kingaku='999999',
        payback_start_ymd='20000101',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='9999',
        payback_tesuryo='999999',
    )
    return COMPARE_EC_REPAY_DICT(data)

def BARCODE_TICKET_REPAY_CASE_05():
    """
    正常系　払戻バーコード 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "00"：正常（決済可能）
    払戻金額 : "001000"：一般値
    開始日・終了日 : "20250201"、"99999999"
    開始時刻・終了時刻 : "0000"、"2359"
    半券確認要否 : "0"：不要
    チケット手数料払戻金額 : "003000"：一般値
    取消処理結果 : "00"：正常
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    チケット種別選択： : プリペイドサービスチケット
    """
    return '8000000742414'
def RESPONSE_TICKET_DATA_TICKET_REPAY_CASE_05():
    data =  ResponseEcTicketRepayData(
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TICKET_REPAY_CASE_05_CANCEL():
    data =  ResponseEcTicketRepayData(
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)

def BARCODE_TICKET_REPAY_SYORI_KEKKA_14():
    """
    正常系　払戻バーコード 生成時選択肢
    --------
    処理結果 : "14"：サービス時間帯エラー
    応答結果 : "00"：正常（決済可能）
    払戻金額 : "001000"：一般値
    開始日・終了日 : "20250201"、"99999999"
    開始時刻・終了時刻 : "0000"、"2359"
    半券確認要否 : "0"：不要
    チケット手数料払戻金額 : "003000"：一般値
    取消処理結果 : "10"：電文区分エラー
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    チケット種別選択： : プリペイドサービスチケット
    """
    return '8000063657298'
def RESPONSE_TICKET_DATA_TICKET_REPAY_SYORI_KEKKA_14():
    data =  ResponseEcTicketRepayData(
        shori_kekka='14',
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TICKET_REPAY_SYORI_KEKKA_14_CANCEL():
    data =  ResponseEcTicketRepayData(
        shori_kekka='10',
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TICKET_REPAY_SYORI_KEKKA_14_CANCEL_RETRY():
    data =  ResponseEcTicketRepayData(
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)

def BARCODE_TICKET_REPAY_SYORI_KEKKA_99_400():
    """
    正常系　払戻バーコード 生成時選択肢
    --------
    処理結果 : "99"：その他エラー(400)
    応答結果 : "00"：正常（決済可能）
    払戻金額 : "001000"：一般値
    開始日・終了日 : "20250201"、"99999999"
    開始時刻・終了時刻 : "0000"、"2359"
    半券確認要否 : "0"：不要
    チケット手数料払戻金額 : "003000"：一般値
    取消処理結果 : "11"：業務区分エラー
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    チケット種別選択： : プリペイドサービスチケット
    """
    return '8000084629137'
def RESPONSE_TICKET_DATA_TICKET_REPAY_SYORI_KEKKA_99_400():
    data =  ResponseEcTicketRepayData(
        shori_kekka='99',
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TICKET_REPAY_SYORI_KEKKA_99_400_CANCEL():
    data =  ResponseEcTicketRepayData(
        shori_kekka='11',
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TICKET_REPAY_SYORI_KEKKA_99_400_CANCEL_RETRY():
    data =  ResponseEcTicketRepayData(
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)

def BARCODE_TICKET_REPAY_SYORI_KEKKA_99_500():
    """
    正常系　払戻バーコード 生成時選択肢
    --------
    処理結果 : "99"：その他エラー(500)
    応答結果 : "00"：正常（決済可能）
    払戻金額 : "001000"：一般値
    開始日・終了日 : "20250201"、"99999999"
    開始時刻・終了時刻 : "0000"、"2359"
    半券確認要否 : "0"：不要
    チケット手数料払戻金額 : "003000"：一般値
    取消処理結果 : "14"：サービス時間帯エラー
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    チケット種別選択： : プリペイドサービスチケット
    """
    return '8000105600978'
def RESPONSE_TICKET_DATA_TICKET_REPAY_SYORI_KEKKA_99_500():
    data =  ResponseEcTicketRepayData(
        shori_kekka='99',
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TICKET_REPAY_SYORI_KEKKA_99_500_CANCEL():
    data =  ResponseEcTicketRepayData(
        shori_kekka='14',
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TICKET_REPAY_SYORI_KEKKA_99_500_CANCEL_RETRY():
    data =  ResponseEcTicketRepayData(
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)

def BARCODE_TICKET_REPAY_OTO_KEKKA_01():
    """
    正常系　払戻バーコード 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "01"：検索キーエラー
    払戻金額 : "001000"：一般値
    開始日・終了日 : "20250201"、"99999999"
    開始時刻・終了時刻 : "0000"、"2359"
    半券確認要否 : "0"：不要
    チケット手数料払戻金額 : "003000"：一般値
    取消処理結果 : "99"：その他エラー(400)
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    チケット種別選択： : プリペイドサービスチケット
    """
    return '8000002054416'
def RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_01():
    data =  ResponseEcTicketRepayData(
        oto_kekka='01',
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_01_CANCEL():
    data =  ResponseEcTicketRepayData(
        shori_kekka='99',
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_01_CANCEL_RETRY():
    data =  ResponseEcTicketRepayData(
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)

def BARCODE_TICKET_REPAY_OTO_KEKKA_05():
    """
    正常系　払戻バーコード 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "05"：決済中止
    払戻金額 : "001000"：一般値
    開始日・終了日 : "20250201"、"99999999"
    開始時刻・終了時刻 : "0000"、"2359"
    半券確認要否 : "0"：不要
    チケット手数料払戻金額 : "003000"：一般値
    取消処理結果 : "99"：その他エラー(500)
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    チケット種別選択： : プリペイドサービスチケット
    """
    return '8000003365450'
def RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_05():
    data =  ResponseEcTicketRepayData(
        oto_kekka='05',
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_05_CANCEL():
    data =  ResponseEcTicketRepayData(
        shori_kekka='99',
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_05_CANCEL_RETRY():
    data =  ResponseEcTicketRepayData(
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)

def BARCODE_TICKET_REPAY_OTO_KEKKA_11():
    """
    正常系　払戻バーコード 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "11"：店舗指定ｴﾗｰ
    払戻金額 : "001000"：一般値
    開始日・終了日 : "20250201"、"99999999"
    開始時刻・終了時刻 : "0000"、"2359"
    半券確認要否 : "0"：不要
    チケット手数料払戻金額 : "003000"：一般値
    取消処理結果 : "00"：正常
    取消応答結果 : "01"：取消異常(検索キーエラー)
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    チケット種別選択： : プリペイドサービスチケット
    """
    return '8000004674650'
def RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_11():
    data =  ResponseEcTicketRepayData(
        oto_kekka='11',
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_11_CANCEL():
    data =  ResponseEcTicketRepayData(
        oto_kekka='01',
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_11_CANCEL_RETRY():
    data =  ResponseEcTicketRepayData(
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)

def BARCODE_TICKET_REPAY_OTO_KEKKA_51():
    """
    正常系　払戻バーコード 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "51"：払戻済み
    払戻金額 : "001000"：一般値
    開始日・終了日 : "20250201"、"99999999"
    開始時刻・終了時刻 : "0000"、"2359"
    半券確認要否 : "0"：不要
    チケット手数料払戻金額 : "003000"：一般値
    取消処理結果 : "00"：正常
    取消応答結果 : "54"：取消異常(払戻未済み)
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    チケット種別選択： : プリペイドサービスチケット
    """
    return '8000005985458'
def RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_51():
    data =  ResponseEcTicketRepayData(
        oto_kekka='51',
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_51_CANCEL():
    data =  ResponseEcTicketRepayData(
        oto_kekka='54',
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_51_CANCEL_RETRY():
    data =  ResponseEcTicketRepayData(
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)

def BARCODE_TICKET_REPAY_OTO_KEKKA_52():
    """
    正常系　払戻バーコード 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "52"：払戻期間前エラー
    払戻金額 : "001000"：一般値
    開始日・終了日 : "20250201"、"99999999"
    開始時刻・終了時刻 : "0000"、"2359"
    半券確認要否 : "0"：不要
    チケット手数料払戻金額 : "003000"：一般値
    取消処理結果 : "00"：正常
    取消応答結果 : "99"：取消異常(その他エラー)
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    チケット種別選択： : プリペイドサービスチケット
    """
    return '8000007296255'
def RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_52():
    data =  ResponseEcTicketRepayData(
        oto_kekka='52',
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_52_CANCEL():
    data =  ResponseEcTicketRepayData(
        oto_kekka='99',
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_52_CANCEL_RETRY():
    data =  ResponseEcTicketRepayData(
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)

def BARCODE_TICKET_REPAY_OTO_KEKKA_53():
    """
    正常系　払戻バーコード 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "53"：払戻不可エラー
    払戻金額 : "001000"：一般値
    開始日・終了日 : "20250201"、"99999999"
    開始時刻・終了時刻 : "0000"、"2359"
    半券確認要否 : "0"：不要
    チケット手数料払戻金額 : "003000"：一般値
    取消処理結果 : "10"：電文区分エラー
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "1"：再送異常
    チケット種別選択： : プリペイドサービスチケット
    """
    return '8000008607098'
def RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_53():
    data =  ResponseEcTicketRepayData(
        oto_kekka='53',
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_53_CANCEL():
    data =  ResponseEcTicketRepayData(
        shori_kekka='10',
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)

def BARCODE_TICKET_REPAY_OTO_KEKKA_55():
    """
    正常系　払戻バーコード 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "55"：払戻ｻｰﾋﾞｽ時間帯ｴﾗｰ
    払戻金額 : "001000"：一般値
    開始日・終了日 : "20250201"、"99999999"
    開始時刻・終了時刻 : "0000"、"2359"
    半券確認要否 : "0"：不要
    チケット手数料払戻金額 : "003000"：一般値
    取消処理結果 : "00"：正常
    取消応答結果 : "01"：取消異常(検索キーエラー)
    レスポンスパターン（取消再送区分用） : "1"：再送異常
    チケット種別選択： : プリペイドサービスチケット
    """
    return '8000009917578'
def RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_55():
    data =  ResponseEcTicketRepayData(
        oto_kekka='55',
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_55_CANCEL():
    data =  ResponseEcTicketRepayData(
        oto_kekka='01',
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)

def BARCODE_TICKET_REPAY_OTO_KEKKA_99():
    """
    正常系　払戻バーコード 生成時選択肢
    --------
    処理結果 : "00"：正常
    応答結果 : "99"：その他エラー
    払戻金額 : "001000"：一般値
    開始日・終了日 : "20250201"、"99999999"
    開始時刻・終了時刻 : "0000"、"2359"
    半券確認要否 : "0"：不要
    チケット手数料払戻金額 : "003000"：一般値
    取消処理結果 : "00"：正常
    取消応答結果 : "00"：取消正常
    レスポンスパターン（取消再送区分用） : "0"：再送正常
    チケット種別選択： : プリペイドサービスチケット
    """
    return '8000013849612'
def RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_99():
    data =  ResponseEcTicketRepayData(
        oto_kekka='99',
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)
def RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_99_CANCEL():
    data =  ResponseEcTicketRepayData(
        payback_kingaku='001000',
        payback_start_ymd='20250201',
        payback_end_ymd='99999999',
        svc_time_start_hm='0000',
        svc_time_end_hm='2359',
        payback_tesuryo='003000',
    )
    return COMPARE_EC_REPAY_DICT(data)


# ---------------------------
# Mcopyチケット マッピングNo3 EC関連問合せ/完了通知
# ---------------------------
def BARCODE_EC_KANRYO_CASE_01():
    return '6000000000028'
def KESSAI_KEY_EC_KANRYO_CASE_01():
    """
    正常系　決済キー 生成時選択肢
    --------
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : " "（半角空白）：預り金計上
    印紙基準額/収納金額 : "      "（ALL半角空白）
    価格変更フラグ : " "（半角空白）：下記以外の場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00000"：オリンピックチケット以外
    チケット発券個別情報 : 0件
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    支払方法区分 : "1"：クレジット支払
    成功まで失敗回数 : 0
    """
    return BARCODE_EC_KANRYO_CASE_01()[1:12]
def RESPONSE_TICKET_DATA_EC_KANRYO_CASE_01_REQUEST():
    data =  ResponseEcTicketData(
        kingaku_henko_flg=' ',
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_KANRYO_CASE_01_REQUEST_CANCEL():
    data =  ResponseEcTicketData(
        kingaku_henko_flg=' ',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_KANRYO_CASE_01():
    data =  ResponseEcTicketKanryoData()
    return COMPARE_EC_KANRYO_DICT(data)


def BARCODE_EC_KANRYO_CASE_02():
    return '6000141086905'
def KESSAI_KEY_EC_KANRYO_CASE_02():
    """
    正常系　決済キー 生成時選択肢
    --------
    支払種別 : "2"：代金引換
    納品種別 : "2"：宅配
    売上計上区分 : "1"：売上計上
    印紙基準額/収納金額 : "000000"：最低値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "5"：新プリペイドサービス
    SHOPCD : "00236"：オリンピックチケット
    チケット発券個別情報 : 1件
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    支払方法区分 : "2"：クレジット支払以外
    成功まで失敗回数 : 0
    """
    return BARCODE_EC_KANRYO_CASE_02()[1:12]
def RESPONSE_TICKET_DATA_EC_KANRYO_CASE_02_REQUEST():
    data =  ResponseEcTicketData(
        pay_type='2',
        dlv_type='2',
        keijyo_type='1',
        inshi_kijun='000000',
        kino_kbn='5',
        shop_id='00236',
        ticket_count=1,
        shuno_kingaku='000000',
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_KANRYO_CASE_02_REQUEST_CANCEL():
    data =  ResponseEcTicketData(
        pay_type='2',
        dlv_type='2',
        keijyo_type='1',
        inshi_kijun='000000',
        kino_kbn='5',
        shop_id='00236',
        ticket_count=1,
        shuno_kingaku='000000',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_KANRYO_CASE_02():
    data =  ResponseEcTicketKanryoData(
        shop_id='00236',
        shiharai_hoho_kbn='2',
        shuno_kingaku='000000',
    )
    return COMPARE_EC_KANRYO_DICT(data)


def BARCODE_EC_KANRYO_CASE_03():
    return '6000194355546'
def KESSAI_KEY_EC_KANRYO_CASE_03():
    """
    正常系　決済キー 生成時選択肢
    --------
    支払種別 : "3"：後払い
    納品種別 : "1"：店渡し
    売上計上区分 : "2"：売上計上/未収入金計上
    印紙基準額/収納金額 : "001000"：一般値
    価格変更フラグ : " "（半角空白）：下記以外の場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00745"：一般値
    チケット発券個別情報 : 2件
    処理結果 : "00"：正常
    応答結果 : "00"：正常応答
    支払方法区分 : " "スペース：ネット商品返品の場合
    成功まで失敗回数 : 0
    """
    return BARCODE_EC_KANRYO_CASE_03()[1:12]
def RESPONSE_TICKET_DATA_EC_KANRYO_CASE_03_REQUEST():
    data =  ResponseEcTicketData(
        pay_type='3',
        keijyo_type='2',
        inshi_kijun='001000',
        kingaku_henko_flg=' ',
        shop_id='00745',
        ticket_count=2,
        shuno_kingaku='001000',
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_KANRYO_CASE_03_REQUEST_CANCEL():
    data =  ResponseEcTicketData(
        pay_type='3',
        keijyo_type='2',
        inshi_kijun='001000',
        kingaku_henko_flg=' ',
        shop_id='00745',
        ticket_count=2,
        shuno_kingaku='001000',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_KANRYO_CASE_03():
    data =  ResponseEcTicketKanryoData(
        shop_id='00745',
        shiharai_hoho_kbn=' ',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)


def BARCODE_EC_KANRYO_SYORI_KEKKA_10():
    return '6000002521941'
def KESSAI_KEY_EC_KANRYO_SYORI_KEKKA_10():
    """
    正常系　決済キー 生成時選択肢
    --------
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : " "（半角空白）：預り金計上
    印紙基準額/収納金額 : "      "（ALL半角空白）
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "5"：新プリペイドサービス
    SHOPCD : "30731"：ぴあ
    チケット発券個別情報 : 10件
    処理結果 : "10"：電文区分エラー
    応答結果 : "00"：正常応答
    支払方法区分 : " "スペース：ネット商品返品の場合
    成功まで失敗回数 : 0
    """
    return BARCODE_EC_KANRYO_SYORI_KEKKA_10()[1:12]
def RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_10_REQUEST():
    data =  ResponseEcTicketData(
        kino_kbn='5',
        shop_id='30731',
        ticket_count=10,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_10_REQUEST_CANCEL():
    data =  ResponseEcTicketData(
        kino_kbn='5',
        shop_id='30731',
        ticket_count=10,
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_10():
    data =  ResponseEcTicketKanryoData(
        shop_id='30731',
        shori_kekka='10',
        shiharai_hoho_kbn=' ',
    )
    return COMPARE_EC_KANRYO_DICT(data)


def BARCODE_EC_KANRYO_SYORI_KEKKA_11():
    return '6000055137625'
def KESSAI_KEY_EC_KANRYO_SYORI_KEKKA_11():
    """
    正常系　決済キー 生成時選択肢
    --------
    支払種別 : "1"：前払い
    納品種別 : "2"：宅配
    売上計上区分 : "1"：売上計上
    印紙基準額/収納金額 : "000000"：最低値
    価格変更フラグ : " "（半角空白）：下記以外の場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00000"：オリンピックチケット以外
    チケット発券個別情報 : 20件
    処理結果 : "11"：業務区分エラー 
    応答結果 : "00"：正常応答
    支払方法区分 : " "スペース：ネット商品返品の場合
    成功まで失敗回数 : 0
    """
    return BARCODE_EC_KANRYO_SYORI_KEKKA_11()[1:12]
def RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_11_REQUEST():
    data =  ResponseEcTicketData(
        dlv_type='2',
        keijyo_type='1',
        inshi_kijun='000000',
        kingaku_henko_flg=' ',
        ticket_count=20,
        shuno_kingaku='000000',
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_11_REQUEST_CANCEL():
    data =  ResponseEcTicketData(
        dlv_type='2',
        keijyo_type='1',
        inshi_kijun='000000',
        kingaku_henko_flg=' ',
        ticket_count=20,
        shuno_kingaku='000000',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_11():
    data =  ResponseEcTicketKanryoData(
        shori_kekka='11',
        shiharai_hoho_kbn=' ',
        shuno_kingaku='000000',
    )
    return COMPARE_EC_KANRYO_DICT(data)


def BARCODE_EC_KANRYO_SYORI_KEKKA_14():
    return '6000112238425'
def KESSAI_KEY_EC_KANRYO_SYORI_KEKKA_14():
    """
    正常系　決済キー 生成時選択肢
    --------
    支払種別 : "2"：代金引換
    納品種別 : "1"：店渡し
    売上計上区分 : "2"：売上計上/未収入金計上
    印紙基準額/収納金額 : "001000"：一般値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "5"：新プリペイドサービス
    SHOPCD : "00236"：オリンピックチケット
    チケット発券個別情報 : 0件
    処理結果 : "14"：サービス時間帯エラー
    応答結果 : "00"：正常応答
    支払方法区分 : " "スペース：ネット商品返品の場合
    成功まで失敗回数 : 0
    """
    return BARCODE_EC_KANRYO_SYORI_KEKKA_14()[1:12]
def RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_14_REQUEST():
    data =  ResponseEcTicketData(
        pay_type='2',
        keijyo_type='2',
        inshi_kijun='001000',
        kino_kbn='5',
        shop_id='00236',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_14_REQUEST_CANCEL():
    data =  ResponseEcTicketData(
        pay_type='2',
        keijyo_type='2',
        inshi_kijun='001000',
        kino_kbn='5',
        shop_id='00236',
        shuno_kingaku='001000',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_14():
    data =  ResponseEcTicketKanryoData(
        shop_id='00236',
        shori_kekka='14',
        shiharai_hoho_kbn=' ',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)


def BARCODE_EC_KANRYO_SYORI_KEKKA_99_400():
    return '6000168130902'
def KESSAI_KEY_EC_KANRYO_SYORI_KEKKA_99_400():
    """
    正常系　決済キー 生成時選択肢
    --------
    支払種別 : "3"：後払い
    納品種別 : "1"：店渡し
    売上計上区分 : " "（半角空白）：預り金計上
    印紙基準額/収納金額 : "      "（ALL半角空白）
    価格変更フラグ : " "（半角空白）：下記以外の場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00745"：一般値
    チケット発券個別情報 : 1件
    処理結果 : "99"：その他エラー(400)
    応答結果 : "00"：正常応答
    支払方法区分 : " "スペース：ネット商品返品の場合
    成功まで失敗回数 : 0
    """
    return BARCODE_EC_KANRYO_SYORI_KEKKA_99_400()[1:12]
def RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_99_400_REQUEST():
    data =  ResponseEcTicketData(
        pay_type='3',
        kingaku_henko_flg=' ',
        shop_id='00745',
        ticket_count=1,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_99_400_REQUEST_CANCEL():
    data =  ResponseEcTicketData(
        pay_type='3',
        kingaku_henko_flg=' ',
        shop_id='00745',
        ticket_count=1,
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_99_400():
    data =  ResponseEcTicketKanryoData(
        shop_id='00745',
        shori_kekka='99',
        shiharai_hoho_kbn=' ',
    )
    return COMPARE_EC_KANRYO_DICT(data)


def BARCODE_EC_KANRYO_SYORI_KEKKA_99_500():
    return '6000057561947'
def KESSAI_KEY_EC_KANRYO_SYORI_KEKKA_99_500():
    """
    正常系　決済キー 生成時選択肢
    --------
    支払種別 : "1"：前払い
    納品種別 : "2"：宅配
    売上計上区分 : "1"：売上計上
    印紙基準額/収納金額 : "000000"：最低値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "5"：新プリペイドサービス
    SHOPCD : "30731"：ぴあ
    チケット発券個別情報 : 2件
    処理結果 : "99"：その他エラー(500)
    応答結果 : "00"：正常応答
    支払方法区分 : " "スペース：ネット商品返品の場合
    成功まで失敗回数 : 0
    """
    return BARCODE_EC_KANRYO_SYORI_KEKKA_99_500()[1:12]
def RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_99_500_REQUEST():
    data =  ResponseEcTicketData(
        dlv_type='2',
        keijyo_type='1',
        inshi_kijun='000000',
        kino_kbn='5',
        shop_id='30731',
        ticket_count=2,
        shuno_kingaku='000000',
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_99_500_REQUEST_CANCEL():
    data =  ResponseEcTicketData(
        dlv_type='2',
        keijyo_type='1',
        inshi_kijun='000000',
        kino_kbn='5',
        shop_id='30731',
        ticket_count=2,
        shuno_kingaku='000000',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_99_500():
    data =  ResponseEcTicketKanryoData(
        shop_id='30731',
        shori_kekka='99',
        shiharai_hoho_kbn=' ',
        shuno_kingaku='000000',
    )
    return COMPARE_EC_KANRYO_DICT(data)


def BARCODE_EC_KANRYO_SYORI_KEKKA_TIMEOUT():
    return '6000026291547'
def KESSAI_KEY_EC_KANRYO_SYORI_KEKKA_TIMEOUT():
    """
    正常系　決済キー 生成時選択肢
    --------
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : "2"：売上計上/未収入金計上
    印紙基準額/収納金額 : "001000"：一般値
    価格変更フラグ : " "（半角空白）：下記以外の場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00000"：オリンピックチケット以外
    チケット発券個別情報 : 10件
    処理結果 : "00"：タイムアウト(正常)
    応答結果 : "00"：正常応答
    支払方法区分 : " "スペース：ネット商品返品の場合
    成功まで失敗回数 : 0
    """
    return BARCODE_EC_KANRYO_SYORI_KEKKA_TIMEOUT()[1:12]
def RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_TIMEOUT_REQUEST():
    data =  ResponseEcTicketData(
        keijyo_type='2',
        inshi_kijun='001000',
        kingaku_henko_flg=' ',
        ticket_count=10,
        shuno_kingaku='001000',
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_TIMEOUT_REQUEST_CANCEL():
    data =  ResponseEcTicketData(
        keijyo_type='2',
        inshi_kijun='001000',
        kingaku_henko_flg=' ',
        ticket_count=10,
        shuno_kingaku='001000',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_TIMEOUT():
    data =  ResponseEcTicketKanryoData(
        shiharai_hoho_kbn=' ',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)


def BARCODE_EC_KANRYO_SYORI_KEKKA_TIMEOUT_99():
    return '6000086116187'
def KESSAI_KEY_EC_KANRYO_SYORI_KEKKA_TIMEOUT_99():
    """
    正常系　決済キー 生成時選択肢
    --------
    支払種別 : "2"：代金引換
    納品種別 : "1"：店渡し
    売上計上区分 : " "（半角空白）：預り金計上
    印紙基準額/収納金額 : "      "（ALL半角空白）
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "5"：新プリペイドサービス
    SHOPCD : "00236"：オリンピックチケット
    チケット発券個別情報 : 20件
    処理結果 : "99"：タイムアウト(その他エラー500)
    応答結果 : "00"：正常応答
    支払方法区分 : " "スペース：ネット商品返品の場合
    成功まで失敗回数 : 0
    """
    return BARCODE_EC_KANRYO_SYORI_KEKKA_TIMEOUT_99()[1:12]
def RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_TIMEOUT_99_REQUEST():
    data =  ResponseEcTicketData(
        pay_type='2',
        kino_kbn='5',
        shop_id='00236',
        ticket_count=20,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_TIMEOUT_99_REQUEST_CANCEL():
    data =  ResponseEcTicketData(
        pay_type='2',
        kino_kbn='5',
        shop_id='00236',
        ticket_count=20,
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_TIMEOUT_99():
    data =  ResponseEcTicketKanryoData(
        shop_id='00236',
        shori_kekka='99',
        shiharai_hoho_kbn=' ',
    )
    return COMPARE_EC_KANRYO_DICT(data)


def BARCODE_EC_KANRYO_OTO_KEKKA_01():
    return '6000181228501'
def KESSAI_KEY_EC_KANRYO_OTO_KEKKA_01():
    """
    正常系　決済キー 生成時選択肢
    --------
    支払種別 : "3"：後払い
    納品種別 : "1"：店渡し
    売上計上区分 : "1"：売上計上
    印紙基準額/収納金額 : "000000"：最低値
    価格変更フラグ : " "（半角空白）：下記以外の場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00745"：一般値
    チケット発券個別情報 : 1件
    処理結果 : "00"：正常
    応答結果 : "01"：検索キーエラー
    支払方法区分 : " "スペース：ネット商品返品の場合
    成功まで失敗回数 : 0
    """
    return BARCODE_EC_KANRYO_OTO_KEKKA_01()[1:12]
def RESPONSE_TICKET_DATA_EC_KANRYO_OTO_KEKKA_01_REQUEST():
    data =  ResponseEcTicketData(
        pay_type='3',
        keijyo_type='1',
        inshi_kijun='000000',
        kingaku_henko_flg=' ',
        shop_id='00745',
        ticket_count=1,
        shuno_kingaku='000000',
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_KANRYO_OTO_KEKKA_01_REQUEST_CANCEL():
    data =  ResponseEcTicketData(
        pay_type='3',
        keijyo_type='1',
        inshi_kijun='000000',
        kingaku_henko_flg=' ',
        shop_id='00745',
        ticket_count=1,
        shuno_kingaku='000000',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_KANRYO_OTO_KEKKA_01():
    data =  ResponseEcTicketKanryoData(
        shop_id='00745',
        oto_kekka='01',
        shiharai_hoho_kbn=' ',
        shuno_kingaku='000000',
    )
    return COMPARE_EC_KANRYO_DICT(data)


def BARCODE_EC_KANRYO_OTO_KEKKA_99():
    return '6000028694100'
def KESSAI_KEY_EC_KANRYO_OTO_KEKKA_99():
    """
    正常系　決済キー 生成時選択肢
    --------
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : "2"：売上計上/未収入金計上
    印紙基準額/収納金額 : "001000"：一般値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "5"：新プリペイドサービス
    SHOPCD : "30731"：ぴあ
    チケット発券個別情報 : 1件
    処理結果 : "00"：正常
    応答結果 : "99"：その他エラー
    支払方法区分 : " "スペース：ネット商品返品の場合
    成功まで失敗回数 : 0
    """
    return BARCODE_EC_KANRYO_OTO_KEKKA_99()[1:12]
def RESPONSE_TICKET_DATA_EC_KANRYO_OTO_KEKKA_99_REQUEST():
    data =  ResponseEcTicketData(
        keijyo_type='2',
        inshi_kijun='001000',
        kino_kbn='5',
        shop_id='30731',
        ticket_count=1,
        shuno_kingaku='001000',
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_KANRYO_OTO_KEKKA_99_REQUEST_CANCEL():
    data =  ResponseEcTicketData(
        keijyo_type='2',
        inshi_kijun='001000',
        kino_kbn='5',
        shop_id='30731',
        ticket_count=1,
        shuno_kingaku='001000',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_KANRYO_OTO_KEKKA_99():
    data =  ResponseEcTicketKanryoData(
        shop_id='30731',
        oto_kekka='99',
        shiharai_hoho_kbn=' ',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)


# ---------------------------
# Mcopyチケット マッピングNo4 EC関連問合せ/完了通知
# ---------------------------
def BARCODE_EC_TICKET_DETAIL_CASE_01():
    return '6000000000035'
def KESSAI_KEY_EC_TICKET_DETAIL_CASE_01():
    """
    正常系　決済キー 生成時選択肢
    --------
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : " "（半角空白）：預り金計上
    印紙基準額 : "      "（ALL半角空白）
    価格変更フラグ : " "（半角空白）：下記以外の場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00000"：オリンピックチケット以外
    収納金額 : "      "（ALL半角空白）
    チケット発券個別情報(枚数) : 0
    券面情報データ : A
    """
    return BARCODE_EC_TICKET_DETAIL_CASE_01()[1:12]
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_01():
    data =  ResponseEcTicketData(
        kingaku_henko_flg=' ',
        ticket_count=0,
        tc_info_data='A',
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_01_CANCEL():
    data =  ResponseEcTicketData(
        kingaku_henko_flg=' ',
        ticket_count=0,
        tc_info_data='A',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_01_KANRYO():
    data =  ResponseEcTicketKanryoData()
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_EC_TICKET_DETAIL_CASE_02():
    return '6000140298958'
def KESSAI_KEY_EC_TICKET_DETAIL_CASE_02():
    """
    正常系　決済キー 生成時選択肢
    --------
    支払種別 : "2"：代金引換
    納品種別 : "2"：宅配
    売上計上区分 : "1"：売上計上
    印紙基準額 : "000000"：最低値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00236"：オリンピックチケット
    収納金額 : "000000"：最低値
    チケット発券個別情報(枚数) : 1
    券面情報データ : B
    """
    return BARCODE_EC_TICKET_DETAIL_CASE_02()[1:12]
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_02():
    data =  ResponseEcTicketData(
        pay_type='2',
        dlv_type='2',
        keijyo_type='1',
        inshi_kijun='000000',
        shop_id='00236',
        shuno_kingaku='000000',
        ticket_count=1,
        tc_info_data='B',
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_02_CANCEL():
    data =  ResponseEcTicketData(
        pay_type='2',
        dlv_type='2',
        keijyo_type='1',
        inshi_kijun='000000',
        shop_id='00236',
        shuno_kingaku='000000',
        ticket_count=1,
        tc_info_data='B',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_02_KANRYO():
    data =  ResponseEcTicketKanryoData(
        shop_id='00236',
        shuno_kingaku='000000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_EC_TICKET_DETAIL_CASE_03():
    return '6000194745712'
def KESSAI_KEY_EC_TICKET_DETAIL_CASE_03():
    """
    正常系　決済キー 生成時選択肢
    --------
    支払種別 : "3"：後払い
    納品種別 : "1"：店渡し
    売上計上区分 : "2"：売上計上/未収入金計上
    印紙基準額 : "001000"：一般値
    価格変更フラグ : " "（半角空白）：下記以外の場合
    機能区分 : "5"：新プリペイドサービス
    SHOPCD : "00245"：一般値
    収納金額 : "001000"：一般値
    チケット発券個別情報(枚数) : 2
    券面情報データ : C
    """
    return BARCODE_EC_TICKET_DETAIL_CASE_03()[1:12]
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_03():
    data =  ResponseEcTicketData(
        pay_type='3',
        keijyo_type='2',
        inshi_kijun='001000',
        kingaku_henko_flg=' ',
        kino_kbn='5',
        shop_id='00245',
        shuno_kingaku='001000',
        ticket_count=2,
        tc_info_data='C',
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_03_CANCEL():
    data =  ResponseEcTicketData(
        pay_type='3',
        keijyo_type='2',
        inshi_kijun='001000',
        kingaku_henko_flg=' ',
        kino_kbn='5',
        shop_id='00245',
        shuno_kingaku='001000',
        ticket_count=2,
        tc_info_data='C',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_03_KANRYO():
    data =  ResponseEcTicketKanryoData(
        kino_kbn='5',
        shop_id='00245',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_EC_TICKET_DETAIL_CASE_04():
    return '6000051929118'
def KESSAI_KEY_EC_TICKET_DETAIL_CASE_04():
    """
    正常系　決済キー 生成時選択肢
    --------
    支払種別 : "1"：前払い
    納品種別 : "2"：宅配
    売上計上区分 : " "（半角空白）：預り金計上
    印紙基準額 : "999999"：最大値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "5"：新プリペイドサービス
    SHOPCD : "00745"：一般値
    収納金額 : "999999"：最大値
    チケット発券個別情報(枚数) : 3
    券面情報データ : D
    """
    return BARCODE_EC_TICKET_DETAIL_CASE_04()[1:12]
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_04():
    data =  ResponseEcTicketData(
        dlv_type='2',
        inshi_kijun='999999',
        kino_kbn='5',
        shop_id='00745',
        shuno_kingaku='999999',
        ticket_count=3,
        tc_info_data='D',
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_04_CANCEL():
    data =  ResponseEcTicketData(
        dlv_type='2',
        inshi_kijun='999999',
        kino_kbn='5',
        shop_id='00745',
        shuno_kingaku='999999',
        ticket_count=3,
        tc_info_data='D',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_04_KANRYO():
    data =  ResponseEcTicketKanryoData(
        kino_kbn='5',
        shop_id='00745',
        shuno_kingaku='999999',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_EC_TICKET_DETAIL_CASE_05():
    return '6000094538438'
def KESSAI_KEY_EC_TICKET_DETAIL_CASE_05():
    """
    正常系　決済キー 生成時選択肢
    --------
    支払種別 : "2"：代金引換
    納品種別 : "1"：店渡し
    売上計上区分 : "1"：売上計上
    印紙基準額 : "      "（ALL半角空白）
    価格変更フラグ : " "（半角空白）：下記以外の場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00781"：ティーガイア（PIN）
    収納金額 : "      "（ALL半角空白）
    チケット発券個別情報(枚数) : 4
    券面情報データ : E
    """
    return BARCODE_EC_TICKET_DETAIL_CASE_05()[1:12]
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_05():
    data =  ResponseEcTicketData(
        pay_type='2',
        keijyo_type='1',
        kingaku_henko_flg=' ',
        shop_id='00781',
        ticket_count=4,
        tc_info_data='E',
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_05_CANCEL():
    data =  ResponseEcTicketData(
        pay_type='2',
        keijyo_type='1',
        kingaku_henko_flg=' ',
        shop_id='00781',
        ticket_count=4,
        tc_info_data='E',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_05_KANRYO():
    data =  ResponseEcTicketKanryoData(
        shop_id='00781',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_EC_TICKET_DETAIL_CASE_06():
    return '6000234837353'
def KESSAI_KEY_EC_TICKET_DETAIL_CASE_06():
    """
    正常系　決済キー 生成時選択肢
    --------
    支払種別 : "3"：後払い
    納品種別 : "2"：宅配
    売上計上区分 : "2"：売上計上/未収入金計上
    印紙基準額 : "000000"：最低値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "3"：チケット発券
    SHOPCD : "30731"：ぴあ
    収納金額 : "000000"：最低値
    チケット発券個別情報(枚数) : 5
    券面情報データ : F
    """
    return BARCODE_EC_TICKET_DETAIL_CASE_06()[1:12]
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_06():
    data =  ResponseEcTicketData(
        pay_type='3',
        dlv_type='2',
        keijyo_type='2',
        inshi_kijun='000000',
        shop_id='30731',
        shuno_kingaku='000000',
        ticket_count=5,
        tc_info_data='F',
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_06_CANCEL():
    data =  ResponseEcTicketData(
        pay_type='3',
        dlv_type='2',
        keijyo_type='2',
        inshi_kijun='000000',
        shop_id='30731',
        shuno_kingaku='000000',
        ticket_count=5,
        tc_info_data='F',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_06_KANRYO():
    data =  ResponseEcTicketKanryoData(
        shop_id='30731',
        shuno_kingaku='000000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_EC_TICKET_DETAIL_CASE_07():
    return '6000027140110'
def KESSAI_KEY_EC_TICKET_DETAIL_CASE_07():
    """
    正常系　決済キー 生成時選択肢
    --------
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : "2"：売上計上/未収入金計上
    印紙基準額 : "001000"：一般値
    価格変更フラグ : " "（半角空白）：下記以外の場合
    機能区分 : "5"：新プリペイドサービス
    SHOPCD : "30771"：ディスコ
    収納金額 : "001000"：一般値
    チケット発券個別情報(枚数) : 6
    券面情報データ : G
    """
    return BARCODE_EC_TICKET_DETAIL_CASE_07()[1:12]
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_07():
    data =  ResponseEcTicketData(
        keijyo_type='2',
        inshi_kijun='001000',
        kingaku_henko_flg=' ',
        kino_kbn='5',
        shop_id='30771',
        shuno_kingaku='001000',
        ticket_count=6,
        tc_info_data='G',
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_07_CANCEL():
    data =  ResponseEcTicketData(
        keijyo_type='2',
        inshi_kijun='001000',
        kingaku_henko_flg=' ',
        kino_kbn='5',
        shop_id='30771',
        shuno_kingaku='001000',
        ticket_count=6,
        tc_info_data='G',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_07_KANRYO():
    data =  ResponseEcTicketKanryoData(
        kino_kbn='5',
        shop_id='30771',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_EC_TICKET_DETAIL_CASE_08():
    return '6000073066914'
def KESSAI_KEY_EC_TICKET_DETAIL_CASE_08():
    """
    正常系　決済キー 生成時選択肢
    --------
    支払種別 : "1"：前払い
    納品種別 : "2"：宅配
    売上計上区分 : "2"：売上計上/未収入金計上
    印紙基準額 : "999999"：最大値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "5"：新プリペイドサービス
    SHOPCD : "30773"：JTB（レジャー）
    収納金額 : "999999"：最大値
    チケット発券個別情報(枚数) : 7
    券面情報データ : A
    """
    return BARCODE_EC_TICKET_DETAIL_CASE_08()[1:12]
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_08():
    data =  ResponseEcTicketData(
        dlv_type='2',
        keijyo_type='2',
        inshi_kijun='999999',
        kino_kbn='5',
        shop_id='30773',
        shuno_kingaku='999999',
        ticket_count=7,
        tc_info_data='A',
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_08_CANCEL():
    data =  ResponseEcTicketData(
        dlv_type='2',
        keijyo_type='2',
        inshi_kijun='999999',
        kino_kbn='5',
        shop_id='30773',
        shuno_kingaku='999999',
        ticket_count=7,
        tc_info_data='A',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_08_KANRYO():
    data =  ResponseEcTicketKanryoData(
        kino_kbn='5',
        shop_id='30773',
        shuno_kingaku='999999',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_EC_TICKET_DETAIL_CASE_09():
    return '6000021304396'
def KESSAI_KEY_EC_TICKET_DETAIL_CASE_09():
    """
    正常系　決済キー 生成時選択肢
    --------
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : "2"：売上計上/未収入金計上
    印紙基準額 : "      "（ALL半角空白）
    価格変更フラグ : " "（半角空白）：下記以外の場合
    機能区分 : "3"：チケット発券
    SHOPCD : "30775"：JTB（ＴＤＲ）
    収納金額 : "      "（ALL半角空白）
    チケット発券個別情報(枚数) : 8
    券面情報データ : B
    """
    return BARCODE_EC_TICKET_DETAIL_CASE_09()[1:12]
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_09():
    data =  ResponseEcTicketData(
        keijyo_type='2',
        kingaku_henko_flg=' ',
        shop_id='30775',
        ticket_count=8,
        tc_info_data='B',
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_09_CANCEL():
    data =  ResponseEcTicketData(
        keijyo_type='2',
        kingaku_henko_flg=' ',
        shop_id='30775',
        ticket_count=8,
        tc_info_data='B',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_09_KANRYO():
    data =  ResponseEcTicketKanryoData(
        shop_id='30775',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_EC_TICKET_DETAIL_CASE_10():
    return '6000067067637'
def KESSAI_KEY_EC_TICKET_DETAIL_CASE_10():
    """
    正常系　決済キー 生成時選択肢
    --------
    支払種別 : "1"：前払い
    納品種別 : "2"：宅配
    売上計上区分 : "2"：売上計上/未収入金計上
    印紙基準額 : "000000"：最低値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "3"：チケット発券
    SHOPCD : "30731"：ぴあ
    収納金額 : "000000"：最低値
    チケット発券個別情報(枚数) : 9
    券面情報データ : C
    """
    return BARCODE_EC_TICKET_DETAIL_CASE_10()[1:12]
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_10():
    data =  ResponseEcTicketData(
        dlv_type='2',
        keijyo_type='2',
        inshi_kijun='000000',
        shop_id='30731',
        shuno_kingaku='000000',
        ticket_count=9,
        tc_info_data='C',
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_10_CANCEL():
    data =  ResponseEcTicketData(
        dlv_type='2',
        keijyo_type='2',
        inshi_kijun='000000',
        shop_id='30731',
        shuno_kingaku='000000',
        ticket_count=9,
        tc_info_data='C',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_10_KANRYO():
    data =  ResponseEcTicketKanryoData(
        shop_id='30731',
        shuno_kingaku='000000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_EC_TICKET_DETAIL_CASE_11():
    return '6000026896797'
def KESSAI_KEY_EC_TICKET_DETAIL_CASE_11():
    """
    正常系　決済キー 生成時選択肢
    --------
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : "2"：売上計上/未収入金計上
    印紙基準額 : "001000"：一般値
    価格変更フラグ : " "（半角空白）：下記以外の場合
    機能区分 : "5"：新プリペイドサービス
    SHOPCD : "00000"：オリンピックチケット以外
    収納金額 : "001000"：一般値
    チケット発券個別情報(枚数) : 10
    券面情報データ : D
    """
    return BARCODE_EC_TICKET_DETAIL_CASE_11()[1:12]
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_11():
    data =  ResponseEcTicketData(
        keijyo_type='2',
        inshi_kijun='001000',
        kingaku_henko_flg=' ',
        kino_kbn='5',
        shuno_kingaku='001000',
        ticket_count=10,
        tc_info_data='D',
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_11_CANCEL():
    data =  ResponseEcTicketData(
        keijyo_type='2',
        inshi_kijun='001000',
        kingaku_henko_flg=' ',
        kino_kbn='5',
        shuno_kingaku='001000',
        ticket_count=10,
        tc_info_data='D',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_11_KANRYO():
    data =  ResponseEcTicketKanryoData(
        kino_kbn='5',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_EC_TICKET_DETAIL_CASE_12():
    return '6000072823877'
def KESSAI_KEY_EC_TICKET_DETAIL_CASE_12():
    """
    正常系　決済キー 生成時選択肢
    --------
    支払種別 : "1"：前払い
    納品種別 : "2"：宅配
    売上計上区分 : "2"：売上計上/未収入金計上
    印紙基準額 : "999999"：最大値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "5"：新プリペイドサービス
    SHOPCD : "00236"：オリンピックチケット
    収納金額 : "999999"：最大値
    チケット発券個別情報(枚数) : 12
    券面情報データ : E
    """
    return BARCODE_EC_TICKET_DETAIL_CASE_12()[1:12]
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_12():
    data =  ResponseEcTicketData(
        dlv_type='2',
        keijyo_type='2',
        inshi_kijun='999999',
        kino_kbn='5',
        shop_id='00236',
        shuno_kingaku='999999',
        ticket_count=12,
        tc_info_data='E',
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_12_CANCEL():
    data =  ResponseEcTicketData(
        dlv_type='2',
        keijyo_type='2',
        inshi_kijun='999999',
        kino_kbn='5',
        shop_id='00236',
        shuno_kingaku='999999',
        ticket_count=12,
        tc_info_data='E',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_12_KANRYO():
    data =  ResponseEcTicketKanryoData(
        kino_kbn='5',
        shop_id='00236',
        shuno_kingaku='999999',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_EC_TICKET_DETAIL_CASE_13():
    return '6000027635432'
def KESSAI_KEY_EC_TICKET_DETAIL_CASE_13():
    """
    正常系　決済キー 生成時選択肢
    --------
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : "2"：売上計上/未収入金計上
    印紙基準額 : "001000"：一般値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00245"：一般値
    収納金額 : "001000"：一般値
    チケット発券個別情報(枚数) : 14
    券面情報データ : F
    """
    return BARCODE_EC_TICKET_DETAIL_CASE_13()[1:12]
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_13():
    data =  ResponseEcTicketData(
        keijyo_type='2',
        inshi_kijun='001000',
        shop_id='00245',
        shuno_kingaku='001000',
        ticket_count=14,
        tc_info_data='F',
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_13_CANCEL():
    data =  ResponseEcTicketData(
        keijyo_type='2',
        inshi_kijun='001000',
        shop_id='00245',
        shuno_kingaku='001000',
        ticket_count=14,
        tc_info_data='F',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_13_KANRYO():
    data =  ResponseEcTicketKanryoData(
        shop_id='00245',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_EC_TICKET_DETAIL_CASE_14():
    return '6000027677074'
def KESSAI_KEY_EC_TICKET_DETAIL_CASE_14():
    """
    正常系　決済キー 生成時選択肢
    --------
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : "2"：売上計上/未収入金計上
    印紙基準額 : "001000"：一般値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00745"：一般値
    収納金額 : "001000"：一般値
    チケット発券個別情報(枚数) : 16
    券面情報データ : G
    """
    return BARCODE_EC_TICKET_DETAIL_CASE_14()[1:12]
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_14():
    data =  ResponseEcTicketData(
        keijyo_type='2',
        inshi_kijun='001000',
        shop_id='00745',
        shuno_kingaku='001000',
        ticket_count=16,
        tc_info_data='G',
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_14_CANCEL():
    data =  ResponseEcTicketData(
        keijyo_type='2',
        inshi_kijun='001000',
        shop_id='00745',
        shuno_kingaku='001000',
        ticket_count=16,
        tc_info_data='G',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_14_KANRYO():
    data =  ResponseEcTicketKanryoData(
        shop_id='00745',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)

def BARCODE_EC_TICKET_DETAIL_CASE_15():
    return '6000027677753'
def KESSAI_KEY_EC_TICKET_DETAIL_CASE_15():
    """
    正常系　決済キー 生成時選択肢
    --------
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : "2"：売上計上/未収入金計上
    印紙基準額 : "001000"：一般値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00745"：一般値
    収納金額 : "001000"：一般値
    チケット発券個別情報(枚数) : 18
    券面情報データ : H
    """
    return BARCODE_EC_TICKET_DETAIL_CASE_15()[1:12]
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_15():
    data =  ResponseEcTicketData(
        keijyo_type='2',
        inshi_kijun='001000',
        shop_id='00745',
        shuno_kingaku='001000',
        ticket_count=18,
        tc_info_data='H',
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_15_CANCEL():
    data =  ResponseEcTicketData(
        keijyo_type='2',
        inshi_kijun='001000',
        shop_id='00745',
        shuno_kingaku='001000',
        ticket_count=18,
        tc_info_data='H',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_15_KANRYO():
    data =  ResponseEcTicketKanryoData(
        shop_id='00745',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)
def BARCODE_EC_TICKET_DETAIL_CASE_16():
    return '6000027678439'
def KESSAI_KEY_EC_TICKET_DETAIL_CASE_16():
    """
    正常系　決済キー 生成時選択肢
    --------
    支払種別 : "1"：前払い
    納品種別 : "1"：店渡し
    売上計上区分 : "2"：売上計上/未収入金計上
    印紙基準額 : "001000"：一般値
    価格変更フラグ : "1"：合計金額の変更がある場合
    機能区分 : "3"：チケット発券
    SHOPCD : "00745"：一般値
    収納金額 : "001000"：一般値
    チケット発券個別情報(枚数) : 20
    券面情報データ : I
    """
    return BARCODE_EC_TICKET_DETAIL_CASE_16()[1:12]
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_16():
    data =  ResponseEcTicketData(
        keijyo_type='2',
        inshi_kijun='001000',
        shop_id='00745',
        shuno_kingaku='001000',
        ticket_count=20,
        tc_info_data='I',
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_16_CANCEL():
    data =  ResponseEcTicketData(
        keijyo_type='2',
        inshi_kijun='001000',
        shop_id='00745',
        shuno_kingaku='001000',
        ticket_count=20,
        tc_info_data='I',
        is_cancel=True,
    )
    return COMPARE_EC_DICT(data)
def RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_16_KANRYO():
    data =  ResponseEcTicketKanryoData(
        shop_id='00745',
        shuno_kingaku='001000',
    )
    return COMPARE_EC_KANRYO_DICT(data)
