import json

from SuiSiannAdminApp.models import 句表
from django.core.management.base import BaseCommand


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('hō-bé',)

    def handle(self, *args, **options):
        勾的號碼 = options['hō-bé']
        結果 = 句表.objects.filter(語料狀況=勾的號碼).values_list('id', '漢字', '臺羅', '備註')
        with open('印勾的句.txt', 'w') as file:
            for item in 結果:
                arr = list(item)
                arr[0] = str(arr[0])
                print('\n'.join(arr), file=file)
                print('', file=file)