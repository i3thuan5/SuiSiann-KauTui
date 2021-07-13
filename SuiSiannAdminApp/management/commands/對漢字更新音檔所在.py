from django.core.management.base import BaseCommand
from SuiSiannAdminApp.models import 句表


class Command(BaseCommand):
    help = '輸入漢字，更新這句佇資料庫內底的音檔所在'

    def add_arguments(self, parser):
        parser.add_argument('h', type=str, help='漢字相仝的句')
        parser.add_argument('l', type=str, help='臺羅相仝的句')
        parser.add_argument('m', type=str, help='新的音檔所在')

    def handle(self, *args, **options):
        對漢字更新音檔所在(options['h'], options['l'], options['m'])


def 對漢字更新音檔所在(揣的漢字, 揣的臺羅, 新的音檔):
    更新的句 = 句表.objects.select_for_update().get(漢字=揣的漢字, 羅馬字=揣的臺羅)
    更新的句.音檔 = 新的音檔
    更新的句.save()
    print('這句更新音檔矣：', 更新的句)
