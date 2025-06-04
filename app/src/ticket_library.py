def req_res_map(
    map_pattern: dict,
    req_data: any,
    default_value: any = None
    ) -> any:
    """
    リクエストの値とレスポンスの値のマッピングを行うメソッド

    Parameters
    ----------
    map_pattern: dict
    req_data: any
    default_value: str
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

#CD計算方法(ＪＡＮ－１３コード等に使用)
def calculate_CD(decimal_string):
    # 初期値
    A = 0
    # 右側からサーチ，奇数桁/偶数桁を判断
    for i, char in enumerate(reversed(decimal_string), start=1):
        num = int(char)
        if i % 2 == 1:  # 奇数桁
            A += num * 3
        else:  # 偶数桁
            A += num * 1
    # 計算 B、C
    B = A % 10
    C = (10 - B) % 10
    return C
