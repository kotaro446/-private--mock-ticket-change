# Ticket External API Mock Server

## run app

```bash
cd app/
pipenv run dev
```

## run lint

```bash
cd app/
pipenv install --dev
pipenv run lint
```

## test

```bash
（１）EC関連問合せ外部APIモック
    モック設定詳細は「チケット_EC関連問合せ外部API_モックサーバレスポンス設定.xlsx」を参照

    CURLコマンドサンプル：
        ・EC関連問合せ（発券）：
        curl --location --request POST "http://127.0.0.1:5000/inkessai/recvrequest.do" --header "Content-Type: application/x-www-form-urlencoded" --data "denbun_kubun=20&gyomu_kubun=0067&syori_kekka=00&kigyo_id=07&mise_no=123456&tuban=SQ&regi_no=1&ticket_regi_no=%20&riyo_time_ymdhms=20241113171523&syori_tuban=20241113000&retry_flg=0&yokyu_kubun=A&toiawase_kanryo_kubun=1&shop_id=00767&torikeshi_riyu=01&bar_code_no=2024112700011&kensaku_key=00000566272&cvs_code=8037110000004&order_type=%20&syohin_info_kbn=%20&item_pointer=01"

        ・EC関連問合せ（発券取消）：
        curl --location --request POST "http://127.0.0.1:5000/inkessai/recvrequest.do" --header "Content-Type: application/x-www-form-urlencoded" --data "denbun_kubun=20&gyomu_kubun=0067&syori_kekka=00&kigyo_id=07&mise_no=123456&tuban=SQ&regi_no=1&ticket_regi_no=%20&riyo_time_ymdhms=20241113171523&syori_tuban=20241113000&retry_flg=0&yokyu_kubun=B&toiawase_kanryo_kubun=1&shop_id=00767&torikeshi_riyu=01&bar_code_no=2024112700011&kensaku_key=00000566272&cvs_code=8037110000004&order_type=%20&syohin_info_kbn=%20&item_pointer=01"

        ・EC関連問合せ（払戻し）：
        curl --location --request POST "http://127.0.0.1:5000/inkessai/recvrequest.do" --header "Content-Type: application/x-www-form-urlencoded" --data "denbun_kubun=20&gyomu_kubun=0067&syori_kekka=00&kigyo_id=07&mise_no=123456&tuban=SQ&regi_no=1&ticket_regi_no=%20&riyo_time_ymdhms=20241113171523&syori_tuban=20241113000&retry_flg=0&yokyu_kubun=E&toiawase_kanryo_kubun=1&shop_id=00767&torikeshi_riyu=01&bar_code_no=8000000663054"

        ・EC関連問合せ（払戻し取消）：
        curl --location --request POST "http://127.0.0.1:5000/inkessai/recvrequest.do" --header "Content-Type: application/x-www-form-urlencoded" --data "denbun_kubun=20&gyomu_kubun=0067&syori_kekka=00&kigyo_id=07&mise_no=123456&tuban=SQ&regi_no=1&ticket_regi_no=%20&riyo_time_ymdhms=20241113171523&syori_tuban=20241113000&retry_flg=0&yokyu_kubun=L&toiawase_kanryo_kubun=1&shop_id=00767&torikeshi_riyu=01&bar_code_no=8000000663054"

        ・EC関連問合せ（完了）：
        curl --location --request POST "http://127.0.0.1:5000/inkessai/recvrequest.do" --header "Content-Type: application/x-www-form-urlencoded" --data "denbun_kubun=20&gyomu_kubun=0067&syori_kekka=00&kigyo_id=07&mise_no=123456&tuban=SQ&regi_no=1&ticket_regi_no=1&riyo_time_ymdhms=20241113171523&syori_tuban=20241113000&retry_flg=0&yokyu_kubun=A&toiawase_kanryo_kubun=2&shop_id=00767&torikeshi_riyu=01&bar_code_no=8000001308411&kanryo_tuchi_kubun=1&shiharai_hoho_kbn=2&kensaku_key=00024107026&cvs_code=8037110000004&kino_kbn=3&shuno_kingaku=001000&otoKekka_kubun=00&oto_kekka=00"


（２）INチケット外部APIモック
    モック設定詳細は「インターネットチケット外部API_モックサーバレスポンス設定.xlsx」を参照

    CURLコマンドサンプル：
        ・インターネットチケット対応 - 入金/発券：
        curl --location --request POST "http://127.0.0.1:5000/register/recvrequest.do" --header "Content-Type: application/x-www-form-urlencoded; charset=Windows-31J" --data "X_gyomu_kbn=0060&X_kigyo_id=07&X_mise_no=123456&X_regi_no=1&X_hakken_regi_no=1&X_regi_date_min=20241118001111&X_saiso_kbn=0&X_yokyu_kbn=01&X_barcode=2100000000005&X_cvs_code=03711&X_torikeshi_riyu=01&X_kaishu_cnt=01&X_shori_tuban=20241118001&X_shori_kekka=00"

        ・インターネットチケット対応 - 入金/発券取消：
        curl --location --request POST "http://127.0.0.1:5000/register/recvrequest.do" --header "Content-Type: application/x-www-form-urlencoded; charset=Windows-31J" --data "X_gyomu_kbn=0060&X_kigyo_id=07&X_mise_no=123456&X_regi_no=1&X_hakken_regi_no=1&X_regi_date_min=20241118001111&X_saiso_kbn=0&X_yokyu_kbn=21&X_barcode=2100000000005&X_cvs_code=03711&X_shop_id=01&X_order_id=01&X_torikeshi_riyu=01&X_kaishu_cnt=01&X_shori_tuban=20241118001&X_shori_kekka=00"

        ・インターネットチケット対応 - 入金/発券完了通知(入金／発券完了通知（代引き、前払い（後日発券）、代済発券、前払いのみ）)：
        curl --location --request POST "http://127.0.0.1:5000/register/recvrequest.do" --header "Content-Type: application/x-www-form-urlencoded; charset=Windows-31J" --data "X_gyomu_kbn=0060&X_kigyo_id=07&X_mise_no=123456&X_regi_no=1&X_hakken_regi_no=1&X_regi_date_min=20241118001111&X_saiso_kbn=0&X_yokyu_kbn=02&X_barcode=2100000000005&X_cvs_code=03711&X_shop_id=12345&X_order_id=213356098564&X_shori_tuban=20241118001&X_nyuukin=1234&X_shori_kekka=00"

        ・インターネットチケット対応 - 入金/発券完了通知(再発行完了通知（代引き、代済発券）)：
        curl --location --request POST "http://127.0.0.1:5000/register/recvrequest.do" --header "Content-Type: application/x-www-form-urlencoded; charset=Windows-31J" --data "X_gyomu_kbn=0060&X_kigyo_id=07&X_mise_no=234234&X_regi_no=9&X_hakken_regi_no=9&X_regi_date_min=20250214150928&X_saiso_kbn=0&X_yokyu_kbn=12&X_barcode=2100000000005&X_cvs_code=03711&X_shop_id=30400&X_order_id=201100012581&X_shori_tuban=20250214010&X_nyuukin=1234&X_shori_kekka=00&X_kaishu_cnt=01"



（３）totoくじチケット外部APIモック
    モック設定詳細は「totoくじ外部API_モックサーバレスポンス設定.xlsx」を参照

    CURLコマンドサンプル：
        ・totoくじ購入要求：
        curl --location --request POST "http://127.0.0.1:5000/toto_register/recvrequest.do" --header "Content-Type: application/x-www-form-urlencoded" --data "X_shori_kekka=00&X_kigyo_id=07&X_mise_no=123456&X_regi_no=1&X_regi_date_min=20241119094500&X_shori_tuban=20241119123&X_yokyu_kbn=01&X_barcode=4000000163848&X_hakken_regi_no=1&X_saiso_kbn=0"

        ・totoくじ購入取消要求：
        curl --location --request POST "http://127.0.0.1:5000/toto_register/recvrequest.do" --header "Content-Type: application/x-www-form-urlencoded" --data "X_shori_kekka=00&X_kigyo_id=07&X_mise_no=123456&X_regi_no=1&X_hakken_regi_no=1&X_regi_date_min=20241119094500&X_shori_tuban=20241119123&X_saiso_kbn=0&X_yokyu_kbn=11&X_barcode=4000000163848&X_torikeshi_riyu=01"

        ・totoくじ本投票要求：
        curl --location --request POST "http://127.0.0.1:5000/toto_register/recvrequest.do" --header "Content-Type: application/x-www-form-urlencoded" --data "X_shori_kekka=00&X_kigyo_id=07&X_mise_no=123456&X_regi_no=1&X_hakken_regi_no=1&X_regi_date_min=20241119094500&X_shori_tuban=20241119123&X_yokyu_kbn=02&X_barcode=4005368709134&X_toto_terminal_id=1&X_toto_terminal_kbn=X&X_toto_julian_date=366&X_toto_julian_time=86399&X_toto_soukan_id=0902abc09080bef1234"

        ・totoくじ本投票障害取消要求：
        curl --location --request POST "http://127.0.0.1:5000/toto_register/recvrequest.do" --header "Content-Type: application/x-www-form-urlencoded" --data "X_shori_kekka=00&X_kigyo_id=07&X_mise_no=123456&X_regi_no=1&X_hakken_regi_no=1&X_regi_date_min=20241119094500&X_shori_tuban=20241119123&X_yokyu_kbn=12&X_barcode=4005368709134&X_toto_terminal_id=1&X_toto_terminal_kbn=X&X_toto_julian_date=366&X_toto_julian_time=86399&X_torikeshi_riyu=01&X_toto_soukan_id=0902abc09080bef1234&X_torikeshi_riyu_kbn=02"

        ・totoくじ払戻要求：
        curl --location --request POST "http://127.0.0.1:5000/toto_register/recvrequest.do" --header "Content-Type: application/x-www-form-urlencoded" --data "X_shori_kekka=00&X_kigyo_id=07&X_mise_no=123456&X_regi_no=1&X_regi_date_min=20241119094500&X_shori_tuban=20241119123&X_saiso_kbn=0&X_yokyu_kbn=03&X_barcode=9000000328068&X_vote_ticket_barcode=0987654321321"

        ・totoくじ払戻取消要求：
        curl --location --request POST "http://127.0.0.1:5000/toto_register/recvrequest.do" --header "Content-Type: application/x-www-form-urlencoded" --data "X_shori_kekka=00&X_kigyo_id=07&X_mise_no=123456&X_regi_no=1&X_regi_date_min=20241119094500&X_shori_tuban=20241119123&X_saiso_kbn=0&X_yokyu_kbn=13&X_barcode=9000000328068&X_vote_ticket_barcode=0987654321321&X_torikeshi_riyu=01"

        ・totoくじ当せん返還消込要求：
        curl --location --request POST "http://127.0.0.1:5000/toto_register/recvrequest.do" --header "Content-Type: application/x-www-form-urlencoded" --data "X_shori_kekka=00&X_kigyo_id=07&X_mise_no=123456&X_regi_no=1&X_regi_date_min=20241119094500&X_shori_tuban=20241119123&X_yokyu_kbn=04&X_barcode=9000000020511&X_toto_terminal_id=1&X_toto_terminal_kbn=X&X_toto_julian_date=366&X_toto_julian_time=86399&X_pos_trade_no=1&X_payback_flg=01&X_vote_ticket_barcode=0987654321321"

```