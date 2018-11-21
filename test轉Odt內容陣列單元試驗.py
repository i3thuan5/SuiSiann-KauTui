from unittest.case import TestCase
from 錄音稿的odt轉csv import odt內容轉陣列



class 轉odt內容陣列單元試驗(TestCase):
    def test幾若逝(self):
        odt內容字串 = [
            "漢字_1", "lomaji_1", 
            "漢字_2", "lomaji_2",
            "",
            "漢字_3", "lomaji_3",
        ]
        結果 = odt內容轉陣列(odt內容字串)
        self.assertEqual(結果, [
            ["漢字_1", "lomaji_1"],
            ["漢字_2", "lomaji_2"],
            ["漢字_3", "lomaji_3"],
        ])
    
    def test開頭有換逝(self):
        odt內容字串 = [
            "",
            "漢字_1", "lomaji_1", 
        ]
        結果 = odt內容轉陣列(odt內容字串)
        self.assertEqual(結果, [
            ["漢字_1", "lomaji_1"],
        ])
        
    def test提掉上尾一逝的頁碼(self):
        odt內容字串 = [
            "漢字_1", "lomaji_1", 
            "英語詞--16", "英語詞--16"
        ]
        結果 = odt內容轉陣列(odt內容字串)
        self.assertEqual(結果, [
            ["漢字_1", "lomaji_1"],
        ])