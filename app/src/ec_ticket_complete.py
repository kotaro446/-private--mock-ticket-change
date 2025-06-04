import in_const as in_const
import time
from ticket_library import (
    req_res_map,
    split_bits,
)
from ec_ticket_library import (
    get_ticket_info,
    get_ec_kanryo_inshi_syukin_gaku,
)

def get_ec_complete_field(request_data:dict, mapping_str:str) -> tuple[dict,dict,dict,int]:

    mapping = split_bits(mapping_str, [
        11,# reserved
        2, # mapping[1]支払種別
        1, # mapping[2]納品種別
        2, # mapping[3]売上計上区分
        2, # mapping[4]印紙基準額/収納金額
        1, # mapping[5]価格変更フラグ
        1, # mapping[6]機能区分
        2, # mapping[7]SHOPCD
        3, # mapping[8]チケット枚数
        3, # mapping[9]処理結果
        2, # mapping[10]応答結果
        2, # mapping[11]支払方法区分
        2, # mapping[12]成功までの失敗回数(未使用)
        2, # NoCare
    ]) # 36bit（内、11bitが未使用、23bitがオプション、2bitがマップ番号）

    # interface_infoの辞書を作成
    (interface_info,
     httpstatus) = get_interface_info(request_data, mapping)
    # order_infoの辞書を作成
    order_info = get_order_info(request_data, mapping)
    # ticket_infoの辞書を作成
    ticket_info = get_ticket_info(request_data, mapping[8], order_info)
        
    return (interface_info, order_info, ticket_info, httpstatus)

def get_interface_info(request_data:dict, mapping:list)->tuple[dict, int]:
    """
    interface_infoの辞書を作成

    Parameters
    ----------
    request_data:dict  
    mapping:list  

    Returns
    -------
    interface_info:dict  
    httpstatus:int
    """
    interface_info:dict 
    httpstatus:int
    if request_data["toiawase_kanryo_kubun"] == "1":
        res_kanryo_syori_kekka = "00"
        httpstatus = 200
        interface_info = {
            "syori_kekka": res_kanryo_syori_kekka
        }
    elif request_data["toiawase_kanryo_kubun"] == "2":
        # 処理結果
        res_kanryo_syori_kekka, httpstatus = get_ec_kanryo_syori_kekka(mapping[9])
        # 支払方法区分
        res_kanryo_siharaihoho_kubun = get_ec_kanryo_siharaihoho_kubun(mapping[11])
        interface_info = {
            "syori_kekka": res_kanryo_syori_kekka,
            "shiharai_hoho_kbn": res_kanryo_siharaihoho_kubun
        }
    return (interface_info, httpstatus)

def get_order_info(request_data:dict, mapping:list)->dict:
    """
    order_infoの辞書を作成
    """
    order_info:dict

    #印紙基準額/収納金額(EC関連完了)
    res_kanryo_inshi_syukin_gaku = get_ec_kanryo_inshi_syukin_gaku(mapping[4])
    # SHOP-CD(EC関連完了) 
    res_kanryo_shop_id = get_ec_kanryo_shop_id_map10(mapping[7])

    if request_data["toiawase_kanryo_kubun"] == "1":
        # 応答結果
        res_kanryo_otoKekka = "00"
        # 支払種別(EC関連完了)
        res_kanryo_shiharai_syubetu = get_ec_kanryo_shiharai_syubetu(mapping[1])
        # 納品種別(EC関連完了)
        res_kanryo_nohin_syubetu = get_ec_kanryo_nohin_syubetu(mapping[2])
        # 売上計上区分(EC関連完了)
        res_kanryo_uriage_keijyo_kubun = get_ec_kanryo_uriage_keijyo_kubun(mapping[3])
        #価格変更フラグ(EC関連完了)
        res_kanryo_kakaku_flag = get_ec_kanryo_kakaku_flag(mapping[5])
        # 機能区分(EC関連完了)
        res_kanryo_kino_kubun = get_ec_kanryo_kino_kubun(mapping[6])
        order_info = {
            "oto_kekka": res_kanryo_otoKekka,
            "pay_type": res_kanryo_shiharai_syubetu,
            "dlv_type": res_kanryo_nohin_syubetu,
            "keijyo_type": res_kanryo_uriage_keijyo_kubun,
            "inshi_kijun": res_kanryo_inshi_syukin_gaku,
            "kingaku_henko_flg": res_kanryo_kakaku_flag,
            "kino_kbn": res_kanryo_kino_kubun,
            "shop_id": res_kanryo_shop_id,
            "shuno_kingaku": res_kanryo_inshi_syukin_gaku
        }
    elif request_data["toiawase_kanryo_kubun"] == "2":
        # 応答結果
        res_kanryo_otoKekka = get_ec_kanryo_otoKekka(mapping[10])
        order_info = {
            "oto_kekka": res_kanryo_otoKekka,
            "shop_id": res_kanryo_shop_id,
            "shuno_kingaku": res_kanryo_inshi_syukin_gaku,
        }
    else:
        raise ValueError(f"問合せ完了区分が不正です。{request_data["toiawase_kanryo_kubun"]}")
    return order_info

