# リクエストパラメータ必須項目
VALIDATE_REQUEST_FIELDS_COMMON = ["X_yokyu_kbn", "X_barcode"]

VALIDATE_REQUEST_FIELDS_PURCHASE = ["X_kigyo_id", "X_mise_no", "X_regi_no", "X_hakken_regi_no", 
                                    "X_regi_date_min", "X_shori_tuban", "X_saiso_kbn"]

VALIDATE_REQUEST_FIELDS_CANCEL = ["X_kigyo_id", "X_mise_no", "X_regi_no", "X_hakken_regi_no",
                                  "X_regi_date_min", "X_shori_tuban", "X_saiso_kbn", "X_torikeshi_riyu"]

VALIDATE_REQUEST_FIELDS_VOTE = ["X_kigyo_id", "X_mise_no", "X_regi_no", "X_hakken_regi_no",
                                "X_regi_date_min", "X_shori_tuban", "X_toto_terminal_id", 
                                "X_toto_terminal_kbn", "X_toto_julian_date", "X_toto_julian_time", 
                                "X_toto_soukan_id"]

VALIDATE_REQUEST_FIELDS_VOTE_CANCEL = ["X_kigyo_id", "X_mise_no", "X_regi_no", "X_hakken_regi_no",
                                       "X_regi_date_min", "X_shori_tuban", "X_torikeshi_riyu", 
                                       "X_toto_terminal_id", "X_toto_terminal_kbn", "X_toto_julian_date", 
                                       "X_toto_julian_time", "X_toto_soukan_id", "X_torikeshi_riyu_kbn"]

VALIDATE_REQUEST_FIELDS_REFUND = ["X_kigyo_id", "X_mise_no", "X_regi_no", "X_regi_date_min", 
                                  "X_shori_tuban", "X_saiso_kbn", "X_vote_ticket_barcode"]

VALIDATE_REQUEST_FIELDS_REFUND_CANCEL = ["X_kigyo_id", "X_mise_no", "X_regi_no", "X_regi_date_min", 
                                  "X_shori_tuban", "X_saiso_kbn", "X_vote_ticket_barcode", "X_torikeshi_riyu"]

VALIDATE_REQUEST_FIELDS_CLEARING = ["X_kigyo_id", "X_mise_no", "X_regi_no", "X_regi_date_min", 
                                    "X_shori_tuban", "X_vote_ticket_barcode", "X_toto_terminal_id", 
                                    "X_toto_terminal_kbn", "X_toto_julian_date", "X_toto_julian_time", 
                                    "X_pos_trade_no", "X_payback_flg"]

# タイムアウト秒
TIMEOUT_SEC = 30
