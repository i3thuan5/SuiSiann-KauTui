import sys
import csv
from tool.正規化漢字 import 漢字正規化


def csv正規化(輸入檔名):
    kiatKo = []
    with open(輸入檔名, 'r') as csv檔:
        csv檔頭 = csv.reader(csv檔)
        bunTsiunn = list(csv檔頭)
        print('bunTsiunn=', bunTsiunn)
        for tsua in bunTsiunn:
            piHun = dict(tsua)
            print('pihun={}', piHun)
            tsingKuiHanji = 漢字正規化(piHun['Hàn-jī'])
            kiatKo.append(piHun.update({
                'Tsing-kui-hàn-jī': tsingKuiHanji,
            }))

    with open(輸入檔名, 'w') as csv檔:
        try:
            fieldnames = bunTsiunn[0].keys()
        except Exception as e:
            raise
        csv檔頭 = csv.DictWriter(csv檔, fieldnames=fieldnames)
        csv檔頭.writeheader()
        for tsua in kiatKo:  
            csv檔頭.writerow(tsua)
            
    csv檔頭.writerow({'first_name': 'Baked', 'last_name': 'Beans'}) 
            
if __name__ == '__main__':
    輸入檔名 = sys.argv[1]
    csv正規化(輸入檔名)