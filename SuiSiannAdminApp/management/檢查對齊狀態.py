from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 用字.models import 用字表
from kesi.butkian.kongiong import si_lomaji


def 檢查對齊狀態(hanji, lomaji, khaugitiau=''):
    try:
        句物件 = 拆文分析器.對齊句物件(hanji, lomaji)
    except 解析錯誤 as 錯誤:
        return str(錯誤)

    毋著的字 = []
    字物陣列 = 句物件.篩出字物件()
    for 一字物 in 字物陣列:
        敢有 = 用字表.有這个字無(一字物)
        if 敢有 is not True and 一字物.型 != 一字物.音:
            毋著的字.append(一字物)

    if 毋著的字:
        return str(毋著的字)

    # 猶未標口語調ê純文字
    if not getattr(khaugitiau, 'p', None):
        return ''
    tshogoo = []
    ting1e_si_span = False
    ting1e_text = ''
    tshogoo_ji = ''
    for phiau_tag in khaugitiau.p.contents:
        tsite_si_span = phiau_tag.name == 'span'
        if ting1e_si_span and tsite_si_span:
            tshogoo_ji += ting1e_text
        elif not tsite_si_span:
            for jiguan in phiau_tag.string:
                if si_lomaji(jiguan):
                    tshogoo_ji += ting1e_text
                    ting1e_text = jiguan
                else:
                    if tshogoo_ji:
                        tshogoo_ji += ting1e_text
                        tshogoo.append(tshogoo_ji)
                    tshogoo_ji = ''
                    ting1e_text = ''
            continue
        elif tsite_si_span and tshogoo_ji:
            tshogoo_ji += ting1e_text
            tshogoo.append(tshogoo_ji)
            tshogoo_ji = ''
        else:
            pass
        ting1e_si_span = tsite_si_span
        ting1e_text = phiau_tag.string
    if tshogoo_ji:
        tshogoo_ji += ting1e_text
        tshogoo.append(tshogoo_ji)
    if tshogoo:
        return '{} 標記錯誤'.format('、'.join(tshogoo))
    else:
        return ''
