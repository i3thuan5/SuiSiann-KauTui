import os


#
# 巡音檔佇咧的資料夾
#
def 記音檔所在():
    print('記音檔所在...')
    目錄根 = "./wavs/"#"/home/tia/Dropbox/母語/語料/TTS 語音合成錄製"
    結果 = dict()
    for kin, dirs, files in os.walk(目錄根):
        for name in files:
            if '.wav' in name:
                if name in 結果:
                    raise RuntimeError(name)
                結果[name] = os.path.join(kin, name)
    
    return 結果
    

音檔所在表 = 記音檔所在()