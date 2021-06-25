# SuiSiann-Kautui
台灣媠聲校對

## Pī-hūn
```
docker-compose exec -T postgres pg_dump -U postgres | gzip > 20210514.sql.gz
zcat 20210514.sql.gz | docker-compose exec -T postgres psql -U postgres
```
