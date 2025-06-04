from test_barcode_functions import *
from test_compare_response_toto_ticket import *

# ---------------------------
# スポーツ振興くじ マッピングNo1 テストデータ
# ---------------------------
def get_reqres_toto_ticket():
    return [
        {
            'case_name': 'TOTO_BUY_CASE_01',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_CASE_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_CASE_01(),
            },
        },
        {
            'case_name': 'TOTO_BUY_CASE_01_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_CASE_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_CASE_01_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_BUY_CASE_02',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_CASE_02(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_CASE_02(),
            },
        },
        {
            'case_name': 'TOTO_BUY_CASE_02_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_CASE_02(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_CASE_02_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_BUY_CASE_02_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_CASE_02(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_CASE_02_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_BUY_CASE_03',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_CASE_03(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_CASE_03(),
            },
        },
        {
            'case_name': 'TOTO_BUY_CASE_03_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_CASE_03(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_CASE_03_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_BUY_CASE_04',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_CASE_04(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_CASE_04(),
            },
        },
        {
            'case_name': 'TOTO_BUY_CASE_04_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_CASE_04(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_CASE_04_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_BUY_CASE_04_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_CASE_04(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_CASE_04_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_BUY_CASE_05',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_CASE_05(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_CASE_05(),
            },
        },
        {
            'case_name': 'TOTO_BUY_CASE_05_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_CASE_05(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_CASE_05_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_BUY_CASE_06',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_CASE_06(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_CASE_06(),
            },
        },
        {
            'case_name': 'TOTO_BUY_CASE_06_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_CASE_06(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_CASE_06_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_BUY_CASE_06_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_CASE_06(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_CASE_06_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_BUY_CASE_07',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_CASE_07(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_CASE_07(),
            },
        },
        {
            'case_name': 'TOTO_BUY_CASE_07_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_CASE_07(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_CASE_07_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_BUY_CASE_08',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_CASE_08(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_CASE_08(),
            },
        },
        {
            'case_name': 'TOTO_BUY_CASE_08_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_CASE_08(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_CASE_08_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_BUY_SYORI_KEKKA_14',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_SYORI_KEKKA_14(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_14(),
            },
        },
        {
            'case_name': 'TOTO_BUY_SYORI_KEKKA_14_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_SYORI_KEKKA_14(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_14_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_BUY_SYORI_KEKKA_14_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_SYORI_KEKKA_14(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_14_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_BUY_SYORI_KEKKA_14_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_SYORI_KEKKA_14(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_14_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_BUY_SYORI_KEKKA_16',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_SYORI_KEKKA_16(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_16(),
            },
        },
        {
            'case_name': 'TOTO_BUY_SYORI_KEKKA_16_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_SYORI_KEKKA_16(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_16_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_BUY_SYORI_KEKKA_16_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_SYORI_KEKKA_16(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_16_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_BUY_SYORI_KEKKA_99_400',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_SYORI_KEKKA_99_400(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_99_400(),
            },
        },
        {
            'case_name': 'TOTO_BUY_SYORI_KEKKA_99_400_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_SYORI_KEKKA_99_400(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_99_400_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_BUY_SYORI_KEKKA_99_400_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_SYORI_KEKKA_99_400(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_99_400_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_BUY_SYORI_KEKKA_99_400_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_SYORI_KEKKA_99_400(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_99_400_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_BUY_SYORI_KEKKA_99_500',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_SYORI_KEKKA_99_500(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_99_500(),
            },
        },
        {
            'case_name': 'TOTO_BUY_SYORI_KEKKA_99_500_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_SYORI_KEKKA_99_500(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_99_500_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_BUY_SYORI_KEKKA_99_500_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_SYORI_KEKKA_99_500(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_99_500_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_BUY_SYORI_KEKKA_99_500_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_SYORI_KEKKA_99_500(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_99_500_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_BUY_SYORI_KEKKA_TIMEOUT',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_SYORI_KEKKA_TIMEOUT(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_TIMEOUT(),
            },
        },
        {
            'case_name': 'TOTO_BUY_SYORI_KEKKA_TIMEOUT_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_SYORI_KEKKA_TIMEOUT(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_TIMEOUT_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_BUY_SYORI_KEKKA_TIMEOUT_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_SYORI_KEKKA_TIMEOUT(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_TIMEOUT_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_BUY_SYORI_KEKKA_TIMEOUT_99',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_SYORI_KEKKA_TIMEOUT_99(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_TIMEOUT_99(),
            },
        },
        {
            'case_name': 'TOTO_BUY_SYORI_KEKKA_TIMEOUT_99_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_SYORI_KEKKA_TIMEOUT_99(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_TIMEOUT_99_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_BUY_SYORI_KEKKA_TIMEOUT_99_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_SYORI_KEKKA_TIMEOUT_99(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_SYORI_KEKKA_TIMEOUT_99_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_BUY_OUTOU_KEKKA_01',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_OUTOU_KEKKA_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_01(),
            },
        },
        {
            'case_name': 'TOTO_BUY_OUTOU_KEKKA_01_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_OUTOU_KEKKA_01(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_01_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_BUY_OUTOU_KEKKA_01_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_OUTOU_KEKKA_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_01_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_BUY_OUTOU_KEKKA_02',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_OUTOU_KEKKA_02(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_02(),
            },
        },
        {
            'case_name': 'TOTO_BUY_OUTOU_KEKKA_02_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_OUTOU_KEKKA_02(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_02_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_BUY_OUTOU_KEKKA_02_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_OUTOU_KEKKA_02(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_02_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_BUY_OUTOU_KEKKA_02_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_OUTOU_KEKKA_02(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_02_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_BUY_OUTOU_KEKKA_03',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_OUTOU_KEKKA_03(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_03(),
            },
        },
        {
            'case_name': 'TOTO_BUY_OUTOU_KEKKA_03_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_OUTOU_KEKKA_03(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_03_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_BUY_OUTOU_KEKKA_03_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_OUTOU_KEKKA_03(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_03_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_BUY_OUTOU_KEKKA_03_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_OUTOU_KEKKA_03(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_03_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_BUY_OUTOU_KEKKA_05',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_OUTOU_KEKKA_05(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_05(),
            },
        },
        {
            'case_name': 'TOTO_BUY_OUTOU_KEKKA_05_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_OUTOU_KEKKA_05(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_05_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_BUY_OUTOU_KEKKA_06',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_OUTOU_KEKKA_06(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_06(),
            },
        },
        {
            'case_name': 'TOTO_BUY_OUTOU_KEKKA_06_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_OUTOU_KEKKA_06(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_06_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_BUY_OUTOU_KEKKA_06_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_OUTOU_KEKKA_06(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_06_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_BUY_OUTOU_KEKKA_07',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_OUTOU_KEKKA_07(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_07(),
            },
        },
        {
            'case_name': 'TOTO_BUY_OUTOU_KEKKA_07_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_OUTOU_KEKKA_07(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_07_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_BUY_OUTOU_KEKKA_07_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_OUTOU_KEKKA_07(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_07_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_BUY_OUTOU_KEKKA_08',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_OUTOU_KEKKA_08(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_08(),
            },
        },
        {
            'case_name': 'TOTO_BUY_OUTOU_KEKKA_08_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_OUTOU_KEKKA_08(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_08_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_BUY_OUTOU_KEKKA_99',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_OUTOU_KEKKA_99(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_99(),
            },
        },
        {
            'case_name': 'TOTO_BUY_OUTOU_KEKKA_99_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_OUTOU_KEKKA_99(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_99_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_BUY_OUTOU_KEKKA_99_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_BUY_OUTOU_KEKKA_99(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_BUY_OUTOU_KEKKA_99_CANCEL(),
            },
        },

    ]

