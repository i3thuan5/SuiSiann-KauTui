from django.test.testcases import TestCase
from SuiSiannAdminApp.models import 句表
from SuiSiannAdminApp.management.commands.對漢字更新音檔所在 import 對漢字更新音檔所在


class 對漢字更新音檔所在單元試驗(TestCase):
    def test_改著一筆(self):
        漢 = "佇高雄左營區有一粒山，看起來誠特別。"
        羅 = "Tī Ko-hiông Tsó-iânn-khu ū tsi̍t lia̍p suann, khuànn--khí-lâi tsiânn ti̍k-pia̍t."
        結果 = "Oct 20, 2018 _38_after.wav"
        一句 = 句表.objects.create(
            音檔="_38.wav",
            漢字=漢,
            羅馬字含口語調=羅,
            原始漢字="A",
            原始羅馬字="a",
        )
        一句.full_clean()
        一句.save()

        對漢字更新音檔所在(漢, 羅, 結果)
        音檔所在 = 句表.objects.get(pk=一句.pk).音檔
        self.assertEqual(音檔所在, 結果)
