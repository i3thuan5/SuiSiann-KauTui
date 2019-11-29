from csv import DictReader
from filecmp import cmp
import json
from os.path import join, basename, dirname
from tempfile import TemporaryDirectory
from unittest.case import skip

from SuiSiannAdminApp.models import 句表, 文章表
from django.core.management import call_command
from django.test.testcases import TestCase


class 匯出Dataset試驗(TestCase):
    def test_資料照來源排(self):
        with TemporaryDirectory() as tsuliaugiap:
            im = join(dirname(__file__), 'Oct 13, 2018 _243.wav')
            文章 = 文章表.objects.create(文章名='33')
            self.hue(文章, 'sui', im)

            kiatko = join(tsuliaugiap, 'kiatko')
            call_command('匯出Dataset', kiatko)
            with open(join(kiatko, 'sui-siann.csv')) as tong:
                tsitpit = list(DictReader(tong))[0]
                self.assertEqual(tsitpit['來源'], '33')
                self.assertEqual(tsitpit['漢字'], 'sui')
                self.assertEqual(tsitpit['羅馬字'], 'sui')

    def test_分號(self):
        with TemporaryDirectory() as tsuliaugiap:
            im = join(dirname(__file__), 'Oct 13, 2018 _243.wav')
            文章 = 文章表.objects.create(文章名='33')
            漢 = '包括全羅三百四十六萬兩千三百六十七个音節佮漢羅五百五十六萬八千空五十七个音節；'
            lo = (
                'Pau-kuah tsuân-lô sann-pah sì-tsa̍p-la̍k-bān nn̄g-tshing sann-pah la̍k-tsa̍p-tshit ê im-tsiat kah '
                'Hàn-lô gōo-pah gōo-tsa̍p-la̍k-bān peh-tshing khòng gōo-tsa̍p-tshit ê im-tsiat;'
            )
            句表.objects.create(
                來源=文章,
                音檔=basename(im),
                原始漢字=漢,
                原始臺羅=lo,
                漢字=漢,
                臺羅=lo,
                kaldi切音時間=[],
            )

            kiatko = join(tsuliaugiap, 'kiatko')
            call_command('匯出Dataset', kiatko)
            with open(join(kiatko, 'sui-siann.csv')) as tong:
                tsitpit = list(DictReader(tong))[0]
                self.assertEqual(tsitpit['來源'], '33')
                self.assertEqual(tsitpit['漢字'], 漢)
                self.assertEqual(tsitpit['羅馬字'], lo)

    def test_音檔名重編號(self):
        with TemporaryDirectory() as tsuliaugiap:
            im = join(dirname(__file__), 'Oct 13, 2018 _243.wav')
            文章 = 文章表.objects.create(文章名='33')
            self.hue(文章, 'sui', im)

            kiatko = join(tsuliaugiap, 'kiatko')
            call_command('匯出Dataset', kiatko)
            with open(join(kiatko, 'sui-siann.csv')) as tong:
                tsitpit = list(DictReader(tong))[0]
                self.assertEqual(tsitpit['音檔'], 'ImTong/SuiSiann_0001.wav')

    def test_音檔名有khoopi(self):
        with TemporaryDirectory() as tsuliaugiap:
            im = join(dirname(__file__), 'Oct 13, 2018 _243.wav')

            文章 = 文章表.objects.create(文章名='33')
            self.hue(文章, 'sui', im)

            kiatko = join(tsuliaugiap, 'kiatko')
            call_command('匯出Dataset', kiatko)
            self.assertEqual(
                open(im, 'rb').read(),
                open(join(kiatko, 'ImTong/SuiSiann_0001.wav'), 'rb').read()
            )
            self.assertTrue(
                cmp(im, join(kiatko, 'ImTong/SuiSiann_0001.wav'))
            )

    @skip
    def test_照對齊結果切(self):
        raise NotImplementedError()

    def hue(self, 文章, ji, imtong):
        句表.objects.create(
            來源=文章,
            音檔=basename(imtong),
            原始漢字=ji,
            原始臺羅=ji,
            漢字=ji,
            臺羅=ji,
            kaldi切音時間=[],
        )

    def theh(self):
        with TemporaryDirectory() as sootsai:
            tongmia = join(sootsai, 'lmj.json')
            call_command('匯出全部音節', tongmia)
            with open(tongmia) as tong:
                return json.load(tong)
