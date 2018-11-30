import sys
import csv
from tool.csv漢字正規化 import 漢字正規化


def csv正規化(輸入檔名):
    with open(輸入檔名, 'r') as csv檔:
        csv檔頭 = csv.reader(csv檔)
        tshingTuann = list(csv檔頭)
        print(tshingTuann)
        return 
        kiatKo = []
        for tsua in csv檔頭:
            temp = tsua
            hanji = 漢字正規化(temp['Hàn-jī'])
            kiatKo.append(temp.update({
                hanji
            }))

    with open(輸入檔名, 'w') as 正規化檔:
        正規化檔頭 = csv.DictWriter(正規化檔)
            
            
if __name__ == '__main__':
    輸入檔名 = sys.argv[1]
    csv正規化(輸入檔名)