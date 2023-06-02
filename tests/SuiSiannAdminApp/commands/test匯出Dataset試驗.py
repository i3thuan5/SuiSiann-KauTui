from csv import DictReader
import json
from os.path import join, basename, dirname
from tempfile import TemporaryDirectory
from unittest.mock import patch

from SuiSiannAdminApp.models import 句表, 文章表
from django.core.management import call_command
from django.test.testcases import TestCase

from phiaua.models import Khuán


class 匯出Dataset試驗(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        khuán = Khuán.objects.create(miâ='口語調', iūnn='color')
        khuán.luī.create(miâ='本調', siktsuí='#ff0000', singāu=0)
        khuán.luī.create(miâ='規則變調', siktsuí='#ff0000', singāu=1)

    def test_資料照來源排(self):
        with TemporaryDirectory() as tsuliaugiap:
            im = 'Oct 13, 2018 _243.wav'
            文章 = 文章表.objects.create(文章名='33')
            self.hue(
                文章, '媠。', '<p><span class="lui-1">Su&iacute;</span>.</p>', im
            )

            kiatko = join(tsuliaugiap, 'kiatko')
            with patch('SuiSiannAdminApp.management.commands.匯出Dataset.urlopen') as mock:
                with open(join(dirname(__file__), im), 'rb') as imtong:
                    (
                        mock.return_value.__enter__.return_value
                        .read.return_value
                    ) = imtong.read()
                call_command('匯出Dataset', kiatko)
            with open(join(kiatko, 'SuiSiann.csv')) as tong:
                tsitpit = list(DictReader(tong))[0]
                self.assertEqual(tsitpit['來源'], '33')
                self.assertEqual(tsitpit['漢字'], '媠。')
                self.assertEqual(tsitpit['羅馬字'], 'Suí.')
                self.assertEqual(tsitpit['口語調'], 'Suí本.')

    def test_分號(self):
        with TemporaryDirectory() as tsuliaugiap:
            im = 'Oct 13, 2018 _243.wav'
            文章 = 文章表.objects.create(文章名='33')
            漢 = '包括全羅三百四十六萬兩千三百六十七个音節佮漢羅五百五十六萬八千空五十七个音節；'
            lo = (
                'Pau-kuah tsuân-lô sann-pah sì-tsa̍p-la̍k-bān nn̄g-tshing sann-pah la̍k-tsa̍p-tshit ê im-tsiat kah '
                'Hàn-lô gōo-pah gōo-tsa̍p-la̍k-bān peh-tshing khòng gōo-tsa̍p-tshit ê im-tsiat;'
            )
            ku = 句表.objects.create(
                來源=文章,
                音檔=im,
                S3音檔=im,
                原始漢字=漢,
                原始羅馬字=lo,
                漢字=漢,
                羅馬字含口語調=lo,
                kaldi切音時間=[(0.0, 7.0), ],
            )
            ku.full_clean()
            ku.save()

            kiatko = join(tsuliaugiap, 'kiatko')
            with patch('SuiSiannAdminApp.management.commands.匯出Dataset.urlopen') as mock:
                with open(join(dirname(__file__), im), 'rb') as imtong:
                    (
                        mock.return_value.__enter__.return_value
                        .read.return_value
                    ) = imtong.read()
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
            self.hue(
                文章, '媠', '<p><span class="lui-1">Suí</span></p>', im
            )

            kiatko = join(tsuliaugiap, 'kiatko')
            with patch('SuiSiannAdminApp.management.commands.匯出Dataset.urlopen') as mock:
                with open(join(dirname(__file__), im), 'rb') as imtong:
                    (
                        mock.return_value.__enter__.return_value
                        .read.return_value
                    ) = imtong.read()
                call_command('匯出Dataset', kiatko)
            with open(join(kiatko, 'SuiSiann.csv')) as tong:
                tsitpit = list(DictReader(tong))[0]
                self.assertEqual(tsitpit['音檔'], 'ImTong/SuiSiann_0001.wav')

    def hue(self, 文章, han, khaugi, imtong):
        ku = 句表.objects.create(
            來源=文章,
            音檔=basename(imtong),
            S3音檔=imtong,
            原始漢字=han,
            原始羅馬字=khaugi,
            漢字=han,
            羅馬字含口語調=khaugi,
            kaldi切音時間=[(0.0, 7.0), ],
        )
        ku.full_clean()
        ku.save()

    def theh(self):
        with TemporaryDirectory() as sootsai:
            tongmia = join(sootsai, 'lmj.json')
            call_command('匯出全部音節', tongmia)
            with open(tongmia) as tong:
                return json.load(tong)
