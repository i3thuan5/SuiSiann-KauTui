import http
import json
from urllib.parse import quote

from SuiSiannAdminApp.models import 句表
from django.http.response import JsonResponse


from SuiSiannAdminApp.management.算音檔網址 import 音檔網址表
from 臺灣言語工具.基本物件.公用變數 import 標點符號
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


'exp/chain/tdnn_1a_sp/frame_subsampling_factor'
frame_subsampling_factor = 3


def kiamtsa(request, kuid):
    ku = 句表.objects.get(id=kuid)
    kiatko = tuìtsê(音檔網址表[ku.音檔][6:], ku.臺羅.split('\n'))
    return JsonResponse({'LMJ': kiatko})


def tuìtsê(wavPath, taiBun):
    網址 = "/?taibun={}&wav={}".format(
        quote(json.dumps(taiBun)),
        quote(wavPath),
    )

    it_conn = http.client.HTTPConnection('it', port=5000)
    it_conn.request("GET", 網址)
    tmpPath = json.loads(it_conn.getresponse().read())
    print('it tmpPath', tmpPath)
    ji_conn = http.client.HTTPConnection('ji', port=5000)
    ji_conn.request("GET", tmpPath)
    print('ji',  json.loads(ji_conn.getresponse().read()))
    sam_conn = http.client.HTTPConnection("sam", port=5000)
    sam_conn.request("GET", tmpPath)
    sikan = json.loads(sam_conn.getresponse().read())
    print('sam', sikan)
    kiatko = []
    for tsua in sikan:
        ku = tsua.split()
        ku[2] = str(float(ku[2]) * frame_subsampling_factor)
        ku[3] = str(float(ku[3]) * frame_subsampling_factor)
        kiatko.append(ku)
        print(' '.join(ku))
    return kiatko
