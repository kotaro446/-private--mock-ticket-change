from test_barcode_functions import *
from test_compare_response_in_ticket import *

# ---------------------------
# インターネットチケット入金／発券問合せ マッピングNo1 テストデータ
# ---------------------------
def get_reqres_in_ticket():
    return [
        {
            'case_name': 'IN_TICKET_CASE_01',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_CASE_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_01(),
            },
        },
        {
            'case_name': 'IN_TICKET_CASE_01_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_CASE_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_01_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_CASE_02',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_CASE_02(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_02(),
            },
        },
        {
            'case_name': 'IN_TICKET_CASE_02_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_CASE_02(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_02_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_CASE_03',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_CASE_03(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_03(),
            },
        },
        {
            'case_name': 'IN_TICKET_CASE_03_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_CASE_03(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_03_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_CASE_04',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_CASE_04(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_04(),
            },
        },
        {
            'case_name': 'IN_TICKET_CASE_04_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_CASE_04(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_04_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_CASE_05',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_CASE_05(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_05(),
            },
        },
        {
            'case_name': 'IN_TICKET_CASE_05_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_CASE_05(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_05_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_CASE_06',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_CASE_06(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_06(),
            },
        },
        {
            'case_name': 'IN_TICKET_CASE_06_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_CASE_06(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_06_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_CASE_07',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_CASE_07(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_07(),
            },
        },
        {
            'case_name': 'IN_TICKET_CASE_07_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_CASE_07(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_07_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_CASE_08',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_CASE_08(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_08(),
            },
        },
        {
            'case_name': 'IN_TICKET_CASE_08_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_CASE_08(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_08_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_CASE_09',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_CASE_09(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_09(),
            },
        },
        {
            'case_name': 'IN_TICKET_CASE_09_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_CASE_09(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_09_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_CASE_10',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_CASE_10(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_10(),
            },
        },
        {
            'case_name': 'IN_TICKET_CASE_10_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_CASE_10(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_10_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_SYORI_KEKKA_11',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_SYORI_KEKKA_11(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_11(),
            },
        },
        {
            'case_name': 'IN_TICKET_SYORI_KEKKA_11_RETRY',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_SYORI_KEKKA_11(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_11_RETRY(),
            },
        },
        {
            'case_name': 'IN_TICKET_SYORI_KEKKA_11_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_SYORI_KEKKA_11(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_11_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_SYORI_KEKKA_14',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_SYORI_KEKKA_14(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_14(),
            },
        },
        {
            'case_name': 'IN_TICKET_SYORI_KEKKA_14_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_SYORI_KEKKA_14(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_14_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_SYORI_KEKKA_15',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_SYORI_KEKKA_15(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_15(),
            },
        },
        {
            'case_name': 'IN_TICKET_SYORI_KEKKA_15_RETRY',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_SYORI_KEKKA_15(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_15_RETRY(),
            },
        },
        {
            'case_name': 'IN_TICKET_SYORI_KEKKA_15_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_SYORI_KEKKA_15(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_15_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_SYORI_KEKKA_15_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_SYORI_KEKKA_15(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_15_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'IN_TICKET_SYORI_KEKKA_99_400',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_SYORI_KEKKA_99_400(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_99_400(),
            },
        },
        {
            'case_name': 'IN_TICKET_SYORI_KEKKA_99_400_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_SYORI_KEKKA_99_400(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_99_400_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_SYORI_KEKKA_99_400_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_SYORI_KEKKA_99_400(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_99_400_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'IN_TICKET_SYORI_KEKKA_99_500',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_SYORI_KEKKA_99_500(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_99_500(),
            },
        },
        {
            'case_name': 'IN_TICKET_SYORI_KEKKA_99_500_RETRY',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_SYORI_KEKKA_99_500(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_99_500_RETRY(),
            },
        },
        {
            'case_name': 'IN_TICKET_SYORI_KEKKA_99_500_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_SYORI_KEKKA_99_500(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_99_500_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_TIMEOUT',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_TIMEOUT(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_TIMEOUT(),
            },
        },
        {
            'case_name': 'IN_TICKET_TIMEOUT_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_TIMEOUT(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_TIMEOUT_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_TIMEOUT_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_TIMEOUT(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_TIMEOUT_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'IN_TICKET_TIMEOUT_500',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_TIMEOUT_500(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_TIMEOUT_500(),
            },
        },
        {
            'case_name': 'IN_TICKET_TIMEOUT_500_RETRY',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_TIMEOUT_500(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_TIMEOUT_500_RETRY(),
            },
        },
        {
            'case_name': 'IN_TICKET_TIMEOUT_500_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_TIMEOUT_500(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_TIMEOUT_500_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_TIMEOUT_500_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_TIMEOUT_500(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_TIMEOUT_500_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_01',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_01(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_01_RETRY',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_01(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_01_RETRY(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_01_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_01_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_02',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_02(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_02(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_02_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_02(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_02_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_02_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_02(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_02_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_03',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_03(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_03(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_03_RETRY',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_03(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_03_RETRY(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_03_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_03(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_03_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_05',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_05(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_05(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_05_RETRY',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_05(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_05_RETRY(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_05_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_05(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_05_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_05_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_05(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_05_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_07',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_07(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_07(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_07_RETRY',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_07(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_07_RETRY(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_07_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_07(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_07_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_08',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_08(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_08(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_08_RETRY',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_08(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_08_RETRY(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_08_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_08(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_08_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_08_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_08(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_08_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_13',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_13(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_13(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_13_RETRY',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_13(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_13_RETRY(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_13_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_13(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_13_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_13_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_13(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_13_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_14',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_14(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_14(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_14_RETRY',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_14(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_14_RETRY(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_14_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_14(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_14_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_15',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_15(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_15(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_15_RETRY',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_15(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_15_RETRY(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_15_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_15(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_15_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_99',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_99(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_99(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_99_RETRY',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_99(),
                'X_saiso_kbn': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_99_RETRY(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_99_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_99(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_99_CANCEL(),
            },
        },

    ]

# ---------------------------
# インターネットチケット入金／発券問合せ マッピングNo2 テストデータ
# ---------------------------
def get_reqres_in_ticket_detail():
    return [
        {
            'case_name': 'IN_TICKET_DETAIL_NO_TICKET',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_NO_TICKET(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_NO_TICKET(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_NO_TICKET_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_NO_TICKET(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_NO_TICKET_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_A',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_A(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_A(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_A_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_A(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_A_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_B',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_B(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_B(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_B_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_B(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_B_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_C',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_C(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_C(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_C_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_C(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_C_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_A_D',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_A_D(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_A_D(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_A_D_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_A_D(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_A_D_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_A_E',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_A_E(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_A_E(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_A_E_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_A_E(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_A_E_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_A_F',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_A_F(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_A_F(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_A_F_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_A_F(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_A_F_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_B_D',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_B_D(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_B_D(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_B_D_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_B_D(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_B_D_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_B_E',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_B_E(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_B_E(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_B_E_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_B_E(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_B_E_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_B_F',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_B_F(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_B_F(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_B_F_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_B_F(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_B_F_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_C_D',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_C_D(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_C_D(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_C_D_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_C_D(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_C_D_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_C_E',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_C_E(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_C_E(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_C_E_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_C_E(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_C_E_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_C_F',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_C_F(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_C_F(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_C_F_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_C_F(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_C_F_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_G',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_G(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_G(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_G_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_G(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_G_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_H01',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_H01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_H01(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_H01_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_H01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_H01_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_J01',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_J01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_J01(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_J01_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_J01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_J01_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_K01',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_K01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_K01(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_K01_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_K01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_K01_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_L01',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_L01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_L01(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_L01_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_L01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_L01_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_M01',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_M01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_M01(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_M01_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_M01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_M01_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_N01',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_N01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_N01(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_N01_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_N01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_N01_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_P01',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_P01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_P01(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_P01_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_P01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_P01_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_R01',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_R01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_R01(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_R01_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_R01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_R01_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_S01',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_S01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_S01(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_S01_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_S01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_S01_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_TU',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_TU(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_TU(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_TU_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_TU(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_TU_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_VW',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_VW(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_VW(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_VW_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_VW(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_VW_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_CASE_01',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_CASE_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_01(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_CASE_01_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_CASE_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_01_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_CASE_02',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_CASE_02(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_02(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_CASE_02_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_CASE_02(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_02_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_CASE_03',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_CASE_03(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_03(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_CASE_03_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_CASE_03(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_03_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_CASE_04',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_CASE_04(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_04(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_CASE_04_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_CASE_04(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_04_CANCEL(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_CASE_05',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_CASE_05(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_05(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_CASE_05_CANCEL',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_CANCEL(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_CASE_05(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_05_CANCEL(),
            },
        },
    ]

# ---------------------------
# インターネットチケット完了通知 マッピングNo1 テストデータ
# ---------------------------
def get_reqres_in_ticket_kanryo():
    return [
        {
            'case_name': 'IN_TICKET_CASE_01_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_CASE_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_01_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_CASE_02_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_CASE_02(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_02_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_CASE_03_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_CASE_03(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_03_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_CASE_04_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_CASE_04(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_04_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_CASE_05_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_CASE_05(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_05_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_CASE_06_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_CASE_06(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_06_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_CASE_07_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_CASE_07(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_07_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_CASE_08_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_CASE_08(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_08_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_CASE_09_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_CASE_09(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_09_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_CASE_10_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_CASE_10(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_CASE_10_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_SYORI_KEKKA_11_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_SYORI_KEKKA_11(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_11_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_SYORI_KEKKA_14_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_SYORI_KEKKA_14(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_14_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_SYORI_KEKKA_15_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_SYORI_KEKKA_15(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_15_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_SYORI_KEKKA_99_400_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_SYORI_KEKKA_99_400(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_99_400_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_SYORI_KEKKA_99_500_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_SYORI_KEKKA_99_500(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_SYORI_KEKKA_99_500_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_TIMEOUT_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_TIMEOUT(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_TIMEOUT_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_TIMEOUT_500_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_TIMEOUT_500(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_TIMEOUT_500_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_01_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_01_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_02_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_02(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_02_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_03_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_03(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_03_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_05_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_05(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_05_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_07_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_07(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_07_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_08_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_08(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_08_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_13_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_13(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_13_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_14_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_14(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_14_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_15_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_15(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_15_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_OUTOU_KEKKA_99_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_OUTOU_KEKKA_99(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_OUTOU_KEKKA_99_KANRYO(),
            },
        },

    ]

# ---------------------------
# インターネットチケット完了通知 マッピングNo2 テストデータ
# ---------------------------
def get_reqres_in_ticket_detail_kanryo():
    return [
        {
            'case_name': 'IN_TICKET_DETAIL_NO_TICKET_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_NO_TICKET(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_NO_TICKET_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_A_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_A(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_A_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_B_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_B(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_B_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_C_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_C(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_C_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_A_D_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_A_D(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_A_D_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_A_E_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_A_E(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_A_E_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_A_F_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_A_F(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_A_F_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_B_D_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_B_D(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_B_D_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_B_E_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_B_E(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_B_E_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_B_F_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_B_F(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_B_F_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_C_D_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_C_D(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_C_D_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_C_E_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_C_E(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_C_E_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_C_F_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_C_F(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_C_F_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_G_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_G(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_G_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_H01_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_H01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_H01_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_J01_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_J01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_J01_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_K01_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_K01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_K01_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_L01_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_L01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_L01_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_M01_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_M01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_M01_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_N01_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_N01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_N01_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_P01_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_P01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_P01_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_R01_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_R01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_R01_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_S01_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_S01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_S01_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_TU_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_TU(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_TU_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_VW_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_VW(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_VW_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_CASE_01_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_CASE_01(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_01_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_CASE_02_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_CASE_02(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_02_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_CASE_03_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_CASE_03(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_03_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_CASE_04_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_CASE_04(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_04_KANRYO(),
            },
        },
        {
            'case_name': 'IN_TICKET_DETAIL_CASE_05_KANRYO',
            'req': { 
                **DEFAULT_DICT_IN_TICKET_KANRYO(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_CASE_05(),

            },
            'res': { 
                **RESPONSE_TICKET_DATA_IN_TICKET_DETAIL_CASE_05_KANRYO(),
            },
        },
    ]

# ---------------------------
# インターネットチケット 異常系 テストデータ
# ---------------------------
def get_reqres_in_ticket_error():
    error_dict = [
        {
            # 要求区分なし
            'case_name': 'ERROR_IN_TICKET_YOKYU_KBN_NONE',
            'req': { 
                'X_barcode': BARCODE_IN_TICKET_CASE_01(),
            },
            'res': { 
                **RESPONSE_X_SHORI_KEKKA_99(),
            },
        },
        {
            # バーコードなし
            'case_name': 'ERROR_IN_TICKET_BARCODE_NONE',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
            },
            'res': { 
                **RESPONSE_X_SHORI_KEKKA_99(),
            },
        },
        {
            # 要求区分不正
            'case_name': 'ERROR_IN_TICKET_YOKYU_KBN_MAP1',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_CASE_01(),
                'X_yokyu_kbn': '00',
            },
            'res': { 
                **RESPONSE_X_SHORI_KEKKA_99(),
            },
        },
        {
            # 要求区分不正
            'case_name': 'ERROR_IN_TICKET_YOKYU_KBN_MAP2',
            'req': { 
                **DEFAULT_DICT_IN_TICKET(),
                'X_barcode': BARCODE_IN_TICKET_DETAIL_S01(),
                'X_yokyu_kbn': '00',
            },
            'res': { 
                **RESPONSE_X_SHORI_KEKKA_99(),
            },
        },
    ]

    key_error_dict1 = [
        {
            # マッピングNo1 キー不足
            'case_name': f'ERROR_IN_TICKET_MAPPING_NO1_LACK_KEY(yokyu_kbn:{yokyu_kbn})',
            'req': { 
                'X_yokyu_kbn': yokyu_kbn,
                'X_barcode': BARCODE_IN_TICKET_CASE_01(),
            },
            'res': { 
                **RESPONSE_X_SHORI_KEKKA_99(),
            },
        } for yokyu_kbn in ['01', '21', '02', '12', ]
    ]

    key_error_dict2 = [
        {
            # マッピングNo2 キー不足
            'case_name': f'ERROR_IN_TICKET_MAPPING_NO2_LACK_KEY(yokyu_kbn:{yokyu_kbn})',
            'req': { 
                'X_yokyu_kbn': yokyu_kbn,
                'X_barcode': BARCODE_IN_TICKET_DETAIL_S01(),
            },
            'res': { 
                **RESPONSE_X_SHORI_KEKKA_99(),
            },
        } for yokyu_kbn in ['01', '21', '02', '12', ]
    ]

    return error_dict + key_error_dict1 + key_error_dict2