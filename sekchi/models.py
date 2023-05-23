from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from tuitse import kiamtsa

from os.path import relpath
from urllib.parse import urljoin
from storages.backends.s3boto3 import S3Boto3Storage

from phiaua.clean import clean_html, get_lomaji
from SuiSiannAdminApp.management.檢查對齊狀態 import 檢查對齊狀態


def siktsi_path():
    return settings.SIKTSI_ROOT


class KuStorage(S3Boto3Storage):
    bucket_name = 'suisiann-kautui'
    location = '汐止媠聲'


class Sekchi(models.Model):
    音檔所在 = models.FilePathField(
        match='.*.wav',
        unique=True,
        path=siktsi_path,
        # recursive是Form選擇時用--ê
        # https://github.com/django/django/blob/
        # 0dd29209091280ccf34e07c9468746c396b7778e/
        # django/forms/fields.py#L1205
        recursive=False,
        allow_files=True,
        allow_folders=False,
        max_length=1000,
    )
    S3音檔 = models.FileField(storage=KuStorage(), editable=False)
    漢字 = models.TextField()
    羅馬字含口語調 = models.TextField()
    羅馬字 = models.TextField(editable=False)
    來源 = models.CharField(max_length=50, db_index=True)
    part = models.CharField(max_length=5, db_index=True)
    編號 = models.CharField(max_length=10, db_index=True)
    修改時間 = models.DateTimeField(auto_now=True)
    修改人 = models.ForeignKey(
        User, editable=False, null=True,
        on_delete=models.PROTECT,
    )
    備註 = models.TextField(blank=True)
    校對狀況 = models.ManyToManyField('Tsònghóng', blank=True)
    對齊狀態 = models.BooleanField()
    口語調狀態 = models.TextField(editable=False)

    class Meta:
        verbose_name = "汐止腔語料"
        verbose_name_plural = verbose_name

    def 音檔網址(self):
        return KuStorage().url(
            relpath(self.音檔所在, settings.SIKTSI_ROOT),
        )

    def clean(self):
        self.羅馬字含口語調 = clean_html(self.羅馬字含口語調)
        self.羅馬字 = get_lomaji(self.羅馬字含口語調)
        self.口語調狀態 = 檢查對齊狀態(self.漢字, self.羅馬字, self.羅馬字含口語調)

    def save(self, *args, **kwargs):
        kiatko = kiamtsa(self.漢字, self.羅馬字)
        self.對齊狀態 = all(map(lambda x: x[3], kiatko))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.漢字


class Tsònghóng(models.Model):
    miâ = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return '{} {}'.format(self.id, self.miâ)

    class Meta:
        verbose_name = "Tsònghóng"
        verbose_name_plural = verbose_name
