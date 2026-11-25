
from SuiSiannAdminApp.models import 句表
from django.core.management.base import BaseCommand


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class Command(BaseCommand):
    ithuan = [
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10,
        11, 12, 13,
        17, 18,
        30,
        50, 51, 52, 53, 54, 55, 56,
    ]

    def add_arguments(self, parser):
        parser.add_argument('tongan',)
        hue = parser.add_mutually_exclusive_group(required=True)
        hue.add_argument(
            '--tsuanpoo', action='store_true', help='匯出全部語句',
        )
        hue.add_argument(
            '--ithuan', action='store_true', help='Kan-na匯出意傳ê語句',
        )

    def handle(self, *args, **options):
        if options['tsuanpoo']:
            語句 = 句表.objects.all()
        elif options['ithuan']:
            語句 = 句表.objects.filter(來源_id__in=self.ithuan)
        with open(options['tongan'], 'wt', encoding='utf-8') as tong:
            for 句 in (
                語句.order_by('來源_id', 'id').select_related('來源')
            ):
                print(
                    拆文分析器.建立句物件(
                        句.漢字.replace('\n', ' '), 句.羅馬字.replace('\n', ' ')
                    ).看分詞(),
                    file=tong
                )
