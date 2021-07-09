import json

from SuiSiannAdminApp.models import 句表
from django.core.management.base import BaseCommand


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('輸出json名',)

    def handle(self, *args, **options):
        輸出名 = options['輸出json名']
        u = dict()
        for 句 in 句表.objects.all():
            for lmj in 拆文分析器.建立句物件(句.羅馬字).轉音(臺灣閩南語羅馬字拼音).篩出字物件():
                if lmj.敢是標點符號():
                    continue
                型 = lmj.型.rstrip('0987654321')
                try:
                    u[型] += 1
                except KeyError:
                    u[型] = 1
        with open(輸出名, 'w') as tong:
            json.dump(
                u,
                tong,
                ensure_ascii=False,
                sort_keys=True,
                indent=2,
            )
