import pytest
import sys
import os
from unittest.mock import patch, MagicMock, Mock

# テスト対象モジュールのパスを追加
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app', 'src'))

# logger, in_const, ticket_library のモック設定（インポート前に設定）
logger_mock = MagicMock()
logger_mock.debug = MagicMock()
logger_mock.error = MagicMock()
logger_mock.setup_logger = MagicMock()

# モジュールのモック化
sys.modules['logger'] = MagicMock()
sys.modules['logger'].get_logger.return_value = logger_mock
sys.modules['in_const'] = MagicMock()
sys.modules['in_const'].TIMEOUT_SEC = 5
sys.modules['ticket_library'] = MagicMock()

# ticket_library関数のモック
ticket_library_mock = MagicMock()
ticket_library_mock.req_res_map = lambda mapping, index, default: mapping.get(index, default)
ticket_library_mock.split_bits = lambda s, sizes: [0] * len(sizes)  # 簡単な実装
ticket_library_mock.calculate_CD = lambda x: "0"
sys.modules['ticket_library'] = ticket_library_mock

from ec_ticket import make_ticket_info
from ec_ticket_library import get_order_details_dictionary
from ec_ticket_nomal import get_ec_nomal_field
from ec_ticket_complete import get_ec_complete_field
from ec_ticket_kenmen import get_ec_kenmen_field
from ec_ticket_xmldef import ec_ticket_output_xml