# ---------------------------
# スポーツ振興くじ マッピングNo2 テストデータ
# ---------------------------
def get_reqres_toto_ticket_vote():
    return [
        {
            'case_name': 'TOTO_VOTE_CASE_01_BUY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_01_BUY(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_01_BUY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_01_BUY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_01',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_01(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_01_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_01_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_02_BUY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_02(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_02_BUY(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_02_BUY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_02(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_02_BUY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_02',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_02(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_02(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_02_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_02(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_02_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_03_BUY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_03(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_03_BUY(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_03_BUY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_03(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_03_BUY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_03',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_03(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_03(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_03_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_03(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_03_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_04_BUY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_04(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_04_BUY(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_04_BUY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_04(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_04_BUY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_04',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_04(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_04(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_04_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_04(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_04_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_05_BUY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_05(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_05_BUY(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_05_BUY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_05(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_05_BUY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_05',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_05(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_05(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_05_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_05(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_05_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_06_BUY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_06(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_06_BUY(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_06_BUY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_06(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_06_BUY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_06',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_06(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_06(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_06_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_06(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_06_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_07_BUY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_07(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_07_BUY(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_07_BUY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_07(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_07_BUY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_07',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_07(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_07(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_07_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_07(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_07_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_08_BUY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_08(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_08_BUY(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_08_BUY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_08(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_08_BUY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_08',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_08(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_08(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_08_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_08(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_08_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_09_BUY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_09(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_09_BUY(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_07_BUY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_09(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_09_BUY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_09',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_09(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_09(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_CASE_09_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_CASE_09(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_CASE_09_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_SYORI_KEKKA_15_BUY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_VOTE_SYORI_KEKKA_15(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_15_BUY(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_SYORI_KEKKA_15_BUY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_SYORI_KEKKA_15(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_15_BUY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_SYORI_KEKKA_15',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE(),
                'X_barcode': BARCODE_TOTO_VOTE_SYORI_KEKKA_15(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_15(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_SYORI_KEKKA_15_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_SYORI_KEKKA_15(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_15_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_SYORI_KEKKA_16_BUY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_VOTE_SYORI_KEKKA_16(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_16_BUY(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_SYORI_KEKKA_16_BUY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_SYORI_KEKKA_16(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_16_BUY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_SYORI_KEKKA_16',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE(),
                'X_barcode': BARCODE_TOTO_VOTE_SYORI_KEKKA_16(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_16(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_SYORI_KEKKA_16_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_SYORI_KEKKA_16(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_16_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_SYORI_KEKKA_99_400_BUY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_VOTE_SYORI_KEKKA_99_400(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_99_400_BUY(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_SYORI_KEKKA_99_400_BUY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_SYORI_KEKKA_99_400(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_99_400_BUY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_SYORI_KEKKA_99_400',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE(),
                'X_barcode': BARCODE_TOTO_VOTE_SYORI_KEKKA_99_400(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_99_400(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_SYORI_KEKKA_99_400_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_SYORI_KEKKA_99_400(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_99_400_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_SYORI_KEKKA_99_500_BUY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_VOTE_SYORI_KEKKA_99_500(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_99_500_BUY(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_SYORI_KEKKA_99_500_BUY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_SYORI_KEKKA_99_500(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_99_500_BUY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_SYORI_KEKKA_99_500',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE(),
                'X_barcode': BARCODE_TOTO_VOTE_SYORI_KEKKA_99_500(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_99_500(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_SYORI_KEKKA_99_500_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_SYORI_KEKKA_99_500(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_99_500_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_SYORI_KEKKA_TIMEOUT_BUY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_VOTE_SYORI_KEKKA_TIMEOUT(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_TIMEOUT_BUY(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_SYORI_KEKKA_TIMEOUT_BUY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_SYORI_KEKKA_TIMEOUT(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_TIMEOUT_BUY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_SYORI_KEKKA_TIMEOUT',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE(),
                'X_barcode': BARCODE_TOTO_VOTE_SYORI_KEKKA_TIMEOUT(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_TIMEOUT(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_SYORI_KEKKA_TIMEOUT_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_SYORI_KEKKA_TIMEOUT(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_TIMEOUT_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_SYORI_KEKKA_TIMEOUT_99_BUY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_VOTE_SYORI_KEKKA_TIMEOUT_99(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_TIMEOUT_99_BUY(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_SYORI_KEKKA_TIMEOUT_99_BUY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_SYORI_KEKKA_TIMEOUT_99(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_TIMEOUT_99_BUY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_SYORI_KEKKA_TIMEOUT_99',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE(),
                'X_barcode': BARCODE_TOTO_VOTE_SYORI_KEKKA_TIMEOUT_99(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_TIMEOUT_99(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_SYORI_KEKKA_TIMEOUT_99_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_SYORI_KEKKA_TIMEOUT_99(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_SYORI_KEKKA_TIMEOUT_99_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_01_BUY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_01_BUY(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_01_BUY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_01_BUY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_01',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_01(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_01_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_01_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_04_BUY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_04(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_04_BUY(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_04_BUY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_04(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_04_BUY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_04',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_04(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_04(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_04_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_04(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_04_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_06_BUY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_06(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_06_BUY(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_06_BUY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_06(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_06_BUY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_06',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_06(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_06(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_06_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_06(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_06_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_07_BUY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_07(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_07_BUY(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_07_BUY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_07(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_07_BUY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_07',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_07(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_07(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_07_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_07(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_07_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_08_BUY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_08(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_08_BUY(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_08_BUY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_08(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_08_BUY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_08',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_08(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_08(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_08_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_08(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_08_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_11_BUY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_11(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_11_BUY(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_11_BUY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_11(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_11_BUY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_11',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_11(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_11(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_11_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_11(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_11_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_12_BUY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_12(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_12_BUY(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_12_BUY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_12(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_12_BUY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_12',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_12(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_12(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_12_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_12(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_12_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_13_BUY',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_13(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_13_BUY(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_13_BUY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_13(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_13_BUY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_13',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_13(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_13(),
            },
        },
        {
            'case_name': 'TOTO_VOTE_OUTOU_KEKKA_13_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_VOTE_CANCEL(),
                'X_barcode': BARCODE_TOTO_VOTE_OUTOU_KEKKA_13(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_VOTE_OUTOU_KEKKA_13_CANCEL(),
            },
        },
    ]

# ---------------------------
# スポーツ振興くじ マッピングNo3 テストデータ
# ---------------------------
def get_reqres_toto_ticket_repay():
    return [
        {
            'case_name': 'TOTO_REPAY_CASE_01',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_REPAY_CASE_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_CASE_01(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_CASE_01_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_REPAY_CASE_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_CASE_01_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_CASE_02',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_REPAY_CASE_02(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_CASE_02(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_CASE_02_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_REPAY_CASE_02(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_CASE_02_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_CASE_03',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_REPAY_CASE_03(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_CASE_03(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_CASE_03_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_REPAY_CASE_03(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_CASE_03_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_CASE_03_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_REPAY_CASE_03(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_CASE_03_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_CASE_04',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_REPAY_CASE_04(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_CASE_04(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_CASE_04_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_REPAY_CASE_04(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_CASE_04_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_SYORI_KEKKA_14',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_REPAY_SYORI_KEKKA_14(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_14(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_SYORI_KEKKA_14_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_REPAY_SYORI_KEKKA_14(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_14_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_SYORI_KEKKA_14_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_REPAY_SYORI_KEKKA_14(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_14_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_SYORI_KEKKA_14_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_REPAY_SYORI_KEKKA_14(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_14_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_SYORI_KEKKA_16',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_REPAY_SYORI_KEKKA_16(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_16(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_SYORI_KEKKA_16_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_REPAY_SYORI_KEKKA_16(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_16_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_SYORI_KEKKA_99_400',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_REPAY_SYORI_KEKKA_99_400(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_99_400(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_SYORI_KEKKA_99_400_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_REPAY_SYORI_KEKKA_99_400(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_99_400_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_SYORI_KEKKA_99_400_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_REPAY_SYORI_KEKKA_99_400(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_99_400_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_SYORI_KEKKA_99_400_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_REPAY_SYORI_KEKKA_99_400(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_99_400_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_SYORI_KEKKA_99_500',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_REPAY_SYORI_KEKKA_99_500(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_99_500(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_SYORI_KEKKA_99_500_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_REPAY_SYORI_KEKKA_99_500(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_99_500_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_SYORI_KEKKA_99_500_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_REPAY_SYORI_KEKKA_99_500(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_99_500_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_SYORI_KEKKA_TIMEOUT',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_REPAY_SYORI_KEKKA_TIMEOUT(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_TIMEOUT(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_SYORI_KEKKA_TIMEOUT_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_REPAY_SYORI_KEKKA_TIMEOUT(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_TIMEOUT_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_SYORI_KEKKA_TIMEOUT_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_REPAY_SYORI_KEKKA_TIMEOUT(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_TIMEOUT_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_SYORI_KEKKA_TIMEOUT_99',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_REPAY_SYORI_KEKKA_TIMEOUT_99(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_TIMEOUT_99(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_SYORI_KEKKA_TIMEOUT_99_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_REPAY_SYORI_KEKKA_TIMEOUT_99(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_TIMEOUT_99_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_SYORI_KEKKA_TIMEOUT_99_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_REPAY_SYORI_KEKKA_TIMEOUT_99(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_SYORI_KEKKA_TIMEOUT_99_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_OUTOU_KEKKA_01',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_REPAY_OUTOU_KEKKA_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_01(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_OUTOU_KEKKA_01_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_REPAY_OUTOU_KEKKA_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_01_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_OUTOU_KEKKA_01_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_REPAY_OUTOU_KEKKA_01(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_01_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_OUTOU_KEKKA_02',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_REPAY_OUTOU_KEKKA_02(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_02(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_OUTOU_KEKKA_02_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_REPAY_OUTOU_KEKKA_02(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_02_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_OUTOU_KEKKA_02_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_REPAY_OUTOU_KEKKA_02(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_02_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_OUTOU_KEKKA_02_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_REPAY_OUTOU_KEKKA_02(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_02_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_OUTOU_KEKKA_03',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_REPAY_OUTOU_KEKKA_03(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_03(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_OUTOU_KEKKA_03_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_REPAY_OUTOU_KEKKA_03(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_03_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_OUTOU_KEKKA_03_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_REPAY_OUTOU_KEKKA_03(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_03_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_OUTOU_KEKKA_05',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_REPAY_OUTOU_KEKKA_05(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_05(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_OUTOU_KEKKA_05_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_REPAY_OUTOU_KEKKA_05(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_05_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_OUTOU_KEKKA_06',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_REPAY_OUTOU_KEKKA_06(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_06(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_OUTOU_KEKKA_06_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_REPAY_OUTOU_KEKKA_06(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_06_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_OUTOU_KEKKA_06_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_REPAY_OUTOU_KEKKA_06(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_06_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_OUTOU_KEKKA_07',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_REPAY_OUTOU_KEKKA_07(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_07(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_OUTOU_KEKKA_07_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_REPAY_OUTOU_KEKKA_07(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_07_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_OUTOU_KEKKA_07_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_REPAY_OUTOU_KEKKA_07(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_07_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_OUTOU_KEKKA_08',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_REPAY_OUTOU_KEKKA_08(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_08(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_OUTOU_KEKKA_08_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_REPAY_OUTOU_KEKKA_08(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_08_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_OUTOU_KEKKA_08_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_REPAY_OUTOU_KEKKA_08(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_08_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_OUTOU_KEKKA_99',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_REPAY_OUTOU_KEKKA_99(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_99(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_OUTOU_KEKKA_99_RETRY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_REPAY_OUTOU_KEKKA_99(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_99_RETRY(),
            },
        },
        {
            'case_name': 'TOTO_REPAY_OUTOU_KEKKA_99_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_REPAY_OUTOU_KEKKA_99(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_REPAY_OUTOU_KEKKA_99_CANCEL(),
            },
        },

    ]

# ---------------------------
# スポーツ振興くじ マッピングNo4 テストデータ
# ---------------------------
def get_reqres_toto_ticket_clearing():
    return [
        {
            'case_name': 'TOTO_CLEARING_CASE_01_REPAY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_CLEARING_CASE_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_CASE_01_REPAY(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_CASE_01_REPAY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_CLEARING_CASE_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_CASE_01_REPAY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_CASE_01',
            'req': { 
                **DEFAULT_DICT_TOTO_CLEARING(),
                'X_barcode': BARCODE_TOTO_CLEARING_CASE_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_CASE_01(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_CASE_02_REPAY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_CLEARING_CASE_02(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_CASE_02_REPAY(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_CASE_02_REPAY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_CLEARING_CASE_02(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_CASE_02_REPAY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_CASE_02',
            'req': { 
                **DEFAULT_DICT_TOTO_CLEARING(),
                'X_barcode': BARCODE_TOTO_CLEARING_CASE_02(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_CASE_02(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_CASE_03_REPAY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_CLEARING_CASE_03(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_CASE_03_REPAY(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_CASE_03_REPAY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_CLEARING_CASE_03(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_CASE_03_REPAY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_CASE_03',
            'req': { 
                **DEFAULT_DICT_TOTO_CLEARING(),
                'X_barcode': BARCODE_TOTO_CLEARING_CASE_03(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_CASE_03(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_CASE_04_REPAY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_CLEARING_CASE_04(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_CASE_04_REPAY(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_CASE_04_REPAY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_CLEARING_CASE_04(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_CASE_04_REPAY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_CASE_04',
            'req': { 
                **DEFAULT_DICT_TOTO_CLEARING(),
                'X_barcode': BARCODE_TOTO_CLEARING_CASE_04(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_CASE_04(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_SYORI_KEKKA_15_REPAY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_CLEARING_SYORI_KEKKA_15(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_15_REPAY(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_SYORI_KEKKA_15_REPAY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_CLEARING_SYORI_KEKKA_15(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_15_REPAY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_SYORI_KEKKA_15',
            'req': { 
                **DEFAULT_DICT_TOTO_CLEARING(),
                'X_barcode': BARCODE_TOTO_CLEARING_SYORI_KEKKA_15(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_15(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_SYORI_KEKKA_16_REPAY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_CLEARING_SYORI_KEKKA_16(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_16_REPAY(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_SYORI_KEKKA_16_REPAY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_CLEARING_SYORI_KEKKA_16(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_16_REPAY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_SYORI_KEKKA_16',
            'req': { 
                **DEFAULT_DICT_TOTO_CLEARING(),
                'X_barcode': BARCODE_TOTO_CLEARING_SYORI_KEKKA_16(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_16(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_SYORI_KEKKA_99_REPAY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_CLEARING_SYORI_KEKKA_99(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_99_REPAY(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_SYORI_KEKKA_99_REPAY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_CLEARING_SYORI_KEKKA_99(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_99_REPAY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_SYORI_KEKKA_99',
            'req': { 
                **DEFAULT_DICT_TOTO_CLEARING(),
                'X_barcode': BARCODE_TOTO_CLEARING_SYORI_KEKKA_99(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_99(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_SYORI_KEKKA_99_REPAY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_CLEARING_SYORI_KEKKA_99(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_99_REPAY(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_SYORI_KEKKA_99_REPAY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_CLEARING_SYORI_KEKKA_99(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_99_REPAY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_SYORI_KEKKA_99',
            'req': { 
                **DEFAULT_DICT_TOTO_CLEARING(),
                'X_barcode': BARCODE_TOTO_CLEARING_SYORI_KEKKA_99(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_99(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_SYORI_KEKKA_TIMEOUT_REPAY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_CLEARING_SYORI_KEKKA_TIMEOUT(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_TIMEOUT_REPAY(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_SYORI_KEKKA_TIMEOUT_REPAY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_CLEARING_SYORI_KEKKA_TIMEOUT(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_TIMEOUT_REPAY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_SYORI_KEKKA_TIMEOUT',
            'req': { 
                **DEFAULT_DICT_TOTO_CLEARING(),
                'X_barcode': BARCODE_TOTO_CLEARING_SYORI_KEKKA_TIMEOUT(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_TIMEOUT(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_SYORI_KEKKA_TIMEOUT_99_REPAY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_CLEARING_SYORI_KEKKA_TIMEOUT_99(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_TIMEOUT_99_REPAY(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_SYORI_KEKKA_TIMEOUT_99_REPAY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_CLEARING_SYORI_KEKKA_TIMEOUT_99(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_TIMEOUT_99_REPAY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_SYORI_KEKKA_TIMEOUT_99',
            'req': { 
                **DEFAULT_DICT_TOTO_CLEARING(),
                'X_barcode': BARCODE_TOTO_CLEARING_SYORI_KEKKA_TIMEOUT_99(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_SYORI_KEKKA_TIMEOUT_99(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_00_REPAY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_00(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_00_REPAY(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_00_REPAY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_00(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_00_REPAY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_00',
            'req': { 
                **DEFAULT_DICT_TOTO_CLEARING(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_00(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_00(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_01_REPAY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_01_REPAY(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_01_REPAY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_01_REPAY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_01',
            'req': { 
                **DEFAULT_DICT_TOTO_CLEARING(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_01(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_04_REPAY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_04(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_04_REPAY(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_04_REPAY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_04(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_04_REPAY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_04',
            'req': { 
                **DEFAULT_DICT_TOTO_CLEARING(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_04(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_04(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_06_REPAY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_06(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_06_REPAY(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_06_REPAY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_06(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_06_REPAY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_06',
            'req': { 
                **DEFAULT_DICT_TOTO_CLEARING(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_06(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_06(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_07_REPAY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_07(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_07_REPAY(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_07_REPAY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_07(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_07_REPAY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_07',
            'req': { 
                **DEFAULT_DICT_TOTO_CLEARING(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_07(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_07(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_08_REPAY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_08(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_08_REPAY(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_08_REPAY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_08(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_08_REPAY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_08',
            'req': { 
                **DEFAULT_DICT_TOTO_CLEARING(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_08(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_08(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_11_REPAY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_11(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_11_REPAY(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_11_REPAY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_11(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_11_REPAY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_11',
            'req': { 
                **DEFAULT_DICT_TOTO_CLEARING(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_11(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_11(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_12_REPAY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_12(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_12_REPAY(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_12_REPAY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_12(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_12_REPAY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_12',
            'req': { 
                **DEFAULT_DICT_TOTO_CLEARING(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_12(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_12(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_13_REPAY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_13(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_13_REPAY(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_13_REPAY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_13(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_13_REPAY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_13',
            'req': { 
                **DEFAULT_DICT_TOTO_CLEARING(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_13(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_13(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_14_REPAY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_14(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_14_REPAY(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_14_REPAY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_14(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_14_REPAY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_14',
            'req': { 
                **DEFAULT_DICT_TOTO_CLEARING(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_14(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_14(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_99_REPAY',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_99(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_99_REPAY(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_99_REPAY_CANCEL',
            'req': { 
                **DEFAULT_DICT_TOTO_REPAY_CANCEL(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_99(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_99_REPAY_CANCEL(),
            },
        },
        {
            'case_name': 'TOTO_CLEARING_OUTOU_KEKKA_99',
            'req': { 
                **DEFAULT_DICT_TOTO_CLEARING(),
                'X_barcode': BARCODE_TOTO_CLEARING_OUTOU_KEKKA_99(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_TOTO_CLEARING_OUTOU_KEKKA_99(),
            },
        },

    ]

# ---------------------------
# スポーツ振興くじ 異常系テストデータ
# ---------------------------
def get_reqres_toto_ticket_error():
    error_dict = [
        {
            # 要求区分なし
            'case_name': 'ERROR_TOTO_TICKET_YOKYU_KBN_NONE',
            'req': { 
                'X_barcode': BARCODE_TOTO_BUY_CASE_01(),
            },
            'res': { 
                **RESPONSE_X_SHORI_KEKKA_99(),
            },
        },
        {
            # バーコードなし
            'case_name': 'ERROR_TOTO_TICKET_BARCODE_NONE',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
            },
            'res': { 
                **RESPONSE_X_SHORI_KEKKA_99(),
            },
        },
        {
            'case_name': 'ERROR_TOTO_TICKET_YOKYU_KBN',
            'req': { 
                **DEFAULT_DICT_TOTO_BUY(),
                'X_barcode': BARCODE_TOTO_BUY_CASE_01(),
                'X_yokyu_kbn': '00',
            },
            'res': { 
                **RESPONSE_X_SHORI_KEKKA_99(),
            },
        },
    ]

    key_error_dict = [
        {
            # キー不足
            'case_name': f'ERROR_TOTO_TICKET_LACK_KEY(yokyu_kbn:{yokyu_kbn})',
            'req': { 
                'X_yokyu_kbn': yokyu_kbn,
                'X_barcode': BARCODE_TOTO_BUY_CASE_01(),
            },
            'res': { 
                **RESPONSE_X_SHORI_KEKKA_99(),
            },
        } for yokyu_kbn in ['01', '11', '02', '12', '03', '13', '04']
    ]

    return error_dict + key_error_dict