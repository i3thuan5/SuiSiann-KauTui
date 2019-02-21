from django.test.testcases import TestCase
from os.path import join
from SuiSiannAdminApp.models import 句表
from django.core.management import call_command
from django.conf import settings


class 匯入csv試驗(TestCase):
    def setUp(self):
        pass

    def test_匯入一音檔一句(self):
        csvPath = join(settings.BASE_DIR, 'csv', '服務台_hanlo.odt.csv')
        call_command("匯入csv", csvPath)
        self.assertEqual(len(句表.objects.all()), 6)

    def test_匯入一音檔多句(self):
        csvPath = join(settings.BASE_DIR, 'csv_piansik', '664_雨後驕陽01.odt.csv')
        call_command("匯入csv", csvPath)
        self.assertEqual(len(句表.objects.all()), 72)

    def test_匯入一音檔多句_001含2句(self):
        csvPath = join(settings.BASE_DIR, 'csv_piansik', '664_雨後驕陽01.odt.csv')
        call_command("匯入csv", csvPath)
        句 = 句表.objects.get(音檔='Dia001.wav')
        self.assertEqual(句.漢字, '喂，\n萬財！')

    def test_匯入一音檔多句_072含1句(self):
        csvPath = join(settings.BASE_DIR, 'csv_piansik', '664_雨後驕陽01.odt.csv')
        call_command("匯入csv", csvPath)
        句 = 句表.objects.get(音檔='Dia072.wav')
        self.assertEqual(句.漢字, '你看起來足瘦的，')

    def test_匯入一音檔多句_033含1句_羅(self):
        csvPath = join(settings.BASE_DIR, 'csv_piansik', '664_雨後驕陽01.odt.csv')
        call_command("匯入csv", csvPath)
        句 = 句表.objects.get(音檔='Dia033.wav')
        self.assertEqual(句.臺羅, "Îng-tshàn--ah,\nlâi lâi lâi,\nlâi tsia!")

    def test_匯入兩擺失敗(self):
        csvPath = join(settings.BASE_DIR, 'csv', '服務台_hanlo.odt.csv')
        # import 1st time
        call_command("匯入csv", csvPath)
        # import 2nd time
        with self.assertRaises(RuntimeError):
            call_command("匯入csv", csvPath)
