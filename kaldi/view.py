import io

from os.path import join
from subprocess import Popen, PIPE
from tempfile import TemporaryDirectory

from SuiSiannAdminApp.models import 句表
from django.http.response import JsonResponse
from ranged_response import RangedFileResponse


from 臺灣言語工具.系統整合.程式腳本 import 程式腳本


def kiamtsa(request, kuid):
    kaldi切音時間 = 句表.objects.get(id=kuid).重斷句()
    return JsonResponse({
        'Tsîng-hîng': 'Hó--ah~',
        'kaldi切音時間': kaldi切音時間,
    })


def 傳音檔(request, 音檔編號, 開始時間, 結束時間):
    全部音檔 = 句表.objects.get(id=音檔編號).聲音檔()
    語句音檔 = 全部音檔.照秒數切出音檔(float(開始時間), float(結束時間))
    try:
        with TemporaryDirectory() as 資料夾:
            檔名 = join(資料夾, 'audio.wav')
            with open(檔名, 'wb') as 檔案:
                指令 = Popen([
                    'sox', '-',
                    '-b', '24',
                    檔名,
                    'remix', '1',
                    'silence', '1', '0.01', '-40db', 'reverse',
                    'silence', '1', '0.01', '-40db', 'reverse',
                ], stdin=PIPE)
                指令.communicate(input=語句音檔.wav格式資料())
            程式腳本._走指令(['normalize-audio', 檔名])
            with open(檔名, 'rb') as 檔案:
                資料 = 檔案.read()
    except RuntimeError:
        資料 = 語句音檔.wav格式資料()
    return RangedFileResponse(
        request,
        io.BytesIO(資料),
        content_type="audio/wav"
    )
