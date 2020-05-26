from http.client import HTTPConnection
import json
from urllib.parse import urlencode


'exp/chain/tdnn_1a_sp/frame_subsampling_factor'
frame_subsampling_factor = 3


def tuìtsê(wavPath, taiBun):
    參數 = urlencode({
        'taibun': json.dumps(taiBun),
        'wav': (wavPath),
    })
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        "Accept": "text/plain"
    }
    it_conn = HTTPConnection('it', port=5000)
    it_conn.request("POST", '/', 參數, headers)
    tmpPath = json.loads(it_conn.getresponse().read())
    print('it tmpPath', tmpPath)
    ji_conn = HTTPConnection('ji', port=5000)
    ji_conn.request("GET", tmpPath)
    print('ji',  json.loads(ji_conn.getresponse().read()))
    sam_conn = HTTPConnection("sam", port=5000)
    sam_conn.request("GET", tmpPath)
    sikan = json.loads(sam_conn.getresponse().read())
    print('sam', sikan)
    kiatko = []
    for ku in 敆字做句(sikan):
        ku[2] = float(ku[2])
        ku[3] = float(ku[3])
        kiatko.append((ku[2], ku[2] + ku[3]))
    return kiatko


punkhui = '｜'


def 敆字做句(kaldi結果):
    kapho = []
    tingkuid = None
    tingku = None
    kukhaisi = None
    kukiatsok = None
    for tsua in kaldi結果:
        tongmia, channel, khaisi, tngtoo, lueiong = tsua.split()
        kuid, ku, *_ji = lueiong.split(punkhui, 2)
        if tingkuid != kuid:
            if tingkuid is not None:
                kapho.append([
                    tongmia, channel,
                    kukhaisi, '{:.3f}'.format(kukiatsok - float(kukhaisi)),
                    '{}{}{}'.format(tingkuid, punkhui, tingku)
                ])
            tingkuid = kuid
            tingku = ku
            kukhaisi = khaisi
        kukiatsok = float(khaisi) + float(tngtoo)
    if tingkuid is not None:
        kapho.append([
            tongmia, channel,
            kukhaisi, '{:.3f}'.format(kukiatsok - float(kukhaisi)),
            '{}{}{}'.format(kuid, punkhui, ku)
        ])
    return kapho
