# SuiSiann-Kautui
台灣媠聲校對
語料庫：https://suisiann-dataset.ithuan.tw/
校對原則：https://hackmd.ithuan.tw/@fFPu4cAQSSC7Ln4qB2xJQg/ByxRAxcjCd


## 設定音檔
```bash
ln -s '.../Dropbox/Gí-liāu/台灣媠聲——TTS 語音合成錄製/' 台灣媠聲
ln -s '.../Dropbox/Gí-liāu/汐止媠聲——TTS 語音合成錄製/' 汐止媠聲
```

## Dependencies

`sudo apt-get install normalize-audio sox`

若是出現錯誤訊息：
```
FileNotFoundError: 檔案無存在，抑是指令參數愛用陣列的形式！！指令：['normalize-audio', '/tmp/tmpq_h7677d/audio.wav']
```
就是表示無tàu著需要ê套件。


## 更新套件版本

1. 手動更新`requirements.in`。
2. Tàu [Pip-tools](https://github.com/jazzband/pip-tools) Python管理套件版本套件.
```
pip install pip-tools
```
3. `pip-compile`自動更新套件版本。
```bash
# 有必要--ê才更新
pip-compile
# 盡量更新
pip-compile --upgrade
````

## Pī-hūn
```
docker-compose exec -T postgres pg_dump -U postgres | gzip > 20210514.sql.gz
zcat 20210514.sql.gz | docker-compose exec -T postgres psql -U postgres
```
