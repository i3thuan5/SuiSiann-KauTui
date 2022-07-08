from django.core.management.base import BaseCommand
from sekchi.models import Sekchi
from pathlib import Path
import csv

def micodad():
    # Hint: 要打開的檔案路徑是 'sekchi/csv/part1.csv'
    with ... as ...:

        # Hint: csvfile要是一個用open()方法回傳的file-object
        reader = csv.DictReader(csvfile)

        part1_dict = {}
        for row in reader:
            print(row)
            # Hint: 觀察 row 的資料結構
            # 取出「編號」、「漢字」兩個欄位，放進 part1_dict 裡面，key是編號，value是漢字
            # https://docs.python.org/3/library/csv.html#csv.DictReader

    print(part1_dict)
    # part1_dict的結果應該是
    {
     '1': '多元文化欲受人肯定， 語言佇公領域的呈現是真重要的開始。',
     '2': '這馬是原住民族語， 向望未來客家語、臺語攏有機會。',
    }


class Command(BaseCommand):

    def handle(self, *args, **options):
        micodad()
