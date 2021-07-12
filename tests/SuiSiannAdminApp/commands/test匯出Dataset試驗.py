from csv import DictReader
import json
from os.path import join, basename
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
            ku = 句表.objects.create(
                來源=文章,
                音檔=im,
                原始漢字=漢,
                原始羅馬字=lo,
                漢字=漢,
                羅馬字含口語調=lo,
                kaldi切音時間=[(0.0, 7.0), ],
            )
            ku.full_clean()
            ku.save()

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

    def test_對齊結果切出2筆(self):
        with TemporaryDirectory() as tsuliaugiap:
            im = 'Oct 13, 2018 _243.wav'
            文章 = 文章表.objects.create(文章名='33')
            漢 = '包括全羅\n漢羅'
            lo = (
                'Pau-kuah tsuân-lô \n'
                'Hàn-lô'
            )
            ku = 句表.objects.create(
                來源=文章,
                音檔=im,
                原始漢字=漢,
                原始羅馬字=lo,
                漢字=漢,
                羅馬字含口語調=lo,
                kaldi切音時間=[[0., 3.], [4., 7.]],
            )
            ku.full_clean()
            ku.save()

            kiatko = join(tsuliaugiap, 'kiatko')
            call_command('匯出Dataset', kiatko)
            with open(join(kiatko, 'SuiSiann.csv')) as tong:
                tsitpit = list(DictReader(tong))
                self.assertEqual(len(tsitpit), 2)

    def hue(self, 文章, ji, imtong):
        ku = 句表.objects.create(
            來源=文章,
            音檔=basename(imtong),
            原始漢字=ji,
            原始羅馬字=ji,
            漢字=ji,
            羅馬字含口語調=ji,
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

    def test_實際例(self):
        punte = [
            ('鳥啼聲含情帶意，\r', 'Tsiáu-thî-siann hâm tsîng tài ì,\r', [0.78, 3.51]),
            ('美麗春光滿滿是，\r', 'bí-lē tshun-kong muá-muá sī,\r',
             [4.26, 7.949999999999999]),
            ('有情人形影不離，', 'ū-tsîng lâng hîng-iánn put lī,',
             [7.95, 11.370000000000001]),
            ('談情在河邊，\r', 'tâm tsîng tsāi hô-pinn,\r', [11.37, 14.25]),
            ('好情意歡歡喜喜，\r', 'hó tsîng-ì huann-huann-hí-hí,\r',
             [14.25, 18.33]),
            ('笑容滿面好春天，', 'tshiò-iông muá-bīn hó tshun-thinn,',
             [18.33, 22.08]),
            ('無論是海角天邊，\r', 'bô-lūn sī hái-kak thinn-pinn,\r',
             [22.08, 25.68]),
            ('也不來分離。\r', 'iā put lâi hun-lī.\r', [25.68, 28.95]),
            ('雙人是春風滿面，', 'Siang-lâng sī tshun-hong muá-bīn,',
             [28.95, 32.25])
        ]
        kiatko = [
            ['鳥啼聲含情帶意， 美麗春光滿滿是，', 'Tsiáu-thî-siann hâm tsîng tài ì, bí-lē tshun-kong muá-muá sī,',
                (0.77, 7.959999999999999)],
            ['有情人形影不離， 談情在河邊，',
                'ū-tsîng lâng hîng-iánn put lī, tâm tsîng tsāi hô-pinn,', (7.94, 14.26)],
            ['好情意歡歡喜喜， 笑容滿面好春天，',
                'hó tsîng-ì huann-huann-hí-hí, tshiò-iông muá-bīn hó tshun-thinn,', (14.24, 22.09)],
            ['無論是海角天邊， 也不來分離。', 'bô-lūn sī hái-kak thinn-pinn, iā put lâi hun-lī.',
                (22.069999999999997, 28.96)],
            ['雙人是春風滿面，', 'Siang-lâng sī tshun-hong muá-bīn,',
                (28.939999999999998, 32.26)]
        ]
        self.assertEqual(Command().kap時間(32.26, punte), kiatko)
