from unittest.case import TestCase
from sunko.management.正規化漢字 import 提掉漢字的括號


class 漢字正規化單元試驗(TestCase):
    def test_全形括號共提掉(self):
        han = "「這个老歲仔呔會遮爾戇（gōng）啦？」"
        expect = "「這个老歲仔呔會遮爾戇啦？」"
        self.assertEqual(提掉漢字的括號(han), expect)

    def test_半形括號共提掉(self):
        han = "哎呀！管遐濟創啥(siánnh)？"
        expect = "哎呀！管遐濟創啥？"
        self.assertEqual(提掉漢字的括號(han), expect)

    def test_大頭仔王的_兩个全形括號(self):
        han = "漢鍾離的圓仔親像雞卵遐爾大圈（khian），大頭仔王的搩（kiat）兩粒落去，腹肚已經有小可仔飽矣。"
        expect = "漢鍾離的圓仔親像雞卵遐爾大圈，大頭仔王的搩兩粒落去，腹肚已經有小可仔飽矣。"
        self.assertEqual(提掉漢字的括號(han), expect)

    def test_大頭仔王的_一全形一半形(self):
        han = "漢鍾離的圓仔親像雞卵遐爾大圈(khian)，大頭仔王的搩（kiat）兩粒落去，腹肚已經有小可仔飽矣。"
        expect = "漢鍾離的圓仔親像雞卵遐爾大圈，大頭仔王的搩兩粒落去，腹肚已經有小可仔飽矣。"
        self.assertEqual(提掉漢字的括號(han), expect)
