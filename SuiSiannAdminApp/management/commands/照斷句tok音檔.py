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
        besaih = []
        esaih = []
        for 句 in 句表.objects.all():
            if len(句.kaldi切音時間) <= 1:
                continue
            wav, sample_rate = librosa.load(
                句.音檔檔案, sr=None,
            )
            punte_usiann = []
            for thau, bue in librosa.effects.split(
                wav, top_db=options['threshold_db'],
                frame_length=2048, hop_length=512,
            ):
                punte_usiann.append(
                    (thau / sample_rate, bue / sample_rate)
                )

            usiann = []
            for thau, bue in 句.kaldi切音時間:
                khi = 0
                suah = 句.kaldi切音時間[-1][-1]
                for pun_thau, pun_bue in punte_usiann:
                    if pun_bue <= thau:
                        khi = pun_bue
                    if pun_thau >= bue:
                        suah = pun_thau
                        break
                usiann.append(
                    (khi, suah)
                )
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
                if (
                    (tsing and tsing[1] == kati[0])
                    or (au and au[0] == kati[1])
                ):
                    besaih.append(句.id)
                else:
                    esaih.append(句.id)
                    # print(usiann)
                    # raise RuntimeError('!!')
                tok.append((thau, bue))
            if 句.id == 1737:
                print(句.id)
                print('句.kaldi切音時間', 句.kaldi切音時間)
                print('punte_usiann', punte_usiann)
                print('usiann', usiann)
                print('tok', tok)

            longtsong += 1
        print(longtsong, len(besaih), len(esaih))
