import http
import json
from urllib.parse import quote

from SuiSiannAdminApp.models import 句表
from django.http.response import JsonResponse


from SuiSiannAdminApp.management.算音檔網址 import 音檔網址表
from 臺灣言語工具.基本物件.公用變數 import 標點符號
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


def kiamtsa(request, kuid):
    ku = 句表.objects.get(id=kuid)
    han = []
    for ji in 拆文分析器.建立句物件(ku.漢字).篩出字物件():
        if ji not in 標點符號:
            han.append(ji.型)
    tong = 音檔網址表[ku.音檔][6:]
    conn = http.client.HTTPConnection("it", port=5000)
    conn.request("GET", quote("/{}/{}".format(' '.join(han), tong)))
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    a = r1.read()
    print(a)
    data1 = json.loads(a)  # This will return entire content.
    conn = http.client.HTTPConnection("ji", port=5000)
    conn.request("GET", data1)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    r1.read()  # This will return entire content.
    conn = http.client.HTTPConnection("sann", port=5000)
    conn.request("GET", data1)
    r3 = conn.getresponse()
    print(r3.status, r3.reason)
    data3 = json.loads(r3.read())  # This will return entire content.
    print(data3)
    return JsonResponse({'LMJ': data3})
