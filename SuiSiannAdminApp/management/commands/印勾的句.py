from SuiSiannAdminApp.models import 句表
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    HTMLTemplate = """<!DOCTYPE html><html>
            <head>
            <meta charset="utf-8"/>
            <title>Un2-gian5 lun5-bun5</title>
            <style>
            p {{font-family:"WenQuanYi Micro Hei"}}
            .tua7 {{font-size:13pt; font-weight:"bold"}}
            .se3 {{font-size:10pt;}}
            </style>
            </head>
            <body>{}</body>
        </html>"""

    def add_arguments(self, parser):
        parser.add_argument('勾碼',)

    def handle(self, *args, **options):
        勾的號碼 = options['勾碼']

        結果 = 句表.objects.filter(語料狀況=勾的號碼).values('id', '漢字', '臺羅', '備註')

        html = ""
        for item in 結果:
            html += (
                "<p class='tua7'>{}</p>".format(item['漢字'])
                + "<p class='se3'>{}</p>".format(item['臺羅'])
                + "<p class='se3'>理由：{}（編號{}）</p>".format(
                    item['備註'], item['id'])
                + "<br/>"
            )

        with open('印勾的句.html', 'w') as html_tong2:
            print(self.HTMLTemplate.format(html), file=html_tong2)
