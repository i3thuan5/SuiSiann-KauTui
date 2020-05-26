
from SuiSiannAdminApp.models import 句表
from django.core.management.base import BaseCommand


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('tongan',)

    def handle(self, *args, **options):
        with open(options['tongan'], 'wt', encoding='utf-8') as tong:
            for _kui, 句 in enumerate(
                句表.objects
                .order_by('來源_id', 'id').select_related('來源'),
                start=1,
            ):
                print(
                    拆文分析器.建立句物件(
                        句.漢字.replace('\n', ' '), 句.羅馬字.replace('\n', ' ')
                    ).看分詞(),
                    file=tong
                )
