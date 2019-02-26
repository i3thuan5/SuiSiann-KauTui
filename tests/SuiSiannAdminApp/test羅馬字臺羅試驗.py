from unittest.case import TestCase

from SuiSiannAdminApp.models import 句表


class 羅馬字單元試驗(TestCase):
    def test_正確(self):
        句 = 句表.objects.create(
            原始漢字="豬",
            原始臺羅="ti",
            漢字="豬仔",
            臺羅="ti-á"
        )
        self.assertEqual(句.羅馬字, "ti-á", )

    def test_無對齊(self):
        句 = 句表.objects.create(
            原始漢字="豬",
            原始臺羅="ti",
            漢字="豬仔",
            臺羅="ti-á"
        )
        self.assertEqual(句.原始羅馬字, "ti", )
