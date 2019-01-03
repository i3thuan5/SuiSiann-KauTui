from django.core.management.base import BaseCommand
from SuiSiannAdminApp.models import 句表
from django.db.models import F
from django.db.models.expressions import Func, Value


class Command(BaseCommand):
    help = '修改資料庫內底的音檔所在'

    def handle(self, *args, **options):
        修改音檔所在()


def 修改音檔所在():
    句表.objects.filter(音檔__contains='Oct 8,').update(
        音檔=Func(
            F('音檔'),
            Value('Oct 8,'), Value('Oct 13,'),
            function='replace'
        ))
