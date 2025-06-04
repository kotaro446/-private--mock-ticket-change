from flask import Flask, request, Response

from logger import get_logger
from recorder import save_request, save_response
from ec_ticket import mock_ecticket_ms_main
from in_ticket import mock_inticket_ms_main
from toto_ticket import mock_toto_register_ms_main

app = Flask(__name__)

logger = get_logger()
logger.setup_logger(app)

# 例外時エラーレスポンス定義
xml_response_err = """<?xml version="1.0" encoding="Windows-31J"?>
<sejmsg xmlns="http://sej.co.jp/">
<response>
    <interface_info>
         <shori_kekka>99</shori_kekka>
    </interface_info>
</response>
</sejmsg>
"""

# NRIセンターEC関連問合わせ モックサーバ  - 発券・取消、払戻し、完了通知
@app.route('/inkessai/recvrequest.do', methods=['POST'])
def mock_ecticket_ms() -> Response:
    logger.debug(f"リクエストを受信 request: {request}")

    # リクエストデータを保存
    logger.debug("リクエストを保存")
    save_request(request)

    # リクエストデータを取得
    req = request.form.to_dict()
    logger.debug(f"リクエストデータ: {req}")

    try:
        # メイン関数を呼出、レスポンスを返却する
        res = mock_ecticket_ms_main(req)

        # レスポンスデータを保存
        logger.debug("レスポンスデータを保存")
        save_response(request, str(res.get_data().decode("cp932")))
        logger.debug(f"レスポンスデータ: {res.response}")
        return res
    except Exception as e:
        logger.debug(f"Exception: {e}")
        logger.debug(f"レスポンスデータ: {xml_response_err}")
        return Response(xml_response_err.encode(encoding='cp932'), status = 500, content_type='text/xml; charset=Windows-31J')  



#　インターネットチケット モックサーバ - 入金/発券問合せ, 入金/発券完了通知
@app.route('/register/recvrequest.do', methods=['POST'])
def mock_inticket_ms():
    logger.debug(f"リクエストを受信 request: {request}")

    # リクエストデータを保存
    logger.debug("リクエストを保存")
    save_request(request)

    # リクエストデータを取得
    req = request.form.to_dict()
    logger.debug(f"リクエストデータ: {req}")

    try:
        # メイン関数を呼出、レスポンスを返却する
        res = mock_inticket_ms_main(req)

        # レスポンスデータを保存
        logger.debug("レスポンスデータを保存")
        save_response(request, str(res.get_data().decode("cp932")))
        logger.debug(f"レスポンスデータ: {res.response}")
        return res
    except Exception as e:
        logger.debug(f"Exception: {e}")
        logger.debug(f"レスポンスデータ: {xml_response_err}")
        return Response(xml_response_err.encode(encoding='Shift_JIS'), status=400, content_type='text/xml; charset=Shift_JIS')


#　totoくじ モックサーバ
@app.route('/toto_register/recvrequest.do', methods=['POST'])
def mock_toto_register_ms():
    logger.debug(f"リクエストを受信 request: {request}")

    # リクエストデータを保存
    logger.debug("リクエストを保存")
    save_request(request)

    # リクエストデータを取得
    req = request.form.to_dict()
    logger.debug(f"リクエストデータ: {req}")

    try:
        # メイン関数を呼出、レスポンスを返却する
        res = mock_toto_register_ms_main(req, logger)

        # レスポンスデータを保存
        logger.debug("レスポンスデータを保存")
        save_response(request, str(res.get_data().decode("cp932")))
        logger.debug(f"レスポンスデータ: {res.response}")
        return res
    except Exception as e:
        logger.debug(f"Exception: {e}")
        logger.debug(f"レスポンスデータ: {xml_response_err}")
        return Response(xml_response_err.encode(encoding='cp932'), status = 500, content_type='text/xml; charset=Windows-31J')


if __name__ == '__main__':
    app.run()