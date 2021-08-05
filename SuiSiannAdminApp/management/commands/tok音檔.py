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
        parser.add_argument('--threshold_db', type=float, default=40.0, help='In decibels below max')

    def handle(self, *args, **options):
        longtsong = 0
        for 句 in 句表.objects.all():
            if len(句.kaldi切音時間) <= 1:
                continue
            wav, sample_rate = librosa.load(句.音檔檔案, sr=None)
            parts = librosa.effects.split(
                wav, top_db=options['threshold_db'],
                frame_length=1024, hop_length=256,
            )
            siunn_làng = False
            for tsing, au in zip(parts[:-1], parts[1:]):
                if (au[0] - tsing[1]) / sample_rate > options['max_gap_duration']:
                    siunn_làng = True
            if siunn_làng:
                longtsong += 1
                print(句.id, 句.kaldi切音時間, sample_rate)
                # print(parts)
                # return
        print(longtsong)
