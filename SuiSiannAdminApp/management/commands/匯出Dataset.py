from csv import DictWriter
from os import makedirs
from os.path import join, relpath

from SuiSiannAdminApp.models import 句表
from django.conf import settings
from django.core.management.base import BaseCommand
from librosa.core.audio import get_duration
from subprocess import run

from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器

from SuiSiannAdminApp.management.算音檔網址 import 音檔網址表


class Command(BaseCommand):
    tongmia = 'ImTong/SuiSiann_{:04}.wav'
    # https://gist.github.com/keithito/771cfc1a1ab69d1957914e377e65b6bd#file-segment-py-L147-L149
    max_duration = 10.0
    max_gap_duration = 0.75
    threshold = 40.0

    def add_arguments(self, parser):
        parser.add_argument('TsuLiauGiap',)
        parser.add_argument(
            '--mai_imtong', action="store_true",
            help='Mài輸出音檔，beh看統計niâ。',
            )

    def handle(self, *args, **options):
        ai_imtong = not options['mai_imtong']
        makedirs(join(options['TsuLiauGiap'], 'ImTong'))
        csvtongmia = join(options['TsuLiauGiap'], 'SuiSiann.csv')

        with open(csvtongmia, 'wt', encoding='utf-8') as tong:
            sia = DictWriter(tong, fieldnames=[
                '音檔',
                '來源',
                '漢字',
                '羅馬字',
                '長短',
            ])
            sia.writeheader()
            kui = 1
            bio = 0.0
            lts = 0.0
            su_soo = 0
            lmj = set()
            for 句 in (
                句表.objects.order_by('來源_id', 'id').select_related('來源')
            ):
                原始音檔 = join(
                    settings.MEDIA_ROOT,
                    relpath(音檔網址表[句.音檔], settings.MEDIA_URL)
                )
                longtsong = get_duration(filename=原始音檔)
                lts += longtsong
                if len(句.kaldi切音時間) == 0:
                    raise ValueError('有音檔bô用kaldi切音！')
                tsuliau = zip(
                    句.漢字.rstrip().split('\n'),
                    句.羅馬字.rstrip().split('\n'),
                    句.kaldi切音時間
                )
                for han, lo, (thau, bue) in self.kap時間(longtsong, tsuliau):
                    wavtongmia = self.tongmia.format(kui)
                    kui += 1
                    ku_tngte = bue - thau
                    bio += ku_tngte
                    句物件 = 拆文分析器.建立句物件(han, lo)
                    su_soo += len(句物件.網出詞物件())
                    sia.writerow({
                        '音檔': wavtongmia,
                        '來源': 句.來源.文章名,
                        '漢字': han.rstrip(),
                        '羅馬字': lo.rstrip(),
                        '長短': '{:.2f}'.format(ku_tngte),
                    })
                    kiatko_mia = join(options['TsuLiauGiap'], wavtongmia)
                    if ai_imtong:
                        run(
                            [
                                'sox', 原始音檔, kiatko_mia,
                                'trim', '{:.5f}'.format(thau), '{:.5f}'.format(ku_tngte),
                            ],
                            check=True,
                        )
                    print(
                        (
                            '結果粒積秒數：{:.2f} 本底音檔秒數：{:.2f}\n'
                            '總詞數：{}'
                        ).format(bio, lts, su_soo),
                        file=self.stderr
                    )

    def kap時間(self, longtsong, tsuliau):
        kap = []
        for han, lo, (thau, bue) in tsuliau:
            han = han.strip()
            lo = lo.strip()
            if (
                len(kap) > 0
                and thau - kap[-1][2][1] <= self.max_gap_duration
                and bue - kap[-1][2][0] <= self.max_duration
            ):
                siongbue = kap.pop()
                kap.append([
                    siongbue[0] + ' ' + han,
                    siongbue[1] + ' ' + lo,
                    (siongbue[2][0], bue)
                ])
            else:
                kap.append([han, lo, (thau, bue)])
        kiatko = []
        for han, lo, (thau, bue) in kap:
            thau -= 0.01
            if thau < 0:
                thau = 0
            bue += 0.01
            if bue > longtsong:
                bue = longtsong
            kiatko.append([han, lo, (thau, bue)])
        return kiatko
