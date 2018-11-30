from unittest.case import TestCase
from src.csv漢字正規化 import 漢字正規化


class 漢字正規化單元試驗(TestCase):
    def test_全形括號共提掉(self):
        han = "「這个老歲仔呔會遮爾戇（gōng）啦？」"
        expect = "「這个老歲仔呔會遮爾戇啦？」"
        self.assertEqual(漢字正規化(han), expect)
    
    def test_半形括號共提掉(self):
        han = "哎呀！管遐濟創啥(siánnh)？"
        expect = "哎呀！管遐濟創啥？"
        self.assertEqual(漢字正規化(han), expect)