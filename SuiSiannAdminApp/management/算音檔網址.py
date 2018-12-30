import os
from django.conf import settings


#
# 存音檔名->音檔網址的對應表
#
def 算音檔網址():
    print('算音檔網址...')
    目錄根 = settings.MEDIA_ROOT
    結果 = dict()
    for 這馬層, dirs, files in os.walk(目錄根):
        # 迒過
        欲迒過的資料kiap = ['討論', '錯誤']
        if os.path.basename(這馬層) in 欲迒過的資料kiap:
            continue
        # 吐音檔名
        for name in files:
            if '.wav' in name:
                # 檔名重複
                if name in 結果:
                    raise RuntimeError('音檔重複出現：{}/{}'.format(這馬層, name))
                # http://localhost:8000/wavs/Oct 20, 2018/圓仔的神仙/Oct 20, 2018
                # _37_inn.wav
                結果[name] = os.path.join(
                    settings.MEDIA_URL, os.path.relpath(這馬層, 目錄根), name)
    return 結果


音檔網址表 = 算音檔網址()
