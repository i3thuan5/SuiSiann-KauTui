from django.core.management.base import BaseCommand
from SuiSiannAdminApp.models import 句表


class Command(BaseCommand):
    help = '(oo)重算資料庫內底逐句的對齊狀態'

    def handle(self, *args, **options):
        for 句 in 句表.objects.all():
            # 儉句會重算對齊狀態
            句.save()
