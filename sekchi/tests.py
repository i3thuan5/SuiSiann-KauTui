from django.core.management import call_command
from django.test.testcases import TestCase
from sekchi.models import Sekchi


class 匯入csv來源試驗(TestCase):
    def test_來源有寫ê(self):
        Sekchi.objects.create(
            音檔所在='音檔檔名.wav',
            part=4,
            編號=2924,
        )
        call_command('micodad_to_csv')
        self.assertEqual(Sekchi.objects.get().來源, '三連音')

    def test_來源ài看進前ê(self):
        Sekchi.objects.create(
            音檔所在='音檔檔名.wav',
            part=3,
            編號=2315,
        )
        call_command('micodad_to_csv')
        self.assertEqual(Sekchi.objects.get().來源, '鍼,tserm(文)')

    def test_編號kangkhuan3(self):
        Sekchi.objects.create(
            音檔所在='音檔檔名.wav',
            part=3,
            編號=2258,
        )
        call_command('micodad_to_csv')
        self.assertEqual(Sekchi.objects.get().來源, '連續動詞')

    def test_編號kangkhuan2(self):
        Sekchi.objects.create(
            音檔所在='音檔檔名.wav',
            part=2,
            編號=2258,
        )
        call_command('micodad_to_csv')
        self.assertEqual(Sekchi.objects.get().來源, '三連音')

    def test_漢字(self):
        Sekchi.objects.create(
            音檔所在='音檔檔名.wav',
            part=2,
            編號=2105,
        )
        call_command('micodad_to_csv')
        self.assertEqual(Sekchi.objects.get().漢字, '熱人的荔枝甜甜甜，')

    def test_已校對的不能更改(self):
        Sekchi.objects.create(
            音檔所在='音檔檔名.wav',
            part=2,
            編號=2105,
            漢字='熱人的荔枝甜甜，'
        )
        call_command('micodad_to_csv')
        self.assertEqual(Sekchi.objects.get().漢字, '熱人的荔枝甜甜，')
