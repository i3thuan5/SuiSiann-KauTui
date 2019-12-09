from csv import DictReader
from filecmp import cmp
import json
from os.path import join, basename, dirname
from tempfile import TemporaryDirectory

from SuiSiannAdminApp.models import 句表, 文章表
from django.core.management import call_command
from django.test.testcases import TestCase


from SuiSiannAdminApp.management.commands.匯出Dataset import Command


class 匯出Dataset試驗(TestCase):
    def test_資料照來源排(self):
        with TemporaryDirectory() as tsuliaugiap:
            im = 'Oct 13, 2018 _243.wav'
            文章 = 文章表.objects.create(文章名='33')
            self.hue(文章, 'sui', im)

            kiatko = join(tsuliaugiap, 'kiatko')
            call_command('匯出Dataset', kiatko)
            with open(join(kiatko, 'SuiSiann.csv')) as tong:
                tsitpit = list(DictReader(tong))[0]
                self.assertEqual(tsitpit['來源'], '33')
                self.assertEqual(tsitpit['漢字'], 'sui')
                self.assertEqual(tsitpit['羅馬字'], 'sui')

    def test_分號(self):
        with TemporaryDirectory() as tsuliaugiap:
            im = 'Oct 13, 2018 _243.wav'
            文章 = 文章表.objects.create(文章名='33')
            漢 = '包括全羅三百四十六萬兩千三百六十七个音節佮漢羅五百五十六萬八千空五十七个音節；'
            lo = (
                'Pau-kuah tsuân-lô sann-pah sì-tsa̍p-la̍k-bān nn̄g-tshing sann-pah la̍k-tsa̍p-tshit ê im-tsiat kah '
                'Hàn-lô gōo-pah gōo-tsa̍p-la̍k-bān peh-tshing khòng gōo-tsa̍p-tshit ê im-tsiat;'
            )
            句表.objects.create(
                來源=文章,
                音檔=im,
                原始漢字=漢,
                原始臺羅=lo,
                漢字=漢,
                臺羅=lo,
                kaldi切音時間=[],
            )

            kiatko = join(tsuliaugiap, 'kiatko')
            call_command('匯出Dataset', kiatko)
            with open(join(kiatko, 'SuiSiann.csv')) as tong:
                tsitpit = list(DictReader(tong))[0]
                self.assertEqual(tsitpit['來源'], '33')
                self.assertEqual(tsitpit['漢字'], 漢)
                self.assertEqual(tsitpit['羅馬字'], lo)

    def test_音檔名重編號(self):
        with TemporaryDirectory() as tsuliaugiap:
            im = 'Oct 13, 2018 _243.wav'
            文章 = 文章表.objects.create(文章名='33')
            self.hue(文章, 'sui', im)

            kiatko = join(tsuliaugiap, 'kiatko')
            call_command('匯出Dataset', kiatko)
            with open(join(kiatko, 'SuiSiann.csv')) as tong:
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

    def test_對齊結果切出2筆(self):
        with TemporaryDirectory() as tsuliaugiap:
            im = 'Oct 13, 2018 _243.wav'
            文章 = 文章表.objects.create(文章名='33')
            漢 = '包括全羅\n漢羅'
            lo = (
                'Pau-kuah tsuân-lô \n'
                'Hàn-lô'
            )
            句表.objects.create(
                來源=文章,
                音檔=im,
                原始漢字=漢,
                原始臺羅=lo,
                漢字=漢,
                臺羅=lo,
                kaldi切音時間=[[0., 3.], [4., 7.]],
            )

            kiatko = join(tsuliaugiap, 'kiatko')
            call_command('匯出Dataset', kiatko)
            with open(join(kiatko, 'SuiSiann.csv')) as tong:
                tsitpit = list(DictReader(tong))
                self.assertEqual(len(tsitpit), 2)

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


class Kap時間試驗(TestCase):
    def test_時間加點01秒(self):
        '參考LJSpeech有加0.005秒空--ê，到開始閣有0.005秒，攏總0.01秒'
        punte = [['漢', 'Lô', (1.3, 2.5)], ['漢', 'Lô', (3.3, 3.5), ]]
        kiatko = [['漢', 'Lô', (1.29, 2.51)], ['漢', 'Lô', (3.29, 3.51), ]]
        self.assertEqual(Command().kap時間(5.0, punte), kiatko)

    def test_時間加點01秒嘛袂使超過音檔(self):
        punte = [['漢', 'Lô', (0.0, 2.7)]]
        kiatko = [['漢', 'Lô', (0.0, 2.7)]]
        self.assertEqual(Command().kap時間(2.7, punte), kiatko)

    def test_時間差無零點75秒就kap做伙(self):
        'https://gist.github.com/keithito/771cfc1a1ab69d1957914e377e65b6bd#file-segment-py-L148'
        punte = [['漢', 'Lô', (1.3, 2.5)], ['漢', 'Lô', (3.1, 3.5), ]]
        kiatko = [['漢 漢', 'Lô Lô', (1.29, 3.51)]]
        self.assertEqual(Command().kap時間(6.7, punte), kiatko)

    def test_加起來超過10秒莫kap(self):
        punte = [['漢', 'Lô', (1.3, 2.5)], ['漢', 'Lô', (3.0, 12.5), ]]
        kiatko = [['漢', 'Lô', (1.29, 2.51)], ['漢', 'Lô', (2.99, 12.51), ]]
        self.assertEqual(Command().kap時間(16.7, punte), kiatko)

    def test_換逝提掉(self):
        punte = [['漢\n', 'Lô\n', (1.3, 2.5)], ['漢\n', 'Lô\n', (3.1, 3.5), ]]
        kiatko = [['漢 漢', 'Lô Lô', (1.29, 3.51)]]
        self.assertEqual(Command().kap時間(6.7, punte), kiatko)
