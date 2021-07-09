from django.core.management.base import BaseCommand
import argparse
from SuiSiannAdminApp.models import 句表, 文章表
from os.path import basename
import csv
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = '逐篇文章音檔kah句的csv檔，寄入來db'

    def add_arguments(self, parser):
        parser.add_argument('csv', nargs='+', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        for csvPath in options['csv']:
            tongMia = 提著csv檔名(csvPath.name)
            # Khiam 文章名
            try:
                一文章 = 文章表(文章名=tongMia)
                一文章.save()
            except IntegrityError:
                raise RuntimeError('{}：文章已經匯--li̍p-bâi矣'.format(tongMia))
            # Khiam 文章的句
            csvDict = csv.DictReader(csvPath)
            頂音檔名 = None
            頂一句漢字 = []
            頂一句台羅 = []
            for tsua in csvDict:
                # 新音檔
                if tsua['Im-tóng'] != 頂音檔名 and 頂音檔名 is not None:
                    漢字 = '\n'.join(頂一句漢字)
                    台羅 = '\n'.join(頂一句台羅)
                    一句 = 句表(
                        來源=一文章,
                        音檔=頂音檔名,
                        原始漢字=漢字,
                        原始羅馬字=台羅,
                        漢字=漢字,
                        羅馬字=台羅,
                    )
                    一句.save()
                    頂音檔名 = tsua['Im-tóng']
                    頂一句漢字 = [tsua['Hàn-jī'], ]
                    頂一句台羅 = [tsua['Lô-má-jī'], ]
                # 頭一擺
                elif tsua['Im-tóng'] != 頂音檔名:
                    頂音檔名 = tsua['Im-tóng']
                    頂一句漢字.append(tsua['Hàn-jī'])
                    頂一句台羅.append(tsua['Lô-má-jī'])
                #
                else:
                    頂一句漢字.append(tsua['Hàn-jī'])
                    頂一句台羅.append(tsua['Lô-má-jī'])
            # 匯入最後一个音檔
            漢字 = '\n'.join(頂一句漢字)
            台羅 = '\n'.join(頂一句台羅)
            一句 = 句表(
                來源=一文章,
                音檔=頂音檔名,
                原始漢字=漢字,
                原始羅馬字=台羅,
                漢字=漢字,
                羅馬字=台羅,
            )
            一句.save()


def 提著csv檔名(csv路徑):
    檔名 = basename(csv路徑)
    點所在 = 檔名.index('.')
    純檔名 = 檔名[:點所在].replace('_hanlo', '')
    return 純檔名
