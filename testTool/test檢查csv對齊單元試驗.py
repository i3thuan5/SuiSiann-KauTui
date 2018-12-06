from unittest.case import TestCase
from tool.檢查csv漢羅對齊 import 檢查一段漢羅對齊


class 檢查csv對齊單元試驗(TestCase):
    def test_一般(self):
        tsua = {
            'Hàn-jī': '豬',
            'Lô-má-jī': 'ti',
            'Tsing-kui-hàn-jī': '',
            'Tsing-kui-lô-má-jī': ''
        }
        self.assertTrue(檢查一段漢羅對齊(tsua))

    def test_先對齊正規化資料(self):
        tsua = {
            'Hàn-jī': '2000年',
            'Lô-má-jī': '2000 nî',
            'Tsing-kui-hàn-jī': '2000年',
            'Tsing-kui-lô-má-jī': 'Nn̄g-tshing nî'
        }
        self.assertEqual(
            檢查一段漢羅對齊(tsua),
            '詞組內底的型「2000年」比音「Nn̄g-tshing nî」少！' +
            '配對結果：[詞：[字：2000 Nn̄g, 字：年 tshing]]')
