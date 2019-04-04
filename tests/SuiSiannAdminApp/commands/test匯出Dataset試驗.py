from csv import DictReader
from filecmp import cmp
import json
from os.path import join
from tempfile import TemporaryDirectory
import wave

from SuiSiannAdminApp.models import 句表, 文章表
from django.core.management import call_command
from django.test.testcases import TestCase


class 匯出Dataset試驗(TestCase):
    def test_資料照來源排(self):
        with TemporaryDirectory() as tsuliaugiap:
            im = join(tsuliaugiap, 'Oct 3.wav')
            self.siaimtong(im)
            文章 = 文章表.objects.create(文章名='33')
            self.hue(文章, 'sui', im)

            kiatko = join(tsuliaugiap, 'kiatko')
            call_command('匯出Dataset', kiatko)
            with open(join(kiatko, 'sui-siann.csv')) as tong:
                tsitpit = list(DictReader(tong))[0]
                self.assertEqual(tsitpit['音檔'], 'ImTong/SuiSiann_0001.wav')
                self.assertEqual(tsitpit['來源'], '33')
                self.assertEqual(tsitpit['漢字'], 'sui')
                self.assertEqual(tsitpit['羅馬字'], 'sui')

    def test_音檔名重編號(self):
        with TemporaryDirectory() as tsuliaugiap:
            im = join(tsuliaugiap, 'Oct 3.wav')
            self.siaimtong(im)
            文章 = 文章表.objects.create(文章名='33')
            self.hue(文章, 'sui', im)

            kiatko = join(tsuliaugiap, 'kiatko')
            call_command('匯出Dataset', kiatko)
            self.assertTrue(
                cmp(im), join(tsuliaugiap, 'ImTong/SuiSiann_0001.wav')
            )

    def hue(self, 文章, ji, imtong):
        句表.objects.create(
            來源=文章,
            音檔=None,
            原始漢字=ji,
            原始臺羅=ji,
            漢字=ji,
            臺羅=ji,
            對齊結果=[],
        )

    def siaimtong(self, sootsai):
        with wave.open(sootsai, 'wb') as 音檔:
            音檔.setnchannels(1)
            音檔.setframerate(16000)
            音檔.setsampwidth(2)
            音檔.writeframesraw(b'0' * 100)

    def theh(self):
        with TemporaryDirectory() as sootsai:
            tongmia = join(sootsai, 'lmj.json')
            call_command('匯出全部音節', tongmia)
            with open(tongmia) as tong:
                return json.load(tong)
