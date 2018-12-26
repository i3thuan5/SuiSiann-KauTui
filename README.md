# Sui-Siann-Dataset
臺語媠聲錄音檔 

## 將csv匯入django admin
```
python manage.py 匯入csv --csv csv/賣圓仔的神仙_hanlo.odt.csv
```

## Autopep8 reformat
```
autopep8 -r --in-place --aggressive --exclude=venv,__pycache__,.git,csv ./
```

## 開發
```
bash 批次錄音稿odt轉csv.sh 
```
進前為著管理錄音，逐擺的錄音稿攏有家己的資料kiap。
這个程式會去揣錄音稿的資料kiap，將 in 轉做`.csv`囥佇`csv/`。

