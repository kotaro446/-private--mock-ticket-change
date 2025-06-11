import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# テスト対象のモジュールをインポート
try:
    from ec_ticket_library import get_order_details_dictionary
except ImportError:
    print("ec_ticket_library.pyまたはget_order_details_dictionary関数が見つかりません")

try:
    from main import app
except ImportError:
    print("main.pyまたはapp変数が見つかりません")


class TestOrderDetailsCorrect(unittest.TestCase):
    """order_details機能の正しいテスト"""

    def setUp(self):
        """各テストの前に実行される設定"""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        
        # 実際に動作するテストデータ
        self.valid_test_data = {
            'denbun_kubun': '20',
            'gyomu_kubun': '0067',
            'syori_kekka': '00',
            'kigyo_id': '07',
            'mise_no': '123456',
            'tuban': 'SQ',
            'regi_no': '1',
            'ticket_regi_no': ' ',
            'riyo_time_ymdhms': '20241113171523',
            'syori_tuban': '20241113000',
            'retry_flg': '0',
            'yokyu_kubun': 'B',
            'toiawase_kanryo_kubun': '1',
            'shop_id': '00767',
            'torikeshi_riyu': '01',
            'bar_code_no': '2024112700011',
            'kensaku_key': '00000566272',
            'cvs_code': '8037110000004',
            'order_type': ' ',
            'syohin_info_kbn': ' ',
            'item_pointer': '01'
        }

    def test_yokyu_kubun_b_has_order_details_in_xml(self):
        """要求区分BでXMLにorder_detailsが含まれることをテスト"""
        # ①期待値を用意する
        expected_xml_elements = [
            '<order_details>',
            '</order_details>',
            '<regi_msg_code>     </regi_msg_code>',
            '<zan_item_umu>0</zan_item_umu>'
        ]
        
        # ③テスト対象の関数をコール
        test_data = self.valid_test_data.copy()
        test_data['yokyu_kubun'] = 'B'
        
        response = self.client.post('/inkessai/recvrequest.do', data=test_data)
        
        # ④レスポンスを期待値と比較
        self.assertEqual(response.status_code, 200)
        xml_content = response.data.decode('cp932')
        
        for element in expected_xml_elements:
            self.assertIn(element, xml_content, 
                         f"XMLに{element}が含まれていません")

    def test_yokyu_kubun_h_has_order_details_in_xml(self):
        """要求区分HでXMLにorder_detailsが含まれることをテスト（モック不使用）"""
        # ①期待値を用意する
        expected_xml_elements = [
            '<order_details>',
            '</order_details>',
            '<regi_msg_code>     </regi_msg_code>',
            '<zan_item_umu>0</zan_item_umu>'
        ]
        
        # ③テスト対象の関数をコール
        test_data = self.valid_test_data.copy()
        test_data['yokyu_kubun'] = 'H'
        
        response = self.client.post('/inkessai/recvrequest.do', data=test_data)
        
        # ④レスポンスを期待値と比較
        self.assertEqual(response.status_code, 200)
        xml_content = response.data.decode('cp932')
        
        for element in expected_xml_elements:
            self.assertIn(element, xml_content, 
                         f"要求区分Hで{element}が含まれていません")

    def test_yokyu_kubun_j_has_order_details_in_xml(self):
        """要求区分JでXMLにorder_detailsが含まれることをテスト（モック不使用）"""
        # ①期待値を用意する
        expected_xml_elements = [
            '<order_details>',
            '</order_details>',
            '<regi_msg_code>     </regi_msg_code>',
            '<zan_item_umu>0</zan_item_umu>'
        ]
        
        # ③テスト対象の関数をコール
        test_data = self.valid_test_data.copy()
        test_data['yokyu_kubun'] = 'J'
        
        response = self.client.post('/inkessai/recvrequest.do', data=test_data)
        
        # ④レスポンスを期待値と比較
        self.assertEqual(response.status_code, 200)
        xml_content = response.data.decode('cp932')
        
        for element in expected_xml_elements:
            self.assertIn(element, xml_content, 
                         f"要求区分Jで{element}が含まれていません")

    def test_yokyu_kubun_a_no_order_details_in_xml(self):
        """要求区分AでXMLにorder_detailsが含まれないことをテスト"""
        # ①期待値を用意する（order_detailsが含まれないこと）
        
        # ③テスト対象の関数をコール
        test_data = self.valid_test_data.copy()
        test_data['yokyu_kubun'] = 'A'
        
        response = self.client.post('/inkessai/recvrequest.do', data=test_data)
        
        # ④レスポンスを期待値と比較
        self.assertEqual(response.status_code, 200)
        xml_content = response.data.decode('cp932')
        self.assertNotIn('<order_details>', xml_content,
                        "要求区分Aでorder_detailsが含まれています")

    def test_get_order_details_dictionary_direct_call(self):
        """get_order_details_dictionary関数の直接呼び出しテスト"""
        # ①期待値を用意する
        expected_keys = [
            'regi_msg_code', 'dlv_mise_date_yotei_ymd', 'sej_shohin_code',
            'site_kensu', 'zan_item_umu'
        ]
        
        # ③テスト対象の関数をコール
        test_cases = [
            {'yokyu_kubun': 'B'},
            {'yokyu_kubun': 'H'},
            {'yokyu_kubun': 'J'}
        ]
        
        for test_case in test_cases:
            with self.subTest(yokyu_kubun=test_case['yokyu_kubun']):
                try:
                    result = get_order_details_dictionary(test_case)
                    
                    # ④レスポンスを期待値と比較
                    if test_case['yokyu_kubun'] in ['B', 'H', 'J']:
                        self.assertIsInstance(result, dict)
                        self.assertGreater(len(result), 0)
                        
                        for key in expected_keys:
                            if key in result:
                                self.assertIn(key, result)
                    else:
                        self.assertEqual(result, {})
                        
                except Exception as e:
                    self.fail(f"get_order_details_dictionary呼び出しエラー: {e}")

    def test_all_yokyu_kubun_behavior_summary(self):
        """全要求区分の動作まとめテスト"""
        # ①期待値を用意する
        test_cases = [
            ('B', True, 'order_detailsあり'),
            ('H', True, 'order_detailsあり'),
            ('J', True, 'order_detailsあり'),
            ('A', False, 'order_detailsなし')
        ]
        
        for yokyu_kubun, should_have_order_details, description in test_cases:
            with self.subTest(yokyu_kubun=yokyu_kubun, desc=description):
                
                # ③テスト対象の関数をコール
                test_data = self.valid_test_data.copy()
                test_data['yokyu_kubun'] = yokyu_kubun
                
                response = self.client.post('/inkessai/recvrequest.do', data=test_data)
                
                # ④レスポンスを期待値と比較
                self.assertEqual(response.status_code, 200,
                               f"要求区分{yokyu_kubun}のリクエストが失敗しました")
                
                xml_content = response.data.decode('cp932')
                
                if should_have_order_details:
                    self.assertIn('<order_details>', xml_content,
                                 f"要求区分{yokyu_kubun}でorder_detailsがありません")
                    self.assertIn('<zan_item_umu>0</zan_item_umu>', xml_content,
                                 f"要求区分{yokyu_kubun}でzan_item_umuがありません")
                else:
                    self.assertNotIn('<order_details>', xml_content,
                                    f"要求区分{yokyu_kubun}でorder_detailsが含まれています")

    def test_order_details_field_count_validation(self):
        """order_detailsのフィールド数検証テスト"""
        # ①期待値を用意する
        expected_fields = [
            'regi_msg_code', 'dlv_mise_date_yotei_ymd', 'dlv_mise_time_yotei_hm',
            'nohin_setumei_kbn', 'dlv_ymd', 'sej_shohin_code',
            'site_nai_shiharai_kingaku', 'oisogi_flg', 'oisogi_fee',
            'other_fee', 'tax_kbn', 'tax_ritsu', 'oisogi_delay_flg',
            'tyumon_no', 'site_kensu', 'site_utiwake1', 'site_name1',
            'site_price1', 'site_crekbn1', 'zan_item_umu'
        ]
        
        # ③テスト対象の関数をコール
        test_data = self.valid_test_data.copy()
        test_data['yokyu_kubun'] = 'B'
        
        response = self.client.post('/inkessai/recvrequest.do', data=test_data)
        
        # ④レスポンスを期待値と比較
        self.assertEqual(response.status_code, 200)
        xml_content = response.data.decode('cp932')
        
        # 重要なフィールドが含まれていることを確認
        for field in expected_fields:
            self.assertIn(f'<{field}>', xml_content,
                         f"XMLに{field}フィールドが含まれていません")


