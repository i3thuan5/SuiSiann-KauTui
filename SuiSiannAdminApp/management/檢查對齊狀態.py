from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤


def 檢查對齊狀態(hanji, lomaji):
    對齊 = 檢查對齊(hanji, lomaji)
    if 對齊 is not True:
        return 對齊
    
    用字 = 檢查對齊()


def 檢查對齊(hanji, lomaji):
    try:
        拆文分析器.對齊句物件(hanji, lomaji)
    except 解析錯誤 as 錯誤:
        return str(錯誤)
    else:
        return True


def 檢查用字(hanji, lomaji):
    