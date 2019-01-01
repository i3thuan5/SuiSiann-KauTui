from urllib.parse import quote
import http
import json
from sys import stderr
from django.http.response import JsonResponse
def kiamtsa(request):
 conn = http.client.HTTPConnection("it",port=5000)
 han='坐 咧'
 tong='Nov 3, 2018/動詞/Nov 3, 2018.wav'
 conn.request("GET", quote("/{}/{}".format(han,tong)))
 r1 = conn.getresponse()
 print(r1.status, r1.reason)
 a=r1.read()
 print(a)
 data1 = json.loads(a)  # This will return entire content.
 print(data1,'data1')
 print(data1,'data1',file=stderr)
 conn = http.client.HTTPConnection("ji",port=5000)
 conn.request("GET", data1)
 r1 = conn.getresponse()
 print(r1.status, r1.reason)
 data2 = r1.read()  # This will return entire content.
 conn = http.client.HTTPConnection("sann",port=5000)
 conn.request("GET", data1)
 r3 = conn.getresponse()
 print(r3.status, r3.reason)
 data3 = json.loads(r3.read())  # This will return entire content.
 print(data3)
 return JsonResponse({'LMJ': data3})
