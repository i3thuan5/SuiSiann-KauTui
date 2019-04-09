from csv import DictWriter
from os import makedirs
from os.path import join, relpath
from shutil import copy

from SuiSiannAdminApp.models import 句表
from django.conf import settings
from django.core.management.base import BaseCommand


from SuiSiannAdminApp.management.算音檔網址 import 音檔網址表


class Command(BaseCommand):

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
            for kui, 句 in enumerate(
                句表.objects.order_by('來源_id').select_related('來源'),
                start=1,
            ):
                wavtongmia = 'ImTong/SuiSiann_{:04}.wav'.format(kui)
                sia.writerow({
                    '音檔': wavtongmia,
                    '來源': 句.來源.文章名,
                    '漢字': 句.漢字,
                    '羅馬字': 句.羅馬字,
                })
                copy(
                    join(
                        settings.MEDIA_ROOT,
                        relpath(音檔網址表[句.音檔], settings.MEDIA_URL)
                    ),
                    join(options['TsuLiauGiap'], wavtongmia)
                )
