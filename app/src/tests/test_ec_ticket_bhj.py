import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# テスト対象のモジュールをインポート
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from ec_ticket import make_ticket_info
from ec_ticket_nomal import get_ec_nomal_field, get_order_info


class TestECTicketBHJOrderDetails(unittest.TestCase):
    """要求区分B・H・J時のorder_details返却テスト"""

    def setUp(self):
        """テストケースの初期設定"""
        # 基本的なリクエストデータのテンプレート
        self.base_request_data = {
            "denbun_kubun": "20",
            "syori_kekka": "00",
            "gyomu_kubun": "0067",
            "kigyo_id": "07",
            "mise_no": "123456",
            "tuban": "01",
            "regi_no": "001",
            "ticket_regi_no": "T001",
            "order_type": "1",
            "syohin_info_kbn": "1",
            "riyo_time_ymdhms": "20250610120000",
            "syori_tuban": "001",
            "retry_flg": "0",
            "toiawase_kanryo_kubun": "1",
            "kensaku_key": "12345678901",
            "bar_code_no": "1234567890123",
            "cvs_code": "8037110000004",
            "item_pointer": "1"
        }

    def test_yokyu_kubun_b_returns_order_details_normal_response(self):
        """要求区分B（チケット発券取消）で正常応答時のorder_details返却テスト"""
        # ①期待値を用意する
        request_data = self.base_request_data.copy()
        request_data["yokyu_kubun"] = "B"
        
        expected_order_info_keys = [
            "oto_kekka", "pay_type", "dlv_type", "keijyo_type", 
            "inshi_kijun", "kingaku_henko_flg", "kino_kbn", 
            "shop_id", "shuno_kingaku"
        ]
        
        # ②スタブを作る（mockを使用する）
        with patch('ec_ticket_library.get_test_option') as mock_get_test_option, \
             patch('ec_ticket_nomal.split_bits') as mock_split_bits:
            
            # get_test_optionが固定値を返すように設定
            mock_get_test_option.return_value = (0, "12345678901")
            
            # split_bitsが正常応答用のマッピング値を返すように設定
            # mapping[2] = 0 (応答結果 "00")、mapping[14] = 0 (取消応答結果 "00")
            mock_split_bits.return_value = [
                0,  # reserved
                0,  # mapping[1] 処理結果 (正常)
                0,  # mapping[2] 応答結果 (正常応答)
                1,  # mapping[3] 支払種別
                1,  # mapping[4] 納品種別
                1,  # mapping[5] 売上計上区分
                2,  # mapping[6] 印紙基準額
                0,  # mapping[7] 価格変更フラグ
                1,  # mapping[8] 機能区分
                1,  # mapping[9] SHOPCD
                2,  # mapping[10] 収納金額
                1,  # mapping[11] チケット枚数
                0,  # mapping[12] レスポンスパターン（再送区分用）
                0,  # mapping[13] 取消処理結果 (正常)
                0,  # mapping[14] 取消応答結果 (正常)
                0,  # mapping[15] レスポンスパターン（取消再送区分用）
                0   # NoCare
            ]
            
            # ③テスト対象の関数をコールする
            interface_info, order_info, ticket_info, payback_info, httpstatus = make_ticket_info(request_data)
            
            # ④レスポンスを期待値と比較する
            # order_infoが返されることを確認
            self.assertIsInstance(order_info, dict)
            self.assertNotEqual(len(order_info), 0, "order_infoが空ではないことを確認")
            
            # 期待されるキーが含まれていることを確認
            for key in expected_order_info_keys:
                self.assertIn(key, order_info, f"order_infoに{key}が含まれることを確認")
            
            # 正常応答であることを確認
            self.assertEqual(order_info["oto_kekka"], "00", "正常応答であることを確認")
            self.assertEqual(httpstatus, 200, "HTTPステータスが200であることを確認")

    def test_yokyu_kubun_h_returns_order_details_normal_response(self):
        """要求区分H（チケットプリンタエラー発券取消）で正常応答時のorder_details返却テスト"""
        # ①期待値を用意する
        request_data = self.base_request_data.copy()
        request_data["yokyu_kubun"] = "H"
        
        expected_order_info_keys = [
            "oto_kekka", "pay_type", "dlv_type", "keijyo_type", 
            "inshi_kijun", "kingaku_henko_flg", "kino_kbn", 
            "shop_id", "shuno_kingaku"
        ]
        
        # ②スタブを作る
        with patch('ec_ticket_library.get_test_option') as mock_get_test_option, \
             patch('ec_ticket_nomal.split_bits') as mock_split_bits:
            
            mock_get_test_option.return_value = (0, "12345678901")
            mock_split_bits.return_value = [
                0, 0, 0, 1, 1, 1, 2, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0
            ]
            
            # ③テスト対象の関数をコールする
            interface_info, order_info, ticket_info, payback_info, httpstatus = make_ticket_info(request_data)
            
            # ④レスポンスを期待値と比較する
            self.assertIsInstance(order_info, dict)
            self.assertNotEqual(len(order_info), 0)
            
            for key in expected_order_info_keys:
                self.assertIn(key, order_info)
            
            self.assertEqual(order_info["oto_kekka"], "00")
            self.assertEqual(httpstatus, 200)

    def test_yokyu_kubun_j_returns_order_details_normal_response(self):
        """要求区分J（XMLファイル・イメージファイル取得NG発券取消）で正常応答時のorder_details返却テスト"""
        # ①期待値を用意する
        request_data = self.base_request_data.copy()
        request_data["yokyu_kubun"] = "J"
        
        expected_order_info_keys = [
            "oto_kekka", "pay_type", "dlv_type", "keijyo_type", 
            "inshi_kijun", "kingaku_henko_flg", "kino_kbn", 
            "shop_id", "shuno_kingaku"
        ]
        
        # ②スタブを作る
        with patch('ec_ticket_library.get_test_option') as mock_get_test_option, \
             patch('ec_ticket_nomal.split_bits') as mock_split_bits:
            
            mock_get_test_option.return_value = (0, "12345678901")
            mock_split_bits.return_value = [
                0, 0, 0, 1, 1, 1, 2, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0
            ]
            
            # ③テスト対象の関数をコールする
            interface_info, order_info, ticket_info, payback_info, httpstatus = make_ticket_info(request_data)
            
            # ④レスポンスを期待値と比較する
            self.assertIsInstance(order_info, dict)
            self.assertNotEqual(len(order_info), 0)
            
            for key in expected_order_info_keys:
                self.assertIn(key, order_info)
            
            self.assertEqual(order_info["oto_kekka"], "00")
            self.assertEqual(httpstatus, 200)

    def test_yokyu_kubun_bhj_error_response_returns_empty_order_details(self):
        """要求区分B・H・Jでエラー応答時のorder_details返却テスト"""
        # ①期待値を用意する（エラー応答の場合）
        request_data = self.base_request_data.copy()
        request_data["yokyu_kubun"] = "B"
        
        expected_empty_order_info_keys = [
            "bar_code_no", "oto_kekka", "pay_type", "dlv_type", 
            "tenpo_bango", "mise_namek", "mise_address", "tenpo_tel_no",
            "keijyo_type", "inshi_kijun", "kingaku_henko_flg", "kino_kbn",
            "haraikomi_no", "shop_id", "shuno_kingaku", "shohin_daikin",
            "shop_namek", "user_namek", "renraku_saki"
        ]
        
        # ②スタブを作る（エラー応答用）
        with patch('ec_ticket_library.get_test_option') as mock_get_test_option, \
             patch('ec_ticket_nomal.split_bits') as mock_split_bits:
            
            mock_get_test_option.return_value = (0, "12345678901")
            # mapping[14] = 1 (取消応答結果 "01": 取消異常)
            mock_split_bits.return_value = [
                0, 0, 0, 1, 1, 1, 2, 0, 1, 1, 2, 1, 0, 0, 1, 0, 0
            ]
            
            # ③テスト対象の関数をコールする
            interface_info, order_info, ticket_info, payback_info, httpstatus = make_ticket_info(request_data)
            
            # ④レスポンスを期待値と比較する
            self.assertIsInstance(order_info, dict)
            self.assertNotEqual(len(order_info), 0)
            
            # エラー応答時は空白値が設定されたorder_infoが返される
            for key in expected_empty_order_info_keys:
                self.assertIn(key, order_info)
            
            self.assertEqual(order_info["oto_kekka"], "01", "エラー応答コードであることを確認")
            self.assertEqual(httpstatus, 200)

    def test_yokyu_kubun_bhj_retry_success_returns_order_details(self):
        """要求区分B・H・Jで再送成功時のorder_details返却テスト"""
        # ①期待値を用意する
        request_data = self.base_request_data.copy()
        request_data["yokyu_kubun"] = "B"
        request_data["retry_flg"] = "1"  # 再送フラグ
        
        expected_order_info_keys = [
            "oto_kekka", "pay_type", "dlv_type", "keijyo_type", 
            "inshi_kijun", "kingaku_henko_flg", "kino_kbn", 
            "shop_id", "shuno_kingaku"
        ]
        
        # ②スタブを作る
        with patch('ec_ticket_library.get_test_option') as mock_get_test_option, \
             patch('ec_ticket_nomal.split_bits') as mock_split_bits:
            
            mock_get_test_option.return_value = (0, "12345678901")
            # mapping[15] = 0 (レスポンスパターン取消再送: 再送正常)
            mock_split_bits.return_value = [
                0, 0, 0, 1, 1, 1, 2, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0
            ]
            
            # ③テスト対象の関数をコールする
            interface_info, order_info, ticket_info, payback_info, httpstatus = make_ticket_info(request_data)
            
            # ④レスポンスを期待値と比較する
            self.assertIsInstance(order_info, dict)
            self.assertNotEqual(len(order_info), 0)
            
            for key in expected_order_info_keys:
                self.assertIn(key, order_info)
            
            # 再送成功時は正常応答となる
            self.assertEqual(order_info["oto_kekka"], "00", "再送成功時は正常応答")
            self.assertEqual(httpstatus, 200)

    def test_yokyu_kubun_bhj_direct_function_call(self):
        """get_ec_nomal_field関数を直接呼び出すテスト"""
        # ①期待値を用意する
        request_data = self.base_request_data.copy()
        request_data["yokyu_kubun"] = "B"
        mapping_str = "12345678901"
        
        # ②スタブを作る
        with patch('ec_ticket_nomal.split_bits') as mock_split_bits:
            mock_split_bits.return_value = [
                0, 0, 0, 1, 1, 1, 2, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0
            ]
            
            # ③テスト対象の関数をコールする
            interface_info, order_info, ticket_info, httpstatus = get_ec_nomal_field(request_data, mapping_str)
            
            # ④レスポンスを期待値と比較する
            self.assertIsInstance(order_info, dict)
            self.assertIn("oto_kekka", order_info)
            self.assertEqual(order_info["oto_kekka"], "00")
            self.assertEqual(httpstatus, 200)


if __name__ == '__main__':
    # テストの実行
    unittest.main(verbosity=2)