class TestOrderDetailsImplementation:
    """
    要求区分B,H,J時のorder_details対応のリグレッションテスト
    """
    
    def setup_method(self):
        """各テストメソッド実行前のセットアップ"""
        # 基本的なリクエストデータ
        self.base_request_data = {
            "denbun_kubun": "20",
            "gyomu_kubun": "0067",
            "syori_kekka": "00",
            "kigyo_id": "07",
            "mise_no": "123456",
            "tuban": "SQ",
            "regi_no": "1",
            "ticket_regi_no": " ",
            "riyo_time_ymdhms": "20241113171523",
            "syori_tuban": "20241113000",
            "retry_flg": "0",
            "toiawase_kanryo_kubun": "1",
            "shop_id": "00767",
            "torikeshi_riyu": "01",
            "bar_code_no": "2024112700011",
            "kensaku_key": "00000566272",
            "cvs_code": "8037110000004",
            "order_type": " ",
            "syohin_info_kbn": " ",
            "item_pointer": "01"
        }
        
        # 期待されるorder_details辞書（仕様書に基づく）
        self.expected_order_details = {
            "regi_msg_code": "     ",
            "dlv_mise_date_yotei_ymd": "        ",
            "dlv_mise_time_yotei_hm": "    ",
            "nohin_setumei_kbn": "  ",
            "dlv_ymd": "        ",
            "sej_shohin_code": "000000",
            "site_nai_shiharai_kingaku": "000000",
            "oisogi_flg": " ",
            "oisogi_fee": "000000",
            "other_fee": "000000",
            "tax_kbn": " ",
            "tax_ritsu": "000",
            "oisogi_delay_flg": " ",
            "tyumon_no": "              ",
            "site_kensu": "0",
            "site_utiwake1": "    ",
            "site_name1": "                      ",
            "site_price1": "000000",
            "site_crekbn1": " ",
            "site_utiwake2": "    ",
            "site_name2": "                      ",
            "site_price2": "000000",
            "site_crekbn2": " ",
            "site_utiwake3": "    ",
            "site_name3": "                      ",
            "site_price3": "000000",
            "site_crekbn3": " ",
            "site_utiwake4": "    ",
            "site_name4": "                      ",
            "site_price4": "000000",
            "site_crekbn4": " ",
            "shohin_daikin_hyojun": "      ",
            "shohin_daikin_keigen": "      ",
            "sej_shohin_code_hyojun": "      ",
            "sej_shohin_code_keigen": "      ",
            "tax_kbn_hyojun": " ",
            "tax_kbn_keigen": " ",
            "tax_ritsu_hyojun": "   ",
            "tax_ritsu_keigen": "   ",
            "category_name_hyojun": "                      ",
            "category_name_keigen": "                      ",
            "kana_simei": "                                                  ",
            "shouken_num": "          ",
            "kanyu_type": "                        ",
            "hoken_siki": "          ",
            "hoken_shuki": "          ",
            "hoken_shuryou_bi": "                ",
            "hoken_nissu": "00",
            "shohin_daikin_hikazei": "      ",
            "sej_shohin_code_hikazei": "      ",
            "tax_kbn_hikazei": " ",
            "category_name_hikazei": "                      ",
            "shohin_nebiki_kingaku_hyojun": "      ",
            "shohin_nebiki_kingaku_keigen": "      ",
            "shohin_nebiki_kingaku_hikazei": "      ",
            "tax_kbn_hosoryo_takuhairyo": " ",
            "shohin_daikin_hosoryo": "      ",
            "sej_shohin_code_hosoryo": "      ",
            "nebiki_kingaku_hosoryo": "      ",
            "shohin_daikin_takuhairyo": "      ",
            "sej_shohin_code_takuhairyo": "      ",
            "nebiki_kingaku_takuhairyo": "      ",
            "sake_kbn": " ",
            "ondotai_kbn": " ",
            "tento_mae_kingaku": "      ",
            "zan_item_umu": "0",
        }

    def test_get_order_details_dictionary_for_bhj_requests(self):
        """
        要求区分B,H,Jの場合にorder_details辞書が正しく生成されることをテスト
        """
        for yokyu_kubun in ["B", "H", "J"]:
            request_data = {**self.base_request_data, "yokyu_kubun": yokyu_kubun}
            
            # テスト実行
            result = get_order_details_dictionary(request_data)
            
            # 期待値と比較
            assert result == self.expected_order_details, f"要求区分{yokyu_kubun}のorder_details生成が期待値と異なります"

    def test_get_order_details_dictionary_for_non_bhj_requests(self):
        """
        要求区分がB,H,J以外の場合に空の辞書が返されることをテスト
        """
        for yokyu_kubun in ["A", "E", "L"]:
            request_data = {**self.base_request_data, "yokyu_kubun": yokyu_kubun}
            
            # テスト実行
            result = get_order_details_dictionary(request_data)
            
            # 空の辞書が返されることを確認
            assert result == {}, f"要求区分{yokyu_kubun}で空辞書が返されませんでした"

    def test_ec_nomal_field_includes_order_details_for_bhj(self):
        """
        ec_ticket_nomal.pyで要求区分B,H,Jの場合にorder_detailsが含まれることをテスト
        """
        for yokyu_kubun in ["B", "H", "J"]:
            request_data = {**self.base_request_data, "yokyu_kubun": yokyu_kubun}
            mapping_str = "00000566272"  # テスト用マッピング文字列
            
            # テスト実行
            interface_info, order_info, ticket_info, order_details, httpstatus = get_ec_nomal_field(request_data, mapping_str)
            
            # order_detailsが期待値と一致することを確認
            assert order_details == self.expected_order_details, f"要求区分{yokyu_kubun}でorder_detailsが期待値と異なります"

    def test_ec_nomal_field_excludes_order_details_for_non_bhj(self):
        """
        ec_ticket_nomal.pyで要求区分がB,H,J以外の場合にorder_detailsが空であることをテスト
        """
        request_data = {**self.base_request_data, "yokyu_kubun": "A"}
        mapping_str = "00000566272"
        
        # テスト実行
        interface_info, order_info, ticket_info, order_details, httpstatus = get_ec_nomal_field(request_data, mapping_str)
        
        # order_detailsが空であることを確認
        assert order_details == {}, "要求区分Aでorder_detailsが空ではありません"

    def test_ec_complete_field_includes_order_details_for_bhj(self):
        """
        ec_ticket_complete.pyで要求区分B,H,Jの場合にorder_detailsが含まれることをテスト
        """
        for yokyu_kubun in ["B", "H", "J"]:
            request_data = {**self.base_request_data, "yokyu_kubun": yokyu_kubun}
            mapping_str = "00000566272"
            
            # テスト実行
            interface_info, order_info, ticket_info, order_details, httpstatus = get_ec_complete_field(request_data, mapping_str)
            
            # order_detailsが期待値と一致することを確認
            assert order_details == self.expected_order_details, f"要求区分{yokyu_kubun}でorder_detailsが期待値と異なります"

    def test_ec_kenmen_field_includes_order_details_for_bhj(self):
        """
        ec_ticket_kenmen.pyで要求区分B,H,Jの場合にorder_detailsが含まれることをテスト
        """
        for yokyu_kubun in ["B", "H", "J"]:
            request_data = {**self.base_request_data, "yokyu_kubun": yokyu_kubun}
            mapping_str = "00000566272"
            
            # テスト実行
            interface_info, order_info, ticket_info, order_details, httpstatus = get_ec_kenmen_field(request_data, mapping_str)
            
            # order_detailsが期待値と一致することを確認
            assert order_details == self.expected_order_details, f"要求区分{yokyu_kubun}でorder_detailsが期待値と異なります"

    def test_xml_output_contains_order_details_for_bhj(self):
        """
        XML出力で要求区分B,H,Jの場合にorder_detailsセクションが含まれることをテスト
        """
        # テスト用データの準備
        request_data = {**self.base_request_data, "yokyu_kubun": "B", "toiawase_kanryo_kubun": "1"}
        interface_info = {
            "denbun_kubun": "22",
            "syori_kekka": "00",
            "gyomu_kubun": "0067",
            "kigyo_id": "07",
            "mise_no": "123456",
            "tuban": "SQ",
            "regi_no": "1",
            "ticket_regi_no": " ",
            "order_type": " ",
            "syohin_info_kbn": " ",
            "riyo_time_ymdhms": "20241113171523",
            "syori_tuban": "20241113000",
            "retry_flg": "0",
            "yokyu_kubun": "B",
            "toiawase_kanryo_kubun": "1"
        }
        order_info = {
            "kensaku_key": "00000566272",
            "bar_code_no": "             ",
            "oto_kekka": "00",
            "pay_type": "1",
            "dlv_type": "1",
            "tenpo_bango": "123456",
            "mise_namek": "○○店舗                            ",
            "mise_address": "住所（漢字）                                    ",
            "tenpo_tel_no": "029-298-0203",
            "keijyo_type": " ",
            "inshi_kijun": "      ",
            "kingaku_henko_flg": " ",
            "kino_kbn": "3",
            "haraikomi_no": "600000566272X",
            "shop_id": "00000",
            "shuno_kingaku": "      ",
            "shohin_daikin": "000000",
            "shop_namek": "ショップ名                                        ",
            "user_namek": "お客様名                      ",
            "renraku_saki": "ショップ連絡先                                                  "
        }
        ticket_info = {}
        payback_info = {}
        order_details = self.expected_order_details
        
        # テスト実行
        result_xml = ec_ticket_output_xml(request_data, interface_info, order_info, ticket_info, payback_info, order_details)
        
        # XMLにorder_detailsセクションが含まれることを確認
        assert "<order_details>" in result_xml, "XMLにorder_detailsセクションが含まれていません"
        assert "</order_details>" in result_xml, "XMLのorder_detailsセクションが正しく閉じられていません"
        
        # 主要なorder_detailsフィールドがXMLに含まれることを確認（一部をチェック）
        key_fields = ["regi_msg_code", "sej_shohin_code", "site_kensu", "zan_item_umu"]
        for key in key_fields:
            value = order_details[key]
            expected_tag = f"<{key}>{value}</{key}>"
            assert expected_tag in result_xml, f"XMLに{key}タグが正しく含まれていません"

    def test_xml_output_excludes_order_details_for_non_bhj(self):
        """
        XML出力で要求区分がB,H,J以外の場合にorder_detailsセクションが含まれないことをテスト
        """
        # テスト用データの準備（要求区分A）
        request_data = {**self.base_request_data, "yokyu_kubun": "A", "toiawase_kanryo_kubun": "1"}
        interface_info = {
            "denbun_kubun": "22",
            "syori_kekka": "00",
            "gyomu_kubun": "0067",
            "kigyo_id": "07",
            "mise_no": "123456",
            "tuban": "SQ",
            "regi_no": "1",
            "ticket_regi_no": " ",
            "order_type": " ",
            "syohin_info_kbn": " ",
            "riyo_time_ymdhms": "20241113171523",
            "syori_tuban": "20241113000",
            "retry_flg": "0",
            "yokyu_kubun": "A",
            "toiawase_kanryo_kubun": "1"
        }
        order_info = {
            "kensaku_key": "00000566272",
            "bar_code_no": "             ",
            "oto_kekka": "00",
            "pay_type": "1",
            "dlv_type": "1",
            "tenpo_bango": "123456",
            "mise_namek": "○○店舗                            ",
            "mise_address": "住所（漢字）                                    ",
            "tenpo_tel_no": "029-298-0203",
            "keijyo_type": " ",
            "inshi_kijun": "      ",
            "kingaku_henko_flg": " ",
            "kino_kbn": "3",
            "haraikomi_no": "600000566272X",
            "shop_id": "00000",
            "shuno_kingaku": "      ",
            "shohin_daikin": "000000",
            "shop_namek": "ショップ名                                        ",
            "user_namek": "お客様名                      ",
            "renraku_saki": "ショップ連絡先                                                  "
        }
        ticket_info = {}
        payback_info = {}
        order_details = {}  # 空の辞書
        
        # テスト実行
        result_xml = ec_ticket_output_xml(request_data, interface_info, order_info, ticket_info, payback_info, order_details)
        
        # XMLにorder_detailsセクションが含まれないことを確認
        assert "<order_details>" not in result_xml, "XMLにorder_detailsセクションが含まれています（要求区分A）"

    @patch('ec_ticket.get_test_option')
    def test_make_ticket_info_integration_for_bhj(self, mock_get_test_option):
        """
        make_ticket_info関数でのorder_details統合テスト（要求区分B,H,J）
        """
        # モックの設定
        mock_get_test_option.return_value = (0, "00000566272")  # No.1マッピング
        
        for yokyu_kubun in ["B", "H", "J"]:
            request_data = {**self.base_request_data, "yokyu_kubun": yokyu_kubun}
            
            # テスト実行
            interface_info, order_info, ticket_info, payback_info, order_details, httpstatus = make_ticket_info(request_data)
            
            # order_detailsが期待値と一致することを確認
            assert order_details == self.expected_order_details, f"要求区分{yokyu_kubun}の統合テストでorder_detailsが期待値と異なります"
            # HTTPステータスが正常であることを確認
            assert httpstatus == 200, f"要求区分{yokyu_kubun}でHTTPステータスが200ではありません"


