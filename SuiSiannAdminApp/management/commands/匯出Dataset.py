import json

from SuiSiannAdminApp.models import 句表
from django.core.management.base import BaseCommand


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from os import makedirs


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('TsuLiauGiap',)

    def handle(self, *args, **options):
        makedirs(options['TsuLiauGiap'])

#         with open(options['json'], 'w') as tong:
#             json.dump(
#                 {'有聲調': sorted(u), '無聲調': sorted(bo)},
#                 tong,
#                 ensure_ascii=False,
#                 sort_keys=True,
#                 indent=2,
#             )
