from django.core.management.base import BaseCommand
from SuiSiannAdminApp.models import 句表
import librosa


class Command(BaseCommand):
    help = '''(oo)kā 2句以上ê音檔tok--開，參考
        https://gist.github.com/keithito/771cfc1a1ab69d1957914e377e65b6bd
    '''

    def add_arguments(self, parser):
        parser.add_argument('--min_duration', type=float, default=1.0, help='In seconds')
        parser.add_argument('--max_duration', type=float, default=10.0, help='In seconds')
        parser.add_argument('--max_gap_duration', type=float, default=0.75, help='In seconds')
        parser.add_argument('--threshold', type=float, default=40.0, help='In decibels below max')

    def handle(self, *args, **options):
        for 句 in 句表.objects.all():
            if len(句.kaldi切音時間) <= 1:
                continue
            print(句.id, 句.kaldi切音時間)
            wav, sample_rate = librosa.load(句.音檔所在)
            parts = librosa.effects.split(
                wav, top_db=options['threshold_db'],
                frame_length=1024, hop_length=256,
            )
            print(parts)
