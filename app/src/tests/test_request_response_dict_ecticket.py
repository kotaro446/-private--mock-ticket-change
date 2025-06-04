from test_barcode_functions import *
from test_compare_response_ecticket import *

# ---------------------------
# Mcopyチケット マッピングNo1 EC関連問合せ テストデータ
# ---------------------------
def get_reqres_ecticket():
    return [
        {
            'case_name': 'MCOPY_TICKET_CASE_01',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_01(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_01(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_01_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_01(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_01_CANCEL(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_02',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_02(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_02(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_02_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_02(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_02_CANCEL(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_03',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_03(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_03(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_03_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_03(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_03_CANCEL(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_04',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_04(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_04(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_04_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_04(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_04_CANCEL(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_04_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_04(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_04_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_05',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_05(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_05(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_05_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_05(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_05_CANCEL(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_05_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_05(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_05_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_06',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_06(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_06(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_06_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_06(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_06_CANCEL(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_06_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_06(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_06_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_07',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_07(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_07(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_07_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_07(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_07_CANCEL(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_08',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_08(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_08(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_08_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_08(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_08_CANCEL(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_09',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_09(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_09(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_09_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_09(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_09_CANCEL(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_10',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_10(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_10(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_10_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_10(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_10_CANCEL(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_10_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_10(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_10_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_SYORI_KEKKA_10',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_10(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_10(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_SYORI_KEKKA_10_RETRY',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_10(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_10_RETRY(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_SYORI_KEKKA_10_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_10(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_10_CANCEL(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_SYORI_KEKKA_11',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_11(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_11(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_SYORI_KEKKA_11_RETRY',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_11(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_11_RETRY(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_SYORI_KEKKA_11_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_11(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_11_CANCEL(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_SYORI_KEKKA_11_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_11(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_11_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_SYORI_KEKKA_14',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_14(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_14(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_SYORI_KEKKA_14_RETRY',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_14(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_14_RETRY(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_SYORI_KEKKA_14_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_14(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_14_CANCEL(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_SYORI_KEKKA_14_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_14(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_14_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_SYORI_KEKKA_99_400',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_99_400(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_99_400(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_SYORI_KEKKA_99_400_RETRY',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_99_400(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_99_400_RETRY(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_SYORI_KEKKA_99_400_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_99_400(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_99_400_CANCEL(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_SYORI_KEKKA_99_400_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_99_400(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_99_400_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_SYORI_KEKKA_99_500',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_99_500(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_99_500(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_SYORI_KEKKA_99_500_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_99_500(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_99_500_CANCEL(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_SYORI_KEKKA_TIMEOUT',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_TIMEOUT(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_TIMEOUT(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_SYORI_KEKKA_TIMEOUT_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_TIMEOUT(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_TIMEOUT_CANCEL(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_SYORI_KEKKA_TIMEOUT_99',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_TIMEOUT_99(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_TIMEOUT_99(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_SYORI_KEKKA_TIMEOUT_99_RETRY',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_TIMEOUT_99(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_TIMEOUT_99_RETRY(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_SYORI_KEKKA_TIMEOUT_99_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_TIMEOUT_99(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_TIMEOUT_99_CANCEL(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_01',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_01(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_01(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_01_RETRY',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_01(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_01_RETRY(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_01_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_01(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_01_CANCEL(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_01_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_01(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_01_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_02',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_02(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_02(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_02_RETRY',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_02(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_02_RETRY(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_02_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_02(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_02_CANCEL(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_03',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_03(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_03(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_03_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_03(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_03_CANCEL(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_03_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_03(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_03_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_05',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_05(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_05(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_05_RETRY',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_05(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_05_RETRY(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_05_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_05(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_05_CANCEL(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_05_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_05(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_05_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_11',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_11(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_11(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_11_RETRY',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_11(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_11_RETRY(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_11_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_11(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_11_CANCEL(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_11_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_11(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_11_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_12',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_12(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_12(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_12_RETRY',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_12(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_12_RETRY(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_12_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_12(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_12_CANCEL(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_12_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_12(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_12_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_16',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_16(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_16(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_16_RETRY',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_16(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_16_RETRY(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_16_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_16(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_16_CANCEL(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_16_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_16(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_16_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_99',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_99(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_99(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_99_RETRY',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_99(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_99_RETRY(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_99_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_99(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_99_CANCEL(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_99_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_99(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_99_CANCEL_RETRY(),
            },
        },
    ]

# ---------------------------
# Mcopyチケット マッピングNo1 EC関連完了 テストデータ
# ---------------------------
def get_reqres_ecticket_kanryo():
    return [
        {
            'case_name': 'MCOPY_TICKET_CASE_01_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_01(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_01_KANRYO(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_02_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_02(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_02_KANRYO(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_03_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_03(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_03_KANRYO(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_04_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_04(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_04_KANRYO(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_05_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_05(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_05_KANRYO(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_06_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_06(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_06_KANRYO(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_07_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_07(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_07_KANRYO(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_08_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_08(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_08_KANRYO(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_09_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_09(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_09_KANRYO(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_CASE_10_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_10(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_CASE_10_KANRYO(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_SYORI_KEKKA_10_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_10(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_10_KANRYO(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_SYORI_KEKKA_11_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_11(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_11_KANRYO(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_SYORI_KEKKA_14_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_14(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_14_KANRYO(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_SYORI_KEKKA_99_400_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_99_400(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_99_400_KANRYO(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_SYORI_KEKKA_99_500_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_99_500(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_99_500_KANRYO(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_SYORI_KEKKA_TIMEOUT_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_TIMEOUT(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_TIMEOUT_KANRYO(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_SYORI_KEKKA_TIMEOUT_99_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_SYORI_KEKKA_TIMEOUT_99(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_SYORI_KEKKA_TIMEOUT_99_KANRYO(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_01_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_01(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_01_KANRYO(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_02_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_02(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_02_KANRYO(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_03_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_03(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_03_KANRYO(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_05_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_05(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_05_KANRYO(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_11_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_11(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_11_KANRYO(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_12_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_12(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_12_KANRYO(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_16_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_16(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_16_KANRYO(),
            },
        },
        {
            'case_name': 'MCOPY_TICKET_OTO_KEKKA_99_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_OTO_KEKKA_99(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_MCOPY_TICKET_OTO_KEKKA_99_KANRYO(),
            },
        },
    ]

# ---------------------------
# Mcopyチケット マッピングNo2 EC関連払戻 テストデータ
# ---------------------------
def get_reqres_ecticket_repay():
    return [
        {
            'case_name': 'TICKET_REPAY_CASE_01',
            'req': { 
                **DEFAULT_DICT_EC_REPAY(),
                'bar_code_no': BARCODE_TICKET_REPAY_CASE_01(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_CASE_01(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_CASE_01_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_REPAY_CANCEL(),
                'bar_code_no': BARCODE_TICKET_REPAY_CASE_01(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_CASE_01_CANCEL(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_CASE_02',
            'req': { 
                **DEFAULT_DICT_EC_REPAY(),
                'bar_code_no': BARCODE_TICKET_REPAY_CASE_02(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_CASE_02(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_CASE_02_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_REPAY_CANCEL(),
                'bar_code_no': BARCODE_TICKET_REPAY_CASE_02(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_CASE_02_CANCEL(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_CASE_02_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_EC_REPAY_CANCEL(),
                'bar_code_no': BARCODE_TICKET_REPAY_CASE_02(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_CASE_02_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_CASE_03',
            'req': { 
                **DEFAULT_DICT_EC_REPAY(),
                'bar_code_no': BARCODE_TICKET_REPAY_CASE_03(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_CASE_03(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_CASE_03_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_REPAY_CANCEL(),
                'bar_code_no': BARCODE_TICKET_REPAY_CASE_03(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_CASE_03_CANCEL(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_CASE_03_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_EC_REPAY_CANCEL(),
                'bar_code_no': BARCODE_TICKET_REPAY_CASE_03(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_CASE_03_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_CASE_04',
            'req': { 
                **DEFAULT_DICT_EC_REPAY(),
                'bar_code_no': BARCODE_TICKET_REPAY_CASE_04(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_CASE_04(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_CASE_04_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_REPAY_CANCEL(),
                'bar_code_no': BARCODE_TICKET_REPAY_CASE_04(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_CASE_04_CANCEL(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_CASE_04_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_EC_REPAY_CANCEL(),
                'bar_code_no': BARCODE_TICKET_REPAY_CASE_04(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_CASE_04_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_CASE_05',
            'req': { 
                **DEFAULT_DICT_EC_REPAY(),
                'bar_code_no': BARCODE_TICKET_REPAY_CASE_05(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_CASE_05(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_CASE_05_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_REPAY_CANCEL(),
                'bar_code_no': BARCODE_TICKET_REPAY_CASE_05(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_CASE_05_CANCEL(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_SYORI_KEKKA_14',
            'req': { 
                **DEFAULT_DICT_EC_REPAY(),
                'bar_code_no': BARCODE_TICKET_REPAY_SYORI_KEKKA_14(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_SYORI_KEKKA_14(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_SYORI_KEKKA_14_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_REPAY_CANCEL(),
                'bar_code_no': BARCODE_TICKET_REPAY_SYORI_KEKKA_14(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_SYORI_KEKKA_14_CANCEL(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_SYORI_KEKKA_14_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_EC_REPAY_CANCEL(),
                'bar_code_no': BARCODE_TICKET_REPAY_SYORI_KEKKA_14(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_SYORI_KEKKA_14_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_SYORI_KEKKA_99_400',
            'req': { 
                **DEFAULT_DICT_EC_REPAY(),
                'bar_code_no': BARCODE_TICKET_REPAY_SYORI_KEKKA_99_400(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_SYORI_KEKKA_99_400(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_SYORI_KEKKA_99_400_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_REPAY_CANCEL(),
                'bar_code_no': BARCODE_TICKET_REPAY_SYORI_KEKKA_99_400(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_SYORI_KEKKA_99_400_CANCEL(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_SYORI_KEKKA_99_400_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_EC_REPAY_CANCEL(),
                'bar_code_no': BARCODE_TICKET_REPAY_SYORI_KEKKA_99_400(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_SYORI_KEKKA_99_400_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_SYORI_KEKKA_99_500',
            'req': { 
                **DEFAULT_DICT_EC_REPAY(),
                'bar_code_no': BARCODE_TICKET_REPAY_SYORI_KEKKA_99_500(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_SYORI_KEKKA_99_500(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_SYORI_KEKKA_99_500_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_REPAY_CANCEL(),
                'bar_code_no': BARCODE_TICKET_REPAY_SYORI_KEKKA_99_500(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_SYORI_KEKKA_99_500_CANCEL(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_SYORI_KEKKA_99_500_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_EC_REPAY_CANCEL(),
                'bar_code_no': BARCODE_TICKET_REPAY_SYORI_KEKKA_99_500(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_SYORI_KEKKA_99_500_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_OTO_KEKKA_01',
            'req': { 
                **DEFAULT_DICT_EC_REPAY(),
                'bar_code_no': BARCODE_TICKET_REPAY_OTO_KEKKA_01(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_01(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_OTO_KEKKA_01_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_REPAY_CANCEL(),
                'bar_code_no': BARCODE_TICKET_REPAY_OTO_KEKKA_01(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_01_CANCEL(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_OTO_KEKKA_01_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_EC_REPAY_CANCEL(),
                'bar_code_no': BARCODE_TICKET_REPAY_OTO_KEKKA_01(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_01_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_OTO_KEKKA_05',
            'req': { 
                **DEFAULT_DICT_EC_REPAY(),
                'bar_code_no': BARCODE_TICKET_REPAY_OTO_KEKKA_05(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_05(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_OTO_KEKKA_05_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_REPAY_CANCEL(),
                'bar_code_no': BARCODE_TICKET_REPAY_OTO_KEKKA_05(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_05_CANCEL(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_OTO_KEKKA_05_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_EC_REPAY_CANCEL(),
                'bar_code_no': BARCODE_TICKET_REPAY_OTO_KEKKA_05(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_05_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_OTO_KEKKA_11',
            'req': { 
                **DEFAULT_DICT_EC_REPAY(),
                'bar_code_no': BARCODE_TICKET_REPAY_OTO_KEKKA_11(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_11(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_OTO_KEKKA_11_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_REPAY_CANCEL(),
                'bar_code_no': BARCODE_TICKET_REPAY_OTO_KEKKA_11(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_11_CANCEL(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_OTO_KEKKA_11_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_EC_REPAY_CANCEL(),
                'bar_code_no': BARCODE_TICKET_REPAY_OTO_KEKKA_11(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_11_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_OTO_KEKKA_51',
            'req': { 
                **DEFAULT_DICT_EC_REPAY(),
                'bar_code_no': BARCODE_TICKET_REPAY_OTO_KEKKA_51(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_51(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_OTO_KEKKA_51_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_REPAY_CANCEL(),
                'bar_code_no': BARCODE_TICKET_REPAY_OTO_KEKKA_51(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_51_CANCEL(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_OTO_KEKKA_51_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_EC_REPAY_CANCEL(),
                'bar_code_no': BARCODE_TICKET_REPAY_OTO_KEKKA_51(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_51_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_OTO_KEKKA_52',
            'req': { 
                **DEFAULT_DICT_EC_REPAY(),
                'bar_code_no': BARCODE_TICKET_REPAY_OTO_KEKKA_52(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_52(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_OTO_KEKKA_52_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_REPAY_CANCEL(),
                'bar_code_no': BARCODE_TICKET_REPAY_OTO_KEKKA_52(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_52_CANCEL(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_OTO_KEKKA_52_CANCEL_RETRY',
            'req': { 
                **DEFAULT_DICT_EC_REPAY_CANCEL(),
                'bar_code_no': BARCODE_TICKET_REPAY_OTO_KEKKA_52(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_52_CANCEL_RETRY(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_OTO_KEKKA_53',
            'req': { 
                **DEFAULT_DICT_EC_REPAY(),
                'bar_code_no': BARCODE_TICKET_REPAY_OTO_KEKKA_53(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_53(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_OTO_KEKKA_53_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_REPAY_CANCEL(),
                'bar_code_no': BARCODE_TICKET_REPAY_OTO_KEKKA_53(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_53_CANCEL(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_OTO_KEKKA_55',
            'req': { 
                **DEFAULT_DICT_EC_REPAY(),
                'bar_code_no': BARCODE_TICKET_REPAY_OTO_KEKKA_55(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_55(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_OTO_KEKKA_55_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_REPAY_CANCEL(),
                'bar_code_no': BARCODE_TICKET_REPAY_OTO_KEKKA_55(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_55_CANCEL(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_OTO_KEKKA_99',
            'req': { 
                **DEFAULT_DICT_EC_REPAY(),
                'bar_code_no': BARCODE_TICKET_REPAY_OTO_KEKKA_99(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_99(),
            },
        },
        {
            'case_name': 'TICKET_REPAY_OTO_KEKKA_99_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_REPAY_CANCEL(),
                'bar_code_no': BARCODE_TICKET_REPAY_OTO_KEKKA_99(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_TICKET_REPAY_OTO_KEKKA_99_CANCEL(),
            },
        },
    ]


# ---------------------------
# Mcopyチケット マッピングNo3 EC関連問合せ テストデータ
# ---------------------------
def get_reqres_ecticket_map3():
    return [
        {
            'case_name': 'EC_KANRYO_CASE_01_REQUEST',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_CASE_01(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_CASE_01_REQUEST(),
            },
        },
        {
            'case_name': 'EC_KANRYO_CASE_01_REQUEST_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_CASE_01(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_CASE_01_REQUEST(),
            },
        },
        {
            'case_name': 'EC_KANRYO_CASE_02_REQUEST',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_CASE_02(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_CASE_02_REQUEST(),
            },
        },
        {
            'case_name': 'EC_KANRYO_CASE_02_REQUEST_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_CASE_02(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_CASE_02_REQUEST(),
            },
        },
        {
            'case_name': 'EC_KANRYO_CASE_03_REQUEST',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_CASE_03(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_CASE_03_REQUEST(),
            },
        },
        {
            'case_name': 'EC_KANRYO_CASE_03_REQUEST_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_CASE_03(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_CASE_03_REQUEST(),
            },
        },
        {
            'case_name': 'EC_KANRYO_SYORI_KEKKA_10_REQUEST',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_SYORI_KEKKA_10(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_10_REQUEST(),
            },
        },
        {
            'case_name': 'EC_KANRYO_SYORI_KEKKA_10_REQUEST_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_SYORI_KEKKA_10(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_10_REQUEST(),
            },
        },
        {
            'case_name': 'EC_KANRYO_SYORI_KEKKA_11_REQUEST',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_SYORI_KEKKA_11(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_11_REQUEST(),
            },
        },
        {
            'case_name': 'EC_KANRYO_SYORI_KEKKA_11_REQUEST_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_SYORI_KEKKA_11(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_11_REQUEST(),
            },
        },
        {
            'case_name': 'EC_KANRYO_SYORI_KEKKA_14_REQUEST',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_SYORI_KEKKA_14(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_14_REQUEST(),
            },
        },
        {
            'case_name': 'EC_KANRYO_SYORI_KEKKA_14_REQUEST_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_SYORI_KEKKA_14(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_14_REQUEST(),
            },
        },
        {
            'case_name': 'EC_KANRYO_SYORI_KEKKA_99_400_REQUEST',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_SYORI_KEKKA_99_400(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_99_400_REQUEST(),
            },
        },
        {
            'case_name': 'EC_KANRYO_SYORI_KEKKA_99_400_REQUEST_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_SYORI_KEKKA_99_400(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_99_400_REQUEST(),
            },
        },
        {
            'case_name': 'EC_KANRYO_SYORI_KEKKA_99_500_REQUEST',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_SYORI_KEKKA_99_500(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_99_500_REQUEST(),
            },
        },
        {
            'case_name': 'EC_KANRYO_SYORI_KEKKA_99_500_REQUEST_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_SYORI_KEKKA_99_500(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_99_500_REQUEST(),
            },
        },
        {
            'case_name': 'EC_KANRYO_SYORI_KEKKA_TIMEOUT_REQUEST',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_SYORI_KEKKA_TIMEOUT(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_TIMEOUT_REQUEST(),
            },
        },
        {
            'case_name': 'EC_KANRYO_SYORI_KEKKA_TIMEOUT_REQUEST_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_SYORI_KEKKA_TIMEOUT(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_TIMEOUT_REQUEST(),
            },
        },
        {
            'case_name': 'EC_KANRYO_SYORI_KEKKA_TIMEOUT_99_REQUEST',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_SYORI_KEKKA_TIMEOUT_99(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_TIMEOUT_99_REQUEST(),
            },
        },
        {
            'case_name': 'EC_KANRYO_SYORI_KEKKA_TIMEOUT_99_REQUEST_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_SYORI_KEKKA_TIMEOUT_99(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_TIMEOUT_99_REQUEST(),
            },
        },
        {
            'case_name': 'EC_KANRYO_OTO_KEKKA_01_REQUEST',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_OTO_KEKKA_01(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_OTO_KEKKA_01_REQUEST(),
            },
        },
        {
            'case_name': 'EC_KANRYO_OTO_KEKKA_01_REQUEST_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_OTO_KEKKA_01(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_OTO_KEKKA_01_REQUEST(),
            },
        },
        {
            'case_name': 'EC_KANRYO_OTO_KEKKA_99_REQUEST',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_OTO_KEKKA_99(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_OTO_KEKKA_99_REQUEST(),
            },
        },
        {
            'case_name': 'EC_KANRYO_OTO_KEKKA_99_REQUEST_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_OTO_KEKKA_99(),
                'retry_flg': '1',
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_OTO_KEKKA_99_REQUEST(),
            },
        },
    ]


# ---------------------------
# Mcopyチケット マッピングNo3 EC関連完了 テストデータ
# ---------------------------
def get_reqres_ecticket_kanryo_map3():
    return [
        {
            'case_name': 'EC_KANRYO_CASE_01',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_CASE_01(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_CASE_01(),
            },
        },
        {
            'case_name': 'EC_KANRYO_CASE_02',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_CASE_02(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_CASE_02(),
            },
        },
        {
            'case_name': 'EC_KANRYO_CASE_03',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_CASE_03(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_CASE_03(),
            },
        },
        {
            'case_name': 'EC_KANRYO_SYORI_KEKKA_10',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_SYORI_KEKKA_10(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_10(),
            },
        },
        {
            'case_name': 'EC_KANRYO_SYORI_KEKKA_11',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_SYORI_KEKKA_11(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_11(),
            },
        },
        {
            'case_name': 'EC_KANRYO_SYORI_KEKKA_14',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_SYORI_KEKKA_14(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_14(),
            },
        },
        {
            'case_name': 'EC_KANRYO_SYORI_KEKKA_99_400',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_SYORI_KEKKA_99_400(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_99_400(),
            },
        },
        {
            'case_name': 'EC_KANRYO_SYORI_KEKKA_99_500',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_SYORI_KEKKA_99_500(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_99_500(),
            },
        },
        {
            'case_name': 'EC_KANRYO_SYORI_KEKKA_TIMEOUT',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_SYORI_KEKKA_TIMEOUT(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_TIMEOUT(),
            },
        },
        {
            'case_name': 'EC_KANRYO_SYORI_KEKKA_TIMEOUT_99',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_SYORI_KEKKA_TIMEOUT_99(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_SYORI_KEKKA_TIMEOUT_99(),
            },
        },
        {
            'case_name': 'EC_KANRYO_OTO_KEKKA_01',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_OTO_KEKKA_01(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_OTO_KEKKA_01(),
            },
        },
        {
            'case_name': 'EC_KANRYO_OTO_KEKKA_99',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_EC_KANRYO_OTO_KEKKA_99(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_KANRYO_OTO_KEKKA_99(),
            },
        },
    ]


# ---------------------------
# Mcopyチケット マッピングNo4 EC関連問合せ テストデータ
# ---------------------------
def get_reqres_ecticket_map4():
    return [
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_01',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_01(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_01(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_01_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC_CANCEL(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_01(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_01_CANCEL(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_02',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_02(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_02(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_02_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_02(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_02(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_03',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_03(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_03(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_03_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_03(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_03(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_04',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_04(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_04(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_04_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_04(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_04(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_05',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_05(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_05(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_05_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_05(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_05(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_06',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_06(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_06(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_06_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_06(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_06(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_07',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_07(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_07(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_07_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_07(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_07(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_08',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_08(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_08(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_08_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_08(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_08(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_09',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_09(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_09(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_09_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_09(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_09(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_10',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_10(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_10(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_10_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_10(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_10(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_11',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_11(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_11(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_11_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_11(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_11(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_12',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_12(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_12(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_12_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_12(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_12(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_13',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_13(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_13(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_13_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_13(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_13(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_14',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_14(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_14(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_14_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_14(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_14(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_15',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_15(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_15(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_15_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_15(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_15(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_16',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_16(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_16(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_16_CANCEL',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_16(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_16(),
            },
        },
    ]


# ---------------------------
# Mcopyチケット マッピングNo4 EC関連完了 テストデータ
# ---------------------------
def get_reqres_ecticket_kanryo_map4():
    return [
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_01_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_01(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_01_KANRYO(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_02_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_02(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_02_KANRYO(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_03_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_03(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_03_KANRYO(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_04_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_04(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_04_KANRYO(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_05_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_05(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_05_KANRYO(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_06_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_06(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_06_KANRYO(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_07_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_07(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_07_KANRYO(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_08_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_08(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_08_KANRYO(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_09_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_09(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_09_KANRYO(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_10_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_10(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_10_KANRYO(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_11_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_11(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_11_KANRYO(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_12_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_12(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_12_KANRYO(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_13_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_13(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_13_KANRYO(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_14_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_14(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_14_KANRYO(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_15_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_15(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_15_KANRYO(),
            },
        },
        {
            'case_name': 'EC_TICKET_DETAIL_CASE_16_KANRYO',
            'req': { 
                **DEFAULT_DICT_EC_KANRYO(),
                'kensaku_key': KESSAI_KEY_EC_TICKET_DETAIL_CASE_16(),
            },
            'res': { 
                **RESPONSE_TICKET_DATA_EC_TICKET_DETAIL_CASE_16_KANRYO(),
            },
        },
    ]


# ---------------------------
# Mcopyチケット 異常系 テストデータ
# ---------------------------
def get_reqres_ecticket_error():
    return [
        {
            # 要求区分なし
            'case_name': 'ERROR_MCOPY_YOKYU_KBN_NONE',
            'req': { 
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_01(),
            },
            'res': { 
                **RESPONSE_SHORI_KEKKA_99(),
            },
        },
        {
            # 検索キーなし
            'case_name': 'ERROR_MCOPY_KENSAKU_KEY_NONE',
            'req': { 
                **DEFAULT_DICT_EC(),
            },
            'res': { 
                **RESPONSE_SHORI_KEKKA_99(),
            },
        },
        {
            # 検索キーなし
            'case_name': 'ERROR_MCOPY_KENSAKU_KEY_EMPTY',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': '',
            },
            'res': { 
                **RESPONSE_SHORI_KEKKA_99(),
            },
        },
        {
            # 検索キーなし
            'case_name': 'ERROR_MCOPY_REPAY_KENSAKU_KEY_NONE',
            'req': { 
                **DEFAULT_DICT_EC_REPAY(),
            },
            'res': { 
                **RESPONSE_SHORI_KEKKA_99(),
            },
        },
        {
            # 検索キーなし
            'case_name': 'ERROR_MCOPY_REPAY_KENSAKU_KEY_EMPTY',
            'req': { 
                **DEFAULT_DICT_EC_REPAY(),
                'bar_code_no': '',
            },
            'res': { 
                **RESPONSE_SHORI_KEKKA_99(),
            },
        },
        {
            # 電文区分不正
            'case_name': 'ERROR_MCOPY_DENBUN_KUBUN',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_01(),
		        'denbun_kubun': '21',
            },
            'res': { 
                **RESPONSE_SHORI_KEKKA_10(),
            },
        },
        {
            # 業務区分不正
            'case_name': 'ERROR_MCOPY_GYOMU_KUBUN',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_01(),
		        'gyomu_kubun': '0066',
            },
            'res': { 
                **RESPONSE_SHORI_KEKKA_11(),
            },
        },
        {
            # 要求区分不正
            'case_name': 'ERROR_MCOPY_YOKYU_KUBUN',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_01(),
		        'yokyu_kubun': 'Z',
            },
            'res': { 
                **RESPONSE_SHORI_KEKKA_99(),
            },
        },
        {
            # 要求区分不正
            'case_name': 'ERROR_MCOPY_REPAY_YOKYU_KUBUN',
            'req': { 
                **DEFAULT_DICT_EC_REPAY(),
                'bar_code_no': BARCODE_TICKET_REPAY_CASE_03(),
		        'yokyu_kubun': 'Z',
            },
            'res': { 
                **RESPONSE_SHORI_KEKKA_99(),
            },
        },
        {
            # 問合せ完了区分不正
            'case_name': 'ERROR_MCOPY_TOIAWASE_KANRYO_KUBUN',
            'req': { 
                **DEFAULT_DICT_EC(),
                'kensaku_key': KESSAI_KEY_MCOPY_TICKET_CASE_01(),
		        'toiawase_kanryo_kubun': '3',
            },
            'res': { 
                **RESPONSE_SHORI_KEKKA_99(),
            },
        },
        {
            # 問合せ完了区分不正
            'case_name': 'ERROR_MCOPY_REPAY_TOIAWASE_KANRYO_KUBUN',
            'req': { 
                **DEFAULT_DICT_EC_REPAY(),
                'bar_code_no': BARCODE_TICKET_REPAY_CASE_03(),
		        'toiawase_kanryo_kubun': '3',
            },
            'res': { 
                **RESPONSE_SHORI_KEKKA_99(),
            },
        },
    ]