class TestActualBehaviorValidation:
    """
    実際の実装動作の検証テスト
    """
    
    def setup_method(self):
        """セットアップ"""
        self.base_request_data = {
            "denbun_kubun": "20",
            "gyomu_kubun": "0067",
            "syori_kekka": "00",
            "kigyo_id": "07",
            "mise_no": "123456",
            "tuban": "SQ",
            "regi_no": "1",
            "ticket_regi_no": " ",
            "riyo_time_ymdhms": "20241113171523",
            "syori_tuban": "20241113000",
            "retry_flg": "0",
            "toiawase_kanryo_kubun": "1",
            "shop_id": "00767",
            "torikeshi_riyu": "01",
            "bar_code_no": "2024112700011",
            "kensaku_key": "00000566272",
            "cvs_code": "8037110000004",
            "order_type": " ",
            "syohin_info_kbn": " ",
            "item_pointer": "01"
        }

    def test_order_details_dictionary_behavior_validation(self):
        """
        get_order_details_dictionary関数の実際の動作を検証
        実装では要求区分B,H,Jの場合は常にorder_detailsを返す
        """
        # 要求区分B,H,Jの場合：辞書が返される
        for yokyu_kubun in ["B", "H", "J"]:
            request_data = {**self.base_request_data, "yokyu_kubun": yokyu_kubun}
            result = get_order_details_dictionary(request_data)
            
            # 辞書が返されることを確認
            assert isinstance(result, dict), f"要求区分{yokyu_kubun}で辞書が返されませんでした"
            # 空でない辞書が返されることを確認
            assert len(result) > 0, f"要求区分{yokyu_kubun}で空でない辞書が返されませんでした"
            # 特定のキーが含まれることを確認
            expected_keys = ["regi_msg_code", "sej_shohin_code", "site_kensu", "zan_item_umu"]
            for key in expected_keys:
                assert key in result, f"要求区分{yokyu_kubun}でキー'{key}'が見つかりません"
        
        # 要求区分A,E,Lの場合：空辞書が返される
        for yokyu_kubun in ["A", "E", "L"]:
            request_data = {**self.base_request_data, "yokyu_kubun": yokyu_kubun}
            result = get_order_details_dictionary(request_data)
            
            assert result == {}, f"要求区分{yokyu_kubun}で空辞書が返されませんでした"

    def test_order_details_field_values_validation(self):
        """
        order_detailsの各フィールド値が仕様通りであることを検証
        """
        request_data = {**self.base_request_data, "yokyu_kubun": "B"}
        result = get_order_details_dictionary(request_data)
        
        # 重要なフィールドの値をチェック
        field_validations = {
            "regi_msg_code": "     ",  # 5文字の空白
            "dlv_mise_date_yotei_ymd": "        ",  # 8文字の空白
            "dlv_mise_time_yotei_hm": "    ",  # 4文字の空白
            "nohin_setumei_kbn": "  ",  # 2文字の空白
            "sej_shohin_code": "000000",  # 6桁のゼロ
            "site_kensu": "0",  # 1文字のゼロ
            "hoken_nissu": "00",  # 2桁のゼロ
            "zan_item_umu": "0",  # 1文字のゼロ
        }
        
        for field, expected_value in field_validations.items():
            assert result[field] == expected_value, f"フィールド'{field}'の値が期待値'{expected_value}'と異なります: {result[field]}"

    def test_xml_generation_with_order_details(self):
        """
        order_detailsを含むXML生成の動作確認
        """
        # 要求区分Bのorder_detailsを取得
        request_data = {**self.base_request_data, "yokyu_kubun": "B", "toiawase_kanryo_kubun": "1"}
        order_details = get_order_details_dictionary(request_data)
        
        # XML生成用の最小限のデータを準備
        interface_info = {
            "denbun_kubun": "22", "syori_kekka": "00", "gyomu_kubun": "0067",
            "kigyo_id": "07", "mise_no": "123456", "tuban": "SQ", "regi_no": "1",
            "ticket_regi_no": " ", "order_type": " ", "syohin_info_kbn": " ",
            "riyo_time_ymdhms": "20241113171523", "syori_tuban": "20241113000",
            "retry_flg": "0", "yokyu_kubun": "B", "toiawase_kanryo_kubun": "1"
        }
        
        order_info = {
            "kensaku_key": "00000566272", "bar_code_no": "             ",
            "oto_kekka": "00", "pay_type": "1", "dlv_type": "1",
            "tenpo_bango": "123456", "mise_namek": "テスト店舗                            ",
            "mise_address": "テスト住所                                    ",
            "tenpo_tel_no": "029-298-0203", "keijyo_type": " ", "inshi_kijun": "      ",
            "kingaku_henko_flg": " ", "kino_kbn": "3", "haraikomi_no": "600000566272X",
            "shop_id": "00000", "shuno_kingaku": "      ", "shohin_daikin": "000000",
            "shop_namek": "テストショップ                                        ",
            "user_namek": "テストユーザー                      ",
            "renraku_saki": "テスト連絡先                                                  "
        }
        
        # XML生成テスト
        result_xml = ec_ticket_output_xml(request_data, interface_info, order_info, {}, {}, order_details)
        
        # 基本構造の確認
        assert "<?xml version=" in result_xml, "XML宣言が含まれていません"
        assert "<sejmsg xmlns=" in result_xml, "ルート要素が正しくありません"
        assert "<order_details>" in result_xml, "order_detailsセクションが含まれていません"
        assert "</order_details>" in result_xml, "order_detailsセクションが正しく閉じられていません"
        
        # 必須フィールドがXMLに含まれていることを確認
        required_fields = ["regi_msg_code", "sej_shohin_code", "site_kensu"]
        for field in required_fields:
            assert f"<{field}>" in result_xml, f"必須フィールド'{field}'がXMLに含まれていません"


class TestErrorHandling:
    """
    エラーハンドリングのテスト（実装の実際の動作に基づく）
    """
    
    def test_request_data_without_yokyu_kubun(self):
        """
        yokyu_kubunが含まれていないリクエストデータの処理
        実装では KeyError が発生するため、これを確認する
        """
        # yokyu_kubunが含まれていないリクエストデータ
        request_data_without_yokyu = {
            "denbun_kubun": "20",
            "gyomu_kubun": "0067",
            # yokyu_kubunが欠如
        }
        
        # テスト実行（KeyError が発生することを確認）
        with pytest.raises(KeyError, match="yokyu_kubun"):
            result = get_order_details_dictionary(request_data_without_yokyu)

    def test_minimal_request_data_for_bhj(self):
        """
        最小限のリクエストデータでB,H,J処理が動作することを確認
        """
        for yokyu_kubun in ["B", "H", "J"]:
            minimal_request_data = {"yokyu_kubun": yokyu_kubun}
            
            # テスト実行
            result = get_order_details_dictionary(minimal_request_data)
            
            # 辞書が返されることを確認（他の必須フィールドが不足していても）
            assert isinstance(result, dict), f"最小限データでの要求区分{yokyu_kubun}で辞書が返されませんでした"
            assert len(result) > 0, f"最小限データでの要求区分{yokyu_kubun}で空でない辞書が返されませんでした"

    def test_implementation_behavior_consistency(self):
        """
        実装の一貫性確認テスト
        yokyu_kubunキーの存在チェックが各機能で一貫していることを確認
        """
        # 不正なリクエストデータ（yokyu_kubun欠如）
        invalid_request = {"denbun_kubun": "20", "gyomu_kubun": "0067"}
        
        # get_order_details_dictionary では KeyError が発生することを確認
        with pytest.raises(KeyError):
            get_order_details_dictionary(invalid_request)
        
        # 他の関数でも同様の動作をすることを想定
        # （実際の実装に応じてテストを追加）
        
    def test_edge_case_handling(self):
        """
        エッジケースのハンドリングテスト
        """
        # 空の辞書
        with pytest.raises(KeyError):
            get_order_details_dictionary({})
        
        # Noneの場合
        with pytest.raises(TypeError):
            get_order_details_dictionary(None)
        
        # yokyu_kubunがNoneの場合
        request_with_none_yokyu = {"yokyu_kubun": None}
        result = get_order_details_dictionary(request_with_none_yokyu)
        # Noneは "B", "H", "J" に含まれないので空辞書が返される
        assert result == {}, "yokyu_kubun=Noneで空辞書が返されませんでした"
        
        # 空文字列の場合
        request_with_empty_yokyu = {"yokyu_kubun": ""}
        result = get_order_details_dictionary(request_with_empty_yokyu)
        # 空文字列は "B", "H", "J" に含まれないので空辞書が返される
        assert result == {}, "yokyu_kubun=''で空辞書が返されませんでした"
        
        # 無効な値の場合
        for invalid_yokyu in ["X", "1", "AB", "b", "h", "j"]:  # 小文字や無効な値
            request_with_invalid_yokyu = {"yokyu_kubun": invalid_yokyu}
            result = get_order_details_dictionary(request_with_invalid_yokyu)
            assert result == {}, f"yokyu_kubun={invalid_yokyu}で空辞書が返されませんでした"


if __name__ == "__main__":
    # テスト実行用のエントリポイント
    pytest.main([__file__, "-v", "--tb=short"])