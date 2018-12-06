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

    def test_兩組全形括號(self):
        han = "遐爾大圈（khian），大頭仔王的搩（kiat）兩粒落去，"
        expect = "遐爾大圈，大頭仔王的搩兩粒落去，"
        self.assertEqual(提掉漢字的括號(han), expect)

    def test_全一組半一組(self):
        han = "遐爾大圈(khian)，大頭仔王的搩（kiat）兩粒落去，"
        expect = "遐爾大圈，大頭仔王的搩兩粒落去，"
        self.assertEqual(提掉漢字的括號(han), expect)

    def test_倒全正半(self):
        han = "遐爾大圈（khian)，大頭仔"
        expect = "遐爾大圈，大頭仔"
        self.assertEqual(提掉漢字的括號(han), expect)
    
    def test_倒半正全(self):
        han = "遐爾大圈(khian），大頭仔"
        expect = "遐爾大圈，大頭仔"
        self.assertEqual(提掉漢字的括號(han), expect)
    
    def test_兩組混合(self):
        han = "遐爾大圈(khian），大頭仔搩（kiat)兩粒"
        expect = "遐爾大圈，大頭仔搩兩粒"
        self.assertEqual(提掉漢字的括號(han), expect)