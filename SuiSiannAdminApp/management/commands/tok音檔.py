from itertools import zip_longest
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
        max_gap_duration = options['max_gap_duration']
        gap_thè = max_gap_duration * 0.2
        longtsong = 0
        besaih = set()
        for 句 in 句表.objects.all():
            if len(句.kaldi切音時間) <= 1:
                continue
            usiann = []
            print(句.id)
            for thau, bue in 句.kaldi切音時間:
                wav, sample_rate = librosa.load(
                    句.音檔檔案, sr=None,
                    offset=thau, duration=bue - thau
                )
                parts = librosa.effects.split(
                    wav, top_db=options['threshold_db'],
                    frame_length=2048, hop_length=512,
                )
                # print('parts', parts)
                usiann.append((
                    thau + parts[0][0] / sample_rate,
                    thau + parts[-1][1] / sample_rate
                ))
            tok = []
            for tsing, kati, au in zip_longest(
                [None] + usiann[:-1], usiann, usiann[1:]
            ):
                if tsing:
                    thau = tsing[1] + gap_thè
                else:
                    thau = kati[0]
                if au:
                    bue = au[0] - gap_thè
                else:
                    bue = kati[1]
                if thau > kati[0] or bue < kati[1]:
                    besaih.add(句.id)
                    continue
                    # print(句.kaldi切音時間)
                    # print(usiann)
                    # raise RuntimeError('!!')
                tok.append((thau, bue))
            longtsong += 1
            print(tok)
        print(longtsong, len(besaih))
