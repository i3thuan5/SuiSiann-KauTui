# Generated by Django 4.1.5 on 2023-05-23 12:50

from django.db import migrations
from os.path import relpath
from django.conf import settings


def 設定S3音檔(apps, schema_editor):
    句表 = apps.get_model('sekchi', 'Sekchi')
    for ku in 句表.objects.all():
        ku.S3音檔 = relpath(ku.音檔所在, settings.SIKTSI_ROOT)
        ku.save()


class Migration(migrations.Migration):

    dependencies = [
        ('sekchi', '0010_alter_sekchi_修改時間'),
    ]

    operations = [
        migrations.RunPython(設定S3音檔, lambda *x: x),
    ]
