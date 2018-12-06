from unittest.case import TestCase
from sunko.management.commands.匯入csv import 提著csv檔名


class 提著csv檔名單元試驗(TestCase):
    def test_對odt轉做csv(self):
        路徑 = '../csv/賣圓仔的神仙_hanlo.odt.csv'
        self.assertEqual(
            提著csv檔名(路徑),
            '賣圓仔的神仙'
        )

    def test_有空白(self):
        路徑 = '../csv/806 頁岩石油發展緊  OPEC地位不保.odt.csv'
        self.assertEqual(
            提著csv檔名(路徑),
            '806 頁岩石油發展緊  OPEC地位不保'
        )
