from django.core.management.base import BaseCommand
import argparse
from sunko.models import 句表, 文章表
from os.path import basename
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
import csv


class Command(BaseCommand):
    help = '逐篇文章音檔kah句的csv檔，寄入來db'

    def add_arguments(self, parser):
        parser.add_argument('--csv', nargs='+', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        for csvPath in options['csv']:
            tongMia = 提著csv檔名(csvPath.name)
            # Khiam 文章名
            一文章 = 文章表(文章名=tongMia)
            一文章.save()
            # Khiam 文章的句
            csvDict = csv.DictReader(csvPath)
            for tsua in csvDict:
                print(tsua['Im-tóng'], type(tsua['Im-tóng']))
                一句 = 句表(
                    來源=一文章,
                    音檔=tsua['Im-tóng'],
                    漢字=tsua['Hàn-jī'],
                    臺羅=tsua['Lô-má-jī'],
                    對齊狀態=檢查對齊狀態(tsua['Hàn-jī'], tsua['Lô-má-jī'])
                )
                一句.save()


def 提著csv檔名(csv路徑):
    檔名 = basename(csv路徑)
    點所在 = 檔名.index('.')
    純檔名 = 檔名[:點所在].replace('_hanlo', '')
    return 純檔名

def 檢查對齊狀態(hanji, romaji):
    try:
        拆文分析器.對齊句物件(hanji, romaji)
    except 解析錯誤 as 錯誤:
        return str(錯誤)
    else:
        return ''