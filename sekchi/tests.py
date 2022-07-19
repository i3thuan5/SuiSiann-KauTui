from django.core.management import call_command
from django.test.testcases import TestCase
from sekchi.models import Sekchi


class 匯入csv試驗(TestCase):
    def tearDown(self):
        Sekchi.objects.create(
            音檔所在='音檔檔名.wav',
            part='4',
            編號='2923',
        )
        call_command('micodad_to_csv')
        self.assertEqual(Sekchi.objects.get().來源, self.來源)

    def test_來源有寫ê(self):
        self.part = '4'
        self.pianho = '2923'
        self.來源 = '三連音'

    def test_來源ài看進前ê(self):
        self.part = '3'
        self.pianho = 2284
        self.來源 = '針,tserm(文)'
