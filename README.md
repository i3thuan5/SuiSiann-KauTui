# SuiSiann-Kautui
台灣媠聲校對

## 設定音檔
```bash
ln -s '.../Dropbox/語料/TTS 語音合成錄製' wavs
```

## Pī-hūn
```
docker-compose exec -T postgres pg_dump -U postgres | gzip > 20210514.sql.gz
zcat 20210514.sql.gz | docker-compose exec -T postgres psql -U postgres
```
