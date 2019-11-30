from csv import DictWriter
from os import makedirs
from os.path import join, relpath
from shutil import copy
import librosa

from SuiSiannAdminApp.models import 句表
from django.conf import settings
from django.core.management.base import BaseCommand


from SuiSiannAdminApp.management.算音檔網址 import 音檔網址表


class Command(BaseCommand):
    tongmia = 'ImTong/SuiSiann_{:04}.wav'

    def add_arguments(self, parser):
        parser.add_argument('TsuLiauGiap',)

    def handle(self, *args, **options):
        makedirs(join(options['TsuLiauGiap'], 'ImTong'))
        csvtongmia = join(options['TsuLiauGiap'], 'sui-siann.csv')

        with open(csvtongmia, 'wt', encoding='utf-8') as tong:
            sia = DictWriter(tong, fieldnames=[
                '音檔',
                '來源',
                '漢字',
                '羅馬字',
            ])
            sia.writeheader()
            kui = 1
            for 句 in (
                句表.objects.order_by('來源_id', 'id').select_related('來源')
            ):
                原始音檔 = join(
                    settings.MEDIA_ROOT,
                    relpath(音檔網址表[句.音檔], settings.MEDIA_URL)
                )
                if len(句.kaldi切音時間) == 0:
                    wavtongmia = self.tongmia.format(kui)
                    kui += 1
                    sia.writerow({
                        '音檔': wavtongmia,
                        '來源': 句.來源.文章名,
                        '漢字': 句.漢字,
                        '羅馬字': 句.羅馬字,
                    })
                    copy(
                        原始音檔,
                        join(options['TsuLiauGiap'], wavtongmia)
                    )
                else:
                    for han, lo, (thau, bue) in zip(
                        句.漢字.rstrip().split('\n'),
                        句.羅馬字.rstrip().split('\n'),
                        句.kaldi切音時間
                    ):
                        wavtongmia = self.tongmia.format(kui)
                        kui += 1
                        sia.writerow({
                            '音檔': wavtongmia,
                            '來源': 句.來源.文章名,
                            '漢字': han,
                            '羅馬字': lo,
                        })
                        y, sr = librosa.load(原始音檔,offset=thau, duration=bue-thau)
                        mia = join(options['TsuLiauGiap'], wavtongmia)
                        librosa.output.write_wav(mia, y, sr)
