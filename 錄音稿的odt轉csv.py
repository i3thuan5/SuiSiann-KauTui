from odf import text, teletype                                              
from odf.opendocument import load
import sys


def 讀odt檔(檔名):
    if '.odt' not in 檔名:
        exit(0) 
    textdoc = load(檔名)
    for line in textdoc.getElementsByType(text.P):
        print(teletype.extractText(line))


def 錄音稿odt轉csv(檔名):
    讀odt檔(檔名)


if __name__ == '__main__':
    檔名 = sys.argv[1]
    錄音稿odt轉csv(檔名)