from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 用字.models import 用字表


def 檢查對齊狀態(hanji, lomaji):
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
    else:
        return ''
