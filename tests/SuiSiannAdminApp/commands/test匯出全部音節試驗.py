import json
from os.path import join
from tempfile import TemporaryDirectory

from SuiSiannAdminApp.models import 句表, 文章表
from django.core.management import call_command
from django.test.testcases import TestCase


class 匯出全部音節試驗(TestCase):
    def test_無聲調(self):
        self.hue('sui2 koo-niû')
        self.assertEqual(self.theh()['無聲調'], sorted({'sui', 'koo', 'niu'}))

    def test_有聲調(self):
        self.hue('sui2 koo-niû')
        self.assertEqual(self.theh()['有聲調'], sorted({'sui2', 'koo1', 'niu5'}))

    def test_標點莫算(self):
        self.hue(',')
        self.assertEqual(self.theh()['有聲調'], [])

    def test_英語莫算(self):
        self.hue('ABCD')
        self.assertEqual(self.theh()['有聲調'], [])

    def hue(self, ji):
        句表.objects.create(
            來源=文章表.objects.create(文章名='33'),
            音檔=None,
            原始漢字=ji,
            原始臺羅=ji,
            漢字=ji,
            臺羅=ji,
        )

    def theh(self):
        with TemporaryDirectory() as sootsai:
            tongmia = join(sootsai, 'lmj.json')
            call_command('匯出全部音節', tongmia)
            with open(tongmia) as tong:
                return json.load(tong)
