from logger import get_logger
logger = get_logger()

def ec_ticket_output_xml(
        request_data:dict,
        interface_info:dict,
        order_info:dict,
        ticket_info:dict,
        payback_info:dict
        ) -> str:
    """
    xml形式のレスポンスデータ本文を返す
    """
    res:str
    # 処理結果が異常のケース
    if (interface_info["syori_kekka"] != "00"):
        res = f"""<?xml version="1.0" encoding="Windows-31J"?>
<sejmsg xmlns="http://sej.co.jp/">
<response>
    <interface_info>
        <syori_kekka>{interface_info["syori_kekka"]}</syori_kekka>
    </interface_info>
</response>
</sejmsg>"""
    elif (request_data["toiawase_kanryo_kubun"] == "1"):
        # チケット払戻のケース
        if (request_data["yokyu_kubun"] in {"E", "L"}):
            res = f"""<?xml version="1.0" encoding="Windows-31J"?>
<sejmsg xmlns="http://sej.co.jp/">
<response>
    <interface_info>
        <denbun_kubun>{interface_info["denbun_kubun"]}</denbun_kubun>
        <syori_kekka>{interface_info["syori_kekka"]}</syori_kekka>
        <gyomu_kubun>{interface_info["gyomu_kubun"]}</gyomu_kubun>
        <kigyo_id>{interface_info["kigyo_id"]}</kigyo_id>
        <mise_no>{interface_info["mise_no"]}</mise_no>
        <tuban>{interface_info["tuban"]}</tuban>
        <regi_no>{interface_info["regi_no"]}</regi_no>
        <ticket_regi_no>{interface_info["ticket_regi_no"]}</ticket_regi_no>
        <riyo_time_ymdhms>{interface_info["riyo_time_ymdhms"]}</riyo_time_ymdhms>
        <syori_tuban>{interface_info["syori_tuban"]}</syori_tuban>
        <retry_flg>{interface_info["retry_flg"]}</retry_flg>
        <yokyu_kubun>{interface_info["yokyu_kubun"]}</yokyu_kubun>
        <toiawase_kanryo_kubun>{interface_info["toiawase_kanryo_kubun"]}</toiawase_kanryo_kubun>
    </interface_info>
    <payback_info>
        <kessai_id>{payback_info["kessai_id"]}</kessai_id>
        <bar_code_no>{payback_info["bar_code_no"]}</bar_code_no>
        <oto_kekka>{payback_info["oto_kekka"]}</oto_kekka>
        <tenpo_bango>{payback_info["tenpo_bango"]}</tenpo_bango>
        <mise_namek>{payback_info["mise_namek"]}</mise_namek>
        <mise_address>{payback_info["mise_address"]}</mise_address>
        <tenpo_tel_no>{payback_info["tenpo_tel_no"]}</tenpo_tel_no>
        <haraikomi_no>{payback_info["haraikomi_no"]}</haraikomi_no>
        <shop_id>{payback_info["shop_id"]}</shop_id>
        <payback_kingaku>{payback_info["payback_kingaku"]}</payback_kingaku>
        <shop_namek>{payback_info["shop_namek"]}</shop_namek>
        <user_namek>{payback_info["user_namek"]}</user_namek>
        <renraku_saki>{payback_info["renraku_saki"]}</renraku_saki>
        <payback_start_ymd>{payback_info["payback_start_ymd"]}</payback_start_ymd>
        <payback_end_ymd>{payback_info["payback_end_ymd"]}</payback_end_ymd>
        <svc_time_start_hm>{payback_info["svc_time_start_hm"]}</svc_time_start_hm>
        <svc_time_end_hm>{payback_info["svc_time_end_hm"]}</svc_time_end_hm>
        <kogyo_name>{payback_info["kogyo_name"]}</kogyo_name>
        <koen_date_ymd>{payback_info["koen_date_ymd"]}</koen_date_ymd>
        <hanken_yohi>{payback_info["hanken_yohi"]}</hanken_yohi>
        <fuka_riyu>{payback_info["fuka_riyu"]}</fuka_riyu>
        <payback_tesuryo>{payback_info["payback_tesuryo"]}</payback_tesuryo>
    </payback_info>
</response>
</sejmsg>"""
        # チケット発券のケース
        else:
            res = f"""<?xml version="1.0" encoding="Windows-31J"?>
<sejmsg xmlns="http://sej.co.jp/">
<response>
    <interface_info>
        <denbun_kubun>{interface_info["denbun_kubun"]}</denbun_kubun>
        <syori_kekka>{interface_info["syori_kekka"]}</syori_kekka>
        <gyomu_kubun>{interface_info["gyomu_kubun"]}</gyomu_kubun>
        <kigyo_id>{interface_info["kigyo_id"]}</kigyo_id>
        <mise_no>{interface_info["mise_no"]}</mise_no>
        <tuban>{interface_info["tuban"]}</tuban>
        <regi_no>{interface_info["regi_no"]}</regi_no>
        <ticket_regi_no>{interface_info["ticket_regi_no"]}</ticket_regi_no>
        <order_type>{interface_info["order_type"]}</order_type>
        <syohin_info_kbn>{interface_info["syohin_info_kbn"]}</syohin_info_kbn>
        <riyo_time_ymdhms>{interface_info["riyo_time_ymdhms"]}</riyo_time_ymdhms>
        <syori_tuban>{interface_info["syori_tuban"]}</syori_tuban>
        <retry_flg>{interface_info["retry_flg"]}</retry_flg>
        <yokyu_kubun>{interface_info["yokyu_kubun"]}</yokyu_kubun>
        <toiawase_kanryo_kubun>{interface_info["toiawase_kanryo_kubun"]}</toiawase_kanryo_kubun>
    </interface_info>
    <order_info>
        <kensaku_key>{order_info["kensaku_key"]}</kensaku_key>
        <bar_code_no>{order_info["bar_code_no"]}</bar_code_no>
        <oto_kekka>{order_info["oto_kekka"]}</oto_kekka>
        <pay_type>{order_info["pay_type"]}</pay_type>
        <dlv_type>{order_info["dlv_type"]}</dlv_type>
        <tenpo_bango>{order_info["tenpo_bango"]}</tenpo_bango>
        <mise_namek>{order_info["mise_namek"]}</mise_namek>
        <mise_address>{order_info["mise_address"]}</mise_address>
        <tenpo_tel_no>{order_info["tenpo_tel_no"]}</tenpo_tel_no>
        <keijyo_type>{order_info["keijyo_type"]}</keijyo_type>
        <inshi_kijun>{order_info["inshi_kijun"]}</inshi_kijun>
        <kingaku_henko_flg>{order_info["kingaku_henko_flg"]}</kingaku_henko_flg>
        <kino_kbn>{order_info["kino_kbn"]}</kino_kbn>
        <haraikomi_no>{order_info["haraikomi_no"]}</haraikomi_no>
        <shop_id>{order_info["shop_id"]}</shop_id>
        <shuno_kingaku>{order_info["shuno_kingaku"]}</shuno_kingaku>
        <shohin_daikin>{order_info["shohin_daikin"]}</shohin_daikin>
        <shop_namek>{order_info["shop_namek"]}</shop_namek>
        <user_namek>{order_info["user_namek"]}</user_namek>
        <renraku_saki>{order_info["renraku_saki"]}</renraku_saki>
    </order_info>
    <ticket_info>"""
            max_index = int(len(ticket_info) / 3)
            logger.debug(f"max_index={max_index}")
            for i in range(max_index):
                key1 = "html_name" + str(i + 1)
                key2 = "barcode" + str(i + 1)
                key3 = "ticket_data" + str(i + 1)
                res += f"""<{key1}>{ticket_info[key1]}</{key1}>
        <{key2}>{ticket_info[key2]}</{key2}>
        <{key3}>{ticket_info[key3]}</{key3}>"""
            res += f"""</ticket_info>
</response>
</sejmsg>
"""
    else:
        res = f"""<?xml version="1.0" encoding="Windows-31J"?>
<sejmsg xmlns="http://sej.co.jp/">
<response>
    <interface_info>
        <denbun_kubun>{interface_info["denbun_kubun"]}</denbun_kubun>
        <syori_kekka>{interface_info["syori_kekka"]}</syori_kekka>
        <gyomu_kubun>{interface_info["gyomu_kubun"]}</gyomu_kubun>
        <kigyo_id>{interface_info["kigyo_id"]}</kigyo_id>
        <mise_no>{interface_info["mise_no"]}</mise_no>
        <tuban>{interface_info["tuban"]}</tuban>
        <regi_no>{interface_info["regi_no"]}</regi_no>
        <ticket_regi_no>{interface_info["ticket_regi_no"]}</ticket_regi_no>
        <kanryo_tuchi_kubun>{interface_info["kanryo_tuchi_kubun"]}</kanryo_tuchi_kubun>
        <shiharai_hoho_kbn>{interface_info["shiharai_hoho_kbn"]}</shiharai_hoho_kbn>
        <riyo_time_ymdhms>{interface_info["riyo_time_ymdhms"]}</riyo_time_ymdhms>
        <syori_tuban>{interface_info["syori_tuban"]}</syori_tuban>
        <retry_flg>{interface_info["retry_flg"]}</retry_flg>
        <yokyu_kubun>{interface_info["yokyu_kubun"]}</yokyu_kubun>
        <toiawase_kanryo_kubun>{interface_info["toiawase_kanryo_kubun"]}</toiawase_kanryo_kubun>
    </interface_info>
    <order_info>
        <kensaku_key>{order_info["kensaku_key"]}</kensaku_key>
        <bar_code_no>{order_info["bar_code_no"]}</bar_code_no>
        <cvs_code>{order_info["cvs_code"]}</cvs_code>
        <kino_kbn>{order_info["kino_kbn"]}</kino_kbn>
        <shop_id>{order_info["shop_id"]}</shop_id>
        <shuno_kingaku>{order_info["shuno_kingaku"]}</shuno_kingaku>
        <otoKekka_kubun>{order_info["otoKekka_kubun"]}</otoKekka_kubun>
        <oto_kekka>{order_info["oto_kekka"]}</oto_kekka>
    </order_info>
</response>
</sejmsg>"""
    return res
