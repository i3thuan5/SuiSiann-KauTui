from django.core.management.base import BaseCommand
from SuiSiannAdminApp.models import 句表
from django.db.models import F
from django.db.models.expressions import Func, Value


class Command(BaseCommand):
    help = '更新資料庫內底的音檔所在'

    def add_arguments(self, parser):
        parser.add_argument('id', type=str, help='句表的ID')
        parser.add_argument('hanji', type=str, help='漢字')
        parser.add_argument('sinTong', type=str, help='新的音檔所在')

    def handle(self, *args, **options):
        更新音檔所在(options['id'], options['hanji'], options['sinTong'])


def 更新音檔所在(id, 漢字, 新檔):
    這句 = 句表.objects.get(id=id, 漢字__startswith=漢字)
    這句.音檔=新檔
    這句.save()
