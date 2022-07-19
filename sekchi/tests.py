from django.core.management import call_command
from django.test.testcases import TestCase
from sekchi.models import Sekchi


# class 匯入csv試驗(TestCase):
#     def test_有匯漢字(self):
#         Sekchi.objects.create(
#             音檔所在='音檔檔名.wav',
#             part=1,
#             編號=1,
#         )
#         call_command('micodad_to_csv')
#         self.assertEqual(
#             Sekchi.objects.get().漢字,
#             '多元文化欲受人肯定， 語言佇公領域的呈現是真重要的開始。'
#         )

#     def test_有漢字就mài改(self):
#         Sekchi.objects.create(
#             音檔所在='音檔檔名.wav',
#             part=self.part,
#             編號=self.pianho,
#             漢字='有校對--ah',
#         )
#         call_command('micodad_to_csv')
#         self.assertEqual(Sekchi.objects.get().漢字, '有校對--ah')


class 匯入csv來源試驗(TestCase):
    def tearDown(self):
        call_command('micodad_to_csv')

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