def get_ec_kanryo_shiharai_syubetu(map_num:int) -> str:
    """
    支払種別(EC関連完了)
    """
    res = req_res_map({
        0 : "1", #前払い
        1 : "2", #代金引換
        2 : "3", #後払い
    }, map_num, "1")
    return res

def get_ec_kanryo_nohin_syubetu(map_num:int)->str:
    """
    納品種別(EC関連完了)
    """
    res = req_res_map({
        0 : "1", #店渡し
        1 : "2", #宅配
    }, map_num, "1")
    return res

def get_ec_kanryo_uriage_keijyo_kubun(map_num:int)->str:
    """
    売上計上区分(EC関連完了)
    """
    res = req_res_map({
        0 : " ", #" "（半角空白）：預り金計上
        1 : "1", #売上計上
        2 : "2", #売上計上/未収入金計上
    }, map_num, " ")
    return res


def get_ec_kanryo_kakaku_flag(map_num:int)->str:
    """
    価格変更フラグ(EC関連完了)
    """
    res = req_res_map({
        0 : " ", #(空白半角) :下記以外の場合
        1 : "1", #合計金額の変更がある場合
    }, map_num, " ")
    return res

def get_ec_kanryo_kino_kubun(map_num:int)->str:
    """
    機能区分(EC関連完了)
    """
    res = req_res_map({
        0 : "3", #チケット発券
        1 : "5", #新プリペイドサービス
    }, map_num, "3")
    return res

def get_ec_kanryo_shop_id_map10(map_num:int)->str:
    """
    SHOP-CD(EC関連完了)　No.3_EC関連完了応答_マッピング
    """
    res = req_res_map({
        0 : "00000", #オリンピックチケット以外
        1 : "00236", #オリンピックチケット
        2 : "00745", #その他チケット
        3 : "30731", #ぴあ
    }, map_num, "00000")
    return res

def get_ec_kanryo_syori_kekka(map_num:int)->tuple[str,int]:
    """
    処理結果(EC関連完了)
    """
    res = req_res_map({
        0: ("00", 200, False), #正常
        1: ("10", 400, False), #電文区分エラー
        2: ("11", 400, False), #業務区分エラー
        3: ("14", 400, False), #サービス時間帯エラー
        4: ("99", 400, False), #その他エラー (400)
        5: ("99", 500, False), #その他エラー (500)
        6: ("00", 200, True),  #タイムアウト（正常）
        7: ("99", 500, True),  #タイムアウト（その他エラー500)
    }, map_num, ("00", 200, False))
    if res[2]:
        time.sleep(in_const.TIMEOUT_SEC)
    return res[:2]

def get_ec_kanryo_otoKekka(map_num:int) -> str:
    """
    応答結果(EC関連完了)
    """
    res = req_res_map({
        0 : "00", #正常応答
        1 : "01", #検索キーエラー
        2 : "99", #その他エラー
    }, map_num, "00")
    return res

def get_ec_kanryo_siharaihoho_kubun(map_num:int) -> str:
    """
    支払方法区分(EC関連完了)   
    """
    res = req_res_map({
        0 : "1", #クレジット支払
        1 : "2", #クレジット支払以外
        2 : " ", #” ”スペース：ネット商品返品の場合
    }, map_num, "1")
    return res

