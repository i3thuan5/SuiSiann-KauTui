from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
import csv
import sys
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤


def 檢查一段漢羅對齊(tsua):
    if tsua['Tsing-kui-hàn-jī']:
        han = tsua['Tsing-kui-hàn-jī']
    else:
        han = tsua['Hàn-jī']

    if tsua['Tsing-kui-lô-má-jī']:
        lo = tsua['Tsing-kui-lô-má-jī']
    else:
        lo = tsua['Lô-má-jī']
    try:
        拆文分析器.對齊句物件(han, lo)
    except 解析錯誤 as 錯誤:
        return str(錯誤)
    else:
        return True


def 檢查csv漢羅對齊(輸入檔名):
    with open(輸入檔名, 'r') as csv檔:
        csv檔頭 = csv.DictReader(csv檔)
        tshoNgoo = ""
        for hoBe, tsua in enumerate(csv檔頭):
            kiatKo = 檢查一段漢羅對齊(tsua)
            if kiatKo != True:
                tshoNgoo += '\n\n{}.\n{}\n'.format(hoBe, kiatKo)
        if tshoNgoo:
            raise 解析錯誤(tshoNgoo)


if __name__ == '__main__':
    輸入檔名 = sys.argv[1]
    檢查csv漢羅對齊(輸入檔名)
