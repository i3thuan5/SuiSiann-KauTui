# Generated by Django 4.1.5 on 2023-05-23 12:48
import json
from os.path import dirname, join
from django.db import migrations


def 設定S3音檔(apps, schema_editor):
    with open(join(
        dirname(__file__), '..', 'management', 'sootsai.json')
    ) as tong:
        pio = json.load(tong)
    句表 = apps.get_model('SuiSiannAdminApp', '句表')
    for ku in 句表.objects.all().order_by('id'):
        ku.S3音檔 = pio[ku.音檔.name]
        ku.save()


class Migration(migrations.Migration):

    dependencies = [
        ('SuiSiannAdminApp', '0018_句表_s3音檔'),
    ]

    operations = [
        migrations.RunPython(設定S3音檔, lambda *x: x),
    ]