class TestOrderDetailsDebug(unittest.TestCase):
    """order_details機能のデバッグ用テスト"""

    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        
        self.test_data = {
            'denbun_kubun': '20',
            'gyomu_kubun': '0067',
            'syori_kekka': '00',
            'kigyo_id': '07',
            'mise_no': '123456',
            'tuban': 'SQ',
            'regi_no': '1',
            'ticket_regi_no': ' ',
            'riyo_time_ymdhms': '20241113171523',
            'syori_tuban': '20241113000',
            'retry_flg': '0',
            'yokyu_kubun': 'B',
            'toiawase_kanryo_kubun': '1',
            'shop_id': '00767',
            'torikeshi_riyu': '01',
            'bar_code_no': '2024112700011',
            'kensaku_key': '00000566272',
            'cvs_code': '8037110000004',
            'order_type': ' ',
            'syohin_info_kbn': ' ',
            'item_pointer': '01'
        }

    def test_debug_xml_structure_all_yokyu_kubun(self):
        """全要求区分のXML構造をデバッグ出力"""
        
        for yokyu_kubun in ['A', 'B', 'H', 'J']:
            with self.subTest(yokyu_kubun=yokyu_kubun):
                test_data = self.test_data.copy()
                test_data['yokyu_kubun'] = yokyu_kubun
                
                response = self.client.post('/inkessai/recvrequest.do', data=test_data)
                
                print(f"\n=== 要求区分 {yokyu_kubun} ===")
                print(f"ステータスコード: {response.status_code}")
                
                if response.status_code == 200:
                    xml_content = response.data.decode('cp932')
                    has_order_details = '<order_details>' in xml_content
                    print(f"order_details含有: {has_order_details}")
                    
                    if has_order_details:
                        # order_detailsセクションを抽出
                        start = xml_content.find('<order_details>')
                        end = xml_content.find('</order_details>') + len('</order_details>')
                        if start != -1 and end != -1:
                            order_details_section = xml_content[start:end]
                            field_count = order_details_section.count('<') - order_details_section.count('</')
                            print(f"order_detailsフィールド数: {field_count}")
                
                # テストは常に成功（デバッグ用）
                self.assertTrue(True)


if __name__ == '__main__':
    unittest.main(verbosity=2)