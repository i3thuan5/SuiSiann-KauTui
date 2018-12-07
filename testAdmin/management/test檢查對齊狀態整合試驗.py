from unittest.case import TestCase
from SuiSiannAdminApp.management.檢查對齊狀態 import 檢查對齊狀態


class 檢查對齊狀態整合試驗(TestCase):
    def tearDown(self):
        if self.expect is True:
            self.assertEqual(檢查對齊狀態(self.hanji, self.lomaji), '')
        else:
            self.assertNotEqual(檢查對齊狀態(self.hanji, self.lomaji), '')

    def test_正確(self):
        self.hanji = "嚨喉擽擽"
        self.lomaji = "nâ-âu ngiau-ngiau"
        self.expect = True

    def test_無對齊(self):
        self.hanji = "嚨喉，樂樂"
        self.lomaji = "nâ-âu ngiau-ngiau"
        self.expect = False

    def test_字毋著(self):
        self.hanji = "嚨喉樂樂"
        self.lomaji = "nâ-âu ngiau-ngiau"
        self.expect = False

    def test_英語詞(self):
        self.hanji = "我欲去Seven"
        self.lomaji = "Guá beh-khì Seven"
        self.expect = True

    def test_漢字袂使有數字(self):
        self.hanji = "3月10號"
        self.lomaji = "sann gue̍h tsa̍p hō"
        self.expect = False
    
    def test_羅馬字袂使有數字(self):
        self.hanji = "3月10號"
        self.lomaji = "3 gue̍h tsa̍p hō"
        self.expect = False
        
    def test_合音(self):
        self.hanji = "siàng"
        self.lomaji = "siàng"
        self.expect = True
