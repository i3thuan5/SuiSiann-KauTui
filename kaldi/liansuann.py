import http
from http.client import HTTPConnection
import json
from urllib.parse import quote, urlencode


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
    it_conn = HTTPConnection('tuitse-it', port=5000)
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
    for tsua in sikan:
        ku = tsua.split()
        ku[2] = float(ku[2]) * frame_subsampling_factor
        ku[3] = float(ku[3]) * frame_subsampling_factor
        kiatko.append(ku)
        print(' '.join(ku))
    return kiatko
