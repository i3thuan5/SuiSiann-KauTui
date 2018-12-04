from django.core.management.base import BaseCommand
import argparse
from sunko.models import 句表
from os.path import basename


class Command(BaseCommand):
    help = '逐篇文章音檔kah句的csv檔，寄入來db'

    def add_arguments(self, parser):
        parser.add_argument('--csv', nargs='+', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        for csvPath in options['csv']:
            tongMia = 提著csv檔名(csvPath.name)
            print('name={}'.format(tongMia))
#             一文章 = 文章表(文章名=tongMia)
#             for tsua in csvTong:
#                 print(tsua)


def 提著csv檔名(csv路徑):
    檔名 = basename(csv路徑)
    點所在 = 檔名.index('.')
    純檔名 = 檔名[:點所在].replace('_hanlo', '')
    return 純檔名


def csv寄入去db(一筆):
    一句物件 = 句表(
        音檔=一筆['Im-tóng'],
        漢字=一筆['Hàn-jī'],
        臺羅=一筆['Lô-má-jī']
    )
    一句物件.save()
