from flask import request, Response

def generate_error_response(X_shori_kekka: str = "99", status: int = 400) -> Response:
    """
    XML形式のエラーレスポンスを生成する
    """
    xml_response = f"""<?xml version="1.0" encoding="Shift_JIS"?>
<sejmsg xmlns="http://sej.co.jp/">
	<body>
		<X_shori_kekka>{X_shori_kekka}</X_shori_kekka>
	</body>
</sejmsg>"""
    print(f"レスポンスデータ: {xml_response}")
    return Response(xml_response.encode(encoding='cp932'), status=status, content_type='text/xml; charset=Windows-31J')


def validate_request_fields(req: dict, keys: list[str]) -> bool:
    """
    リクエストデータに指定された項目がすべて含まれているか検証し、
    不足している場合はエラーレスポンスを返す。

    Args:
        req (dict): リクエストデータ
        keys (list[str]): 必須項目のリスト

    Returns:
        bool: True = 必須項目なし / False = 必須項目あり
    """
    return not all(key in req for key in keys)


def req_res_map_flexible(
    map_pattern: dict[any, any],
    req_data: any,
    default_value: any = None
    ) -> any:
    """
    リクエストの値とレスポンスの値のマッピングを行うメソッド

    Parameters
    ----------
    map_pattern: dict[Any, Any]
        マッピングの辞書
    req_data: any
        リクエストのキー
    default_value: any, optional
        該当するキーがない場合のデフォルト値 (デフォルト: None)

    Returns
    -------
    any
        マッピングされた値、またはデフォルト値
    """
    return map_pattern.get(req_data, default_value)


def split_bits(num_str: str, split_pattern: list) -> list:
    """
    ビット区切りの文字列を指定された桁数で分割するメソッド
    Parameters
    ----------
    num_str: str
        分割したい数字の文字列
    split_pattern: list
        分割桁数のリスト

    Returns
    -------
        分割した数字リスト
    """
    number = int(num_str)
    # 与えられた数値を特定のビット長にパディングして2進数に変換
    total_bits = sum(split_pattern)
    binary_str = format(number, f'0{total_bits}b')

    # 各ビット長ごとに数値を分割し、int型に変換
    result = []
    start = 0
    for length in split_pattern:
        chunk = binary_str[start:start + length]
        result.append(int(chunk, 2))
        start += length

    return result


def process_mapping_code_segmentation(barcode_str: str, mapping_num: int) -> list | Response:
    """
    ビット区切りの文字列を指定された桁数で分割するメソッド
    Parameters
    ----------
    barcode_str: str
        バーコード番号の文字列
    mapping_num: int
        マッピング番号の数値

    Returns
    -------
        list | Response: マッピング番号ごとに分割した数字リスト または エラーレスポンス
    """
    definitions_map = {
        0: [  # No.1_購入・購入取消応答_マッピング
            3,  # [0]   処理結果（購入）
            4,  # [1]   応答結果（購入）
            3,  # [2]   チケット代金（購入）
            3,  # [3]   チケット枚数（購入）
            1,  # [4]   レスポンスパターン（再送用）（購入）
            3,  # [5]   処理結果（購入取消）
            3,  # [6]   応答結果（購入取消）
            3,  # [7]   チケット代金（購入取消）
            1,  # [8]   レスポンスパターン（再送用）（購入取消）
            2,  # [9]   ショップID（購入取消）
            2   # [10]  マッピング番号
        ],
        1: [  # No.2_本投票・本投票障害取消応答_マッピング
            3,  # [0]   チケット代金（購入）
            2,  # [1]   チケット枚数（購入）
            3,  # [2]   処理結果（購入取消）
            3,  # [3]   応答結果（購入取消）
            3,  # [4]   処理結果（本投票）
            4,  # [5]   応答結果（本投票）
            3,  # [6]   券面情報データ（本投票）
            1,  # [7]   投票券バーコード番号印字要否（本投票）
            1,  # [8]   totoセンター応答結果（本投票）
            3,  # [9]   処理結果（本投票障害取消）
            4,  # [10]  応答結果（本投票障害取消）
            1,  # [11]  totoセンター応答結果（本投票障害取消）
            2   # [12]  マッピング番号
        ],
        2: [  # No.3_払戻・払戻取消応答_マッピング
            3,  # [0]   処理結果（払戻）
            4,  # [1]   応答結果（払戻）
            2,  # [2]   払戻金額（払戻）
            1,  # [3]   レスポンスパターン（再送用）（払戻）
            3,  # [4]   処理結果（払戻取消）
            3,  # [5]   応答結果（払戻取消）
            2,  # [6]   払戻金額（払戻取消）
            1,  # [7]   レスポンスパターン（再送用）
            2,  # [8]   ショップID（払戻取消）
            2   # [9]   マッピング番号
        ],
        3: [  # No.4_当せん返還消込応答_マッピング
            2,  # [0]   払戻金額（払戻）
            3,  # [1]   処理結果（払戻取消）
            3,  # [2]   応答結果（払戻取消）
            2,  # [3]   払戻金額（払戻取消）
            3,  # [4]   処理結果（当せん返還消込）
            4,  # [5]   応答結果（当せん返還消込）
            2,  # [6]   totoセンター応答結果（当せん返還消込）
            2   # [7]   マッピング番号
        ]
    }
    mapping = definitions_map.get(mapping_num)
    if mapping is None:
        return generate_error_response()
    return split_bits(barcode_str, mapping)
