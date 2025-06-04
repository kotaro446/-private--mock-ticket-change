import html
from logger import get_logger
logger = get_logger()

def in_ticket_output_xml(
        req:dict,
        common_dict:dict,
        success_dict:dict,
        ticket_list:list,
        ) -> str:
    """
    xml形式のレスポンスデータ本文を返す
    """
    res:str
    # 処理結果が異常のケース
    if (common_dict["X_shori_kekka"] != "00"):
        res = f"""<?xml version="1.0" encoding="Shift_JIS"?>
<sejmsg xmlns="http://regifront.sej.co.jp/">
	<body>
        <X_shori_kekka>{common_dict["X_shori_kekka"]}</X_shori_kekka>
    </body>
</sejmsg>"""
    # 入金/発券完了
    elif (req["X_yokyu_kbn"] == "02" or
          req["X_yokyu_kbn"] == "12"):
        res = f"""<?xml version="1.0" encoding="Shift_JIS"?>
<sejmsg xmlns="http://regifront.sej.co.jp/">
	<body>
        <X_shori_kekka>{common_dict["X_shori_kekka"]}</X_shori_kekka>
        <X_gyomu_kbn>{common_dict["X_gyomu_kbn"]}</X_gyomu_kbn>
        <X_kigyo_id>{common_dict["X_kigyo_id"]}</X_kigyo_id>
        <X_mise_no>{common_dict["X_mise_no"]}</X_mise_no>
        <X_regi_no>{common_dict["X_regi_no"]}</X_regi_no>
        <X_hakken_regi_no>{common_dict["X_hakken_regi_no"]}</X_hakken_regi_no>
        <X_regi_date_min>{common_dict["X_regi_date_min"]}</X_regi_date_min>
        <X_shori_tuban>{common_dict["X_shori_tuban"]}</X_shori_tuban>
        <X_saiso_kbn>{common_dict["X_saiso_kbn"]}</X_saiso_kbn>
        <X_yokyu_kbn>{common_dict["X_yokyu_kbn"]}</X_yokyu_kbn>
        <X_barcode>{common_dict["X_barcode"]}</X_barcode>
        <X_cvs_code>{common_dict["X_cvs_code"]}</X_cvs_code>
        <X_shop_id>{common_dict["X_shop_id"]}</X_shop_id>
        <X_order_id>{common_dict["X_order_id"]}</X_order_id>
        <X_nyuukin>{common_dict["X_nyuukin"]}</X_nyuukin>
        <X_kaishu_cnt>{common_dict["X_kaishu_cnt"]}</X_kaishu_cnt>
        <X_outou_kekka_kbn>{common_dict["X_outou_kekka_kbn"]}</X_outou_kekka_kbn>
        <X_outou_kekka>{common_dict["X_outou_kekka"]}</X_outou_kekka>
    </body>
</sejmsg>"""
    # 登録と取消は、チケットがあるか無いかの差
    else:
        res = f"""<?xml version="1.0" encoding="Shift_JIS"?>
<sejmsg xmlns="http://regifront.sej.co.jp/">
	<body>
        <X_shori_kekka>{common_dict["X_shori_kekka"]}</X_shori_kekka>
        <X_gyomu_kbn>{common_dict["X_gyomu_kbn"]}</X_gyomu_kbn>
        <X_kigyo_id>{common_dict["X_kigyo_id"]}</X_kigyo_id>
        <X_mise_no>{common_dict["X_mise_no"]}</X_mise_no>
        <X_regi_no>{common_dict["X_regi_no"]}</X_regi_no>
        <X_hakken_regi_no>{common_dict["X_hakken_regi_no"]}</X_hakken_regi_no>
        <X_regi_date_min>{common_dict["X_regi_date_min"]}</X_regi_date_min>
        <X_shori_tuban>{common_dict["X_shori_tuban"]}</X_shori_tuban>
        <X_saiso_kbn>{common_dict["X_saiso_kbn"]}</X_saiso_kbn>
        <X_yokyu_kbn>{common_dict["X_yokyu_kbn"]}</X_yokyu_kbn>
        <X_barcode>{common_dict["X_barcode"]}</X_barcode>
        <X_cvs_code>{common_dict["X_cvs_code"]}</X_cvs_code>
        <X_shop_id>{common_dict["X_shop_id"]}</X_shop_id>
        <X_order_id>{common_dict["X_order_id"]}</X_order_id>
        <X_torikeshi_riyu>{common_dict["X_torikeshi_riyu"]}</X_torikeshi_riyu>
        <X_kaishu_cnt>{common_dict["X_kaishu_cnt"]}</X_kaishu_cnt>
        <X_outou_kekka_kbn>{common_dict["X_outou_kekka_kbn"]}</X_outou_kekka_kbn>
        <X_outou_kekka>{common_dict["X_outou_kekka"]}</X_outou_kekka>
        <shop_namek>{success_dict["shop_namek"]}</shop_namek>
        <X_renraku_saki>{success_dict["X_renraku_saki"]}</X_renraku_saki>
        <X_haraikomi>{success_dict["X_haraikomi"]}</X_haraikomi>
        <X_haraikomi_org>{success_dict["X_haraikomi_org"]}</X_haraikomi_org>
        <X_hikikae>{success_dict["X_hikikae"]}</X_hikikae>
        <X_hikikae_org>{success_dict["X_hikikae_org"]}</X_hikikae_org>
        <X_hakken_mise_date>{success_dict["X_hakken_mise_date"]}</X_hakken_mise_date>
        <X_hakken_lmt>{success_dict["X_hakken_lmt"]}</X_hakken_lmt>
        <X_goukei>{success_dict["X_goukei"]}</X_goukei>
        <X_tc_dai>{success_dict["X_tc_dai"]}</X_tc_dai>
        <X_tc_kounyu_dai>{success_dict["X_tc_kounyu_dai"]}</X_tc_kounyu_dai>
        <X_hakken_dai>{success_dict["X_hakken_dai"]}</X_hakken_dai>
        <X_inshi_kijun>{success_dict["X_inshi_kijun"]}</X_inshi_kijun>
        <namek>{success_dict["namek"]}</namek>
        <name_kana>{success_dict["name_kana"]}</name_kana>
        <X_tel>{success_dict["X_tel"]}</X_tel>
        <X_post>{success_dict["X_post"]}</X_post>
        <X_mail>{success_dict["X_mail"]}</X_mail>
        <X_ticket_hon_cnt>{success_dict["X_ticket_hon_cnt"]}</X_ticket_hon_cnt>
        <X_ticket_cnt>{success_dict["X_ticket_cnt"]}</X_ticket_cnt>
        <X_hansoku_jan_code>{success_dict["X_hansoku_jan_code"]}</X_hansoku_jan_code>"""
        # 要求区分が01(登録)の場合、チケットリストを出す
        if req["X_yokyu_kbn"] == "01":
            for i in range(len(ticket_list)):
                res += f"""
        <tc_info no="{i + 1}">
            <X_tc_barcode_no>{ticket_list[i][0]}</X_tc_barcode_no>
            <X_tc_kbn>{ticket_list[i][1]}</X_tc_kbn>
            <X_tc_template>{ticket_list[i][2]}</X_tc_template>
            <tc_text>{html.escape(ticket_list[i][3], quote=True)}</tc_text>
        </tc_info>"""
        res += f"""
    </body>
</sejmsg>"""
    return res

