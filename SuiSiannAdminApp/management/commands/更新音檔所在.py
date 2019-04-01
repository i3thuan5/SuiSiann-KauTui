from django.core.management.base import BaseCommand
from SuiSiannAdminApp.models import 句表
from django.db.models import F
from django.db.models.expressions import Func, Value
import csv


class Command(BaseCommand):
    help = '更新資料庫內底的音檔所在'

    def add_arguments(self, parser):
        parser.add_argument('csv', type=str, help='欲改ê句')
        
    def handle(self, *args, **options):
        with open(options['csv'], 'r') as csvTong:
            reader = csv.DictReader(csvTong)
            for tsua in reader:
                更新音檔所在(tsua['句編號'], tsua['頭四字'], tsua['新音檔所在'])


def 更新音檔所在(id, 漢字, 新檔):
    這句 = 句表.objects.get(id=id, 漢字__startswith=漢字)
    這句.音檔=新檔
    這句.save()
