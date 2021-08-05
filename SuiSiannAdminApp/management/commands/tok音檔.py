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
        esaih = set()
        besaih = set()
        bun = {}
        for 句 in 句表.objects.select_related('來源').all():
            if len(句.kaldi切音時間) <= 1:
                continue
            wav, sample_rate = librosa.load(句.音檔檔案, sr=None)
            parts = librosa.effects.split(
                wav, top_db=options['threshold_db'],
                frame_length=2048, hop_length=512,
            )
            siunn_làng = False
            tsitma = 0
            tok = []
            for tsing, au in zip(parts[:-1], parts[1:]):
                if (au[0] - tsing[1]) / sample_rate > max_gap_duration:
                    siunn_làng = True
                    tok.append((
                        tsitma,
                        au[0] / sample_rate - gap_thè
                    ))
                    tsitma = tsing[1] / sample_rate + gap_thè
            if siunn_làng:
                tok.append((tsitma, len(wav) / sample_rate))
                longtsong += 1
                # print(句.id, sample_rate)
                # print(句.kaldi切音時間)
                # print(parts)
                # print(tok)
                # return
                esaih.add(句.id)
                try:
                    bun[句.來源]+=1
                except:
                    bun[句.來源]=1
            else:
                besaih.add(句.id)
                print(句.id)
        print(longtsong, 2168 in besaih, 2168 in esaih)
        print('bun', len(bun), bun)
