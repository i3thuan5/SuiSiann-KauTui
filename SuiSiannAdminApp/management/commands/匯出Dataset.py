from csv import DictWriter
from os import makedirs
from os.path import join
import json

from SuiSiannAdminApp.models import 句表
from django.core.management.base import BaseCommand
from librosa.core.audio import get_duration
from subprocess import run
from phiaua.hue import hue_tacotron

from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


class Command(BaseCommand):
    tongmia = 'ImTong/SuiSiann_{:04}.wav'
    # https://gist.github.com/keithito/771cfc1a1ab69d1957914e377e65b6bd#file-segment-py-L147-L149
    max_duration = 10.0
    max_gap_duration = 0.75
    threshold = 40.0

    def add_arguments(self, parser):
        parser.add_argument('TsuLiauGiap',)
        parser.add_argument(
            '--mai_imtong', action="store_true",
            help='Mài輸出音檔，beh看統計niâ。',
        )

    def handle(self, *args, **options):
        ai_imtong = not options['mai_imtong']
        makedirs(join(options['TsuLiauGiap'], 'ImTong'))
        csvtongmia = join(options['TsuLiauGiap'], 'SuiSiann.csv')
        lmjtongmia = join(options['TsuLiauGiap'], 'lmj.json')

        with open(csvtongmia, 'wt', encoding='utf-8') as tong:
            sia = DictWriter(tong, fieldnames=[
                '音檔',
                '來源',
                '漢字',
                '羅馬字', '口語調',
                '長短',
            ])
            sia.writeheader()
            kui = 1
            bio = 0.0
            lts = 0.0
            su_soo = 0
            ji_soo = 0
            lmj = set()
            siannun = set()
            for kui, 句 in enumerate(
                句表.objects.order_by('來源_id', 'id').select_related('來源')
            ):
                if len(句.kaldi切音時間) > 1:
                    print('有音檔á-bē tok開！')
                    continue
                原始音檔 = 句.音檔檔案
                ku_tngte = get_duration(filename=原始音檔)
                lts += ku_tngte
                wavtongmia = self.tongmia.format(kui)
                句物件 = 拆文分析器.建立句物件(句.漢字, 句.羅馬字)
                su_soo += len(句物件.網出詞物件())
                ji_soo += len(句物件.篩出字物件())

                for 字物件 in 句物件.篩出字物件():
                    字物件.音 = 字物件.音.lstrip('-').lower()
                    if not 字物件.敢是標點符號() and 字物件.音標敢著(臺灣閩南語羅馬字拼音):
                        lmj.add(字物件.看音())
                        siannun.add(
                            字物件.轉音(臺灣閩南語羅馬字拼音)
                            .看音().rstrip('0987654321')
                        )
                    sia.writerow({
                        '音檔': wavtongmia,
                        '來源': 句.來源.文章名,
                        '漢字': 句.漢字,
                        '羅馬字': 句.羅馬字,
                        '口語調': hue_tacotron(句.羅馬字含口語調),
                        '長短': '{:.2f}'.format(ku_tngte),
                    })
                    kiatko_mia = join(options['TsuLiauGiap'], wavtongmia)
                    if ai_imtong:
                        run(
                            [
                                'sox', 原始音檔, kiatko_mia,
                            ],
                            check=True,
                        )
                    print(
                        (
                            '結果粒積秒數：{:.2f} 本底音檔秒數：{:.2f}\n'
                            '總詞數：{} 總字數：{}\n'
                            '羅馬字種類（考慮書寫聲調，bô考慮輕聲、大小寫、變調類型）：{}\n'
                            '聲韻種類（bô考慮聲調、輕聲、大小寫）：{}\n'
                        ).format(bio, lts, su_soo, ji_soo, len(lmj), len(siannun)),
                        file=self.stderr
                    )
        with open(lmjtongmia, 'w') as tong:
            json.dump(
                {'羅馬字': sorted(lmj), '聲韻': sorted(siannun)},
                tong,
                ensure_ascii=False,
                sort_keys=True,
                indent=2,
            )
