from odf import text, teletype                                              
from odf.opendocument import load
import sys
import csv
from os import path, makedirs


def odt內容轉陣列(odt內容陣列):
    #
    # 因為內容有時為著排版共換逝提掉
    # 所以愛判斷siang是漢字逝，siang是羅馬字逝
    # khiam做 [[漢,羅][漢,羅]]
    #
    轉換陣列 = []
    han = None
    countHanLo = 0

    for tsua in odt內容陣列:
        trimTsua = tsua.strip()
        if trimTsua == '':
            # 清掉
            countHanLo = 0
        elif countHanLo % 2 == 0:
            # 頭一擺漢字
            han = trimTsua
            countHanLo += 1
        elif countHanLo % 2 == 1:
            # 羅馬字
            轉換陣列.append([han, trimTsua])
            countHanLo += 1
        else:
            raise RuntimeError('發生錯誤：', tsua)
    return 轉換陣列


def 讀odt檔(檔名):
    if '.odt' not in 檔名:
        exit(0) 
    textdoc = load(檔名)
    內容陣列 = []
    for line in textdoc.getElementsByType(text.P):
        tsua = teletype.extractText(line).strip()
        內容陣列.append(tsua)
    return 內容陣列

def 輸出csv檔(輸出檔名, 轉換陣列):
    with open('./csv/{}.csv'.format(輸出檔名), 'w') as csv檔:
        writer = csv.writer(csv檔)
        writer.writerow([
            'Im-tóng', 'Hàn-jī', 'Lô-má-jī', 
            'Tsing-kui-hàn-jī', 'Tsing-kui-lô-má-jī'])
        for 一組 in 轉換陣列:
            # 先共音檔欄位空咧
            writer.writerow([""]+一組)
        

def 錄音稿odt轉csv(輸入檔名, 輸出檔名):
    makedirs('csv', exist_ok=True)
    
    odt內容陣列 = 讀odt檔(輸入檔名)
    漢羅對應陣列 = odt內容轉陣列(odt內容陣列)
    輸出csv檔(輸出檔名, 漢羅對應陣列)

if __name__ == '__main__':
    輸入檔名 = sys.argv[1]
    輸出檔名 = sys.argv[2]
    錄音稿odt轉csv(輸入檔名, 輸出檔名)