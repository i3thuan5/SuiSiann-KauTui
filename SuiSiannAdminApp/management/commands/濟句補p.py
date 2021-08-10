from django.core.management.base import BaseCommand
from SuiSiannAdminApp.models import 句表


class Command(BaseCommand):

    def handle(self, *args, **options):
        longtsong = 0
        for mih in (
            句表.objects
            .filter(羅馬字='lomaji')
            .exclude(羅馬字含口語調__contains='<p>')
        ):
            if len(mih.kaldi切音時間) > 1:
                longtsong += 1
                mih.羅馬字含口語調 = '<p>{}</p>'.format(
                    '</p><p>'.join(mih.羅馬字含口語調.split('\n'))
                )
                mih.save()
        print('Lóng-tsóng {} kù.'.format(longtsong))
