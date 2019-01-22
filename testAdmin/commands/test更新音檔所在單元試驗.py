from django.test.testcases import TestCase
from SuiSiannAdminApp.models import 句表
from SuiSiannAdminApp.management.commands.更新音檔所在 import 更新音檔所在


class 更新音檔所在單元試驗(TestCase):
    def test_改著一筆(self):
        一句 = 句表.objects.create(
            音檔="Oct 8, 1.wav",
            漢字="A", 原始漢字="A",
            臺羅="a", 原始臺羅="a",
        )
        更新音檔所在()
        音檔所在 = 句表.objects.get(pk=一句.pk).音檔
        self.assertEqual(音檔所在, "Oct 13, 1.wav")

    def test_袂改著Oct8以外的日期(self):
        一句 = 句表.objects.create(
            音檔="Oct 20, 1.wav",
            漢字="A", 原始漢字="A",
            臺羅="a", 原始臺羅="a",
        )
        更新音檔所在()
        音檔所在 = 句表.objects.get(pk=一句.pk).音檔
        self.assertEqual(音檔所在, "Oct 20, 1.wav")
