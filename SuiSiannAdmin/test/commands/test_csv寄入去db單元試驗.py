from django.test.testcases import TestCase
from sunko.models import 句表
from sunko.management.commands.匯入csv import Command


class csv寄入去db單元試驗(TestCase):
    def test_一句(self):
        一筆csv = {
            'Im-tóng': '1.wav',
            'Hàn-jī': '豬',
            'Lô-má-jī': 'ti',
        }
        Command.csv寄入去db(一筆csv)
        self.assertEqual(len(句表.objects.all()), 1)
    
    def test_一句內容是豬(self):
        一筆csv = {
            'Im-tóng': '1.wav',
            'Hàn-jī': '豬',
            'Lô-má-jī': 'ti',
        }
        Command.csv寄入去db(一筆csv)
        一句物件 = 句表.objects.first()
        self.assertEqual(一句物件.漢字, '豬')
        
    def test_重複匯豬(self):
        一筆csv = {
            'Im-tóng': '1.wav',
            'Hàn-jī': '豬',
            'Lô-má-jī': 'ti',
        }
        #第一次
        Command.csv寄入去db(一筆csv)
        #第二次
        Command.csv寄入去db(一筆csv)
        一句物件 = 句表.objects.first()
        self.assertEqual(一句物件.漢字, '豬')