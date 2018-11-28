from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
import csv
import sys


def 檢查一段漢羅對齊(tsua):
    if tsua['Tsing-kui-hàn-jī']:
        han = tsua['Tsing-kui-hàn-jī']
    else:
        han = tsua['Hàn-jī'] 
    
    if tsua['Tsing-kui-lô-má-jī']:
        lo = tsua['Tsing-kui-lô-má-jī']
    else:
        lo = tsua['Lô-má-jī']
    拆文分析器.對齊句物件(han, lo)
    return True

def 檢查csv漢羅對齊(輸入檔名):
    with open(輸入檔名, 'r') as csv檔:
        csv檔頭 = csv.DictReader(csv檔)
        for tsua in csv檔頭:
            檢查一段漢羅對齊(tsua)


if __name__ == '__main__':
    輸入檔名 = sys.argv[1]
    檢查csv漢羅對齊(輸入檔名)