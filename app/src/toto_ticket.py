import html
import os
import random
import time
import xml.etree.ElementTree as ET
import toto_constant
from flask import request, Response
from logger import Logger
from toto_response_purchase import resp_purchase
from toto_response_purchase_cancel import resp_purchase_cancel
from toto_response_vote import resp_vote
from toto_response_vote_cancel import resp_vote_cancel
from toto_response_refund import resp_refund
from toto_response_refund_cancel import resp_refund_cancel
from toto_response_clearing import resp_clearing
from toto_library import *

#　totoくじ チケットのモックサーバ
#　メイン関数
def mock_toto_register_ms_main(req:dict, logger:Logger)  ->  Response:
    
    # 必須項目チェック（要求区分、バーコード情報）
    if validate_request_fields(req, toto_constant.VALIDATE_REQUEST_FIELDS_COMMON):
        return generate_error_response()

    # バーコード番号からマッピング番号を取得する
    mapping_num = split_bits(req["X_barcode"][2:12], [
        31,  #[0]  No Care
        2,   #[1]  マッピング番号
    ])

    # マッピング番号ごとのマッピングルールに従い、レスポンス設定を取得する
    segments = process_mapping_code_segmentation(req["X_barcode"][2:12], mapping_num[1])

    # 要求区分ごとのレスポンスを生成する
    create_resp_handler_mapping = {
        "01": resp_purchase,        # totoくじ - 購入要求
        "11": resp_purchase_cancel, # totoくじ - 購入取消要求
        "02": resp_vote,            # totoくじ - 本投票要求
        "12": resp_vote_cancel,     # totoくじ - 本投票障害取消要求
        "03": resp_refund,          # totoくじ - 払戻要求
        "13": resp_refund_cancel,   # totoくじ - 払戻取消要求
        "04": resp_clearing,        # totoくじ - 当せん返還消込要求
    }
    create_resp_handler = create_resp_handler_mapping.get(req["X_yokyu_kbn"])
    if create_resp_handler is None:
        return generate_error_response()
    return create_resp_handler(req, segments, mapping_num[1])
