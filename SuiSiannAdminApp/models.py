from os.path import join
from storages.backends.s3boto3 import S3Boto3Storage

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from kaldi.tuitse import tngku
from jsonfield.fields import JSONField

from kesi import Ku

from SuiSiannAdminApp.management.檢查對齊狀態 import 檢查對齊狀態
from SuiSiannAdminApp.management.算音檔網址 import 算音檔所在
from phiaua.clean import clean_html, get_lomaji
from 臺灣言語工具.語音辨識.聲音檔 import 聲音檔
from 臺灣言語工具.基本物件.公用變數 import 標點符號


class 文章表(models.Model):
    文章名 = models.TextField(max_length=30, unique=True)

    def __str__(self):
        return self.文章名

    class Meta:
        verbose_name = "文章表"
        verbose_name_plural = verbose_name


class KuStorage(S3Boto3Storage):
    bucket_name = 'suisiann-kautui'
    location = '台灣媠聲'


class 句表(models.Model):
    來源 = models.ForeignKey(
        文章表, editable=False,
        related_name='句', on_delete=models.PROTECT
    )
    音檔 = models.FileField(editable=False)
    S3音檔 = models.FileField(storage=KuStorage(), editable=False, null=True)
    原始漢字 = models.TextField(editable=False)
    原始羅馬字 = models.TextField(editable=False)
    漢字 = models.TextField()
    羅馬字含口語調 = models.TextField()
    羅馬字 = models.TextField(editable=False)
    修改時間 = models.DateTimeField(editable=False, null=True)
    修改人 = models.ForeignKey(
        User, editable=False, null=True,
        on_delete=models.PROTECT,
    )
    對齊狀態 = models.CharField(blank=True, max_length=200, default="-")
    備註 = models.TextField(blank=True)
    語料狀況 = models.ManyToManyField('語料狀況表', blank=True)
    kaldi切音時間 = JSONField(editable=False, default=[])

    音檔所在表 = 算音檔所在()

    def clean(self):
        self.羅馬字含口語調 = clean_html(self.羅馬字含口語調)
        self.羅馬字 = get_lomaji(self.羅馬字含口語調)
        self.對齊狀態 = 檢查對齊狀態(self.漢字, self.羅馬字, self.羅馬字含口語調)

    def __str__(self):
        return '{} {}'.format(self.pk, self.漢字)

    def 重斷句(self):
        lomaji = []
        for tsua in self.羅馬字.split('\n'):
            su_tsua = []
            for su in Ku(tsua):
                if su.lomaji not in 標點符號:
                    su_tsua.append(su.lomaji)
            lomaji.append(' '.join(su_tsua))
        self.kaldi切音時間 = tngku(lomaji, self.音檔檔案, self.音檔所在)
        self.save()
        return self.kaldi切音時間

    def kaldi切音時間網址(self):
        for thau, bue in self.斷句時間:
            yield reverse('imtong', args=(self.id, thau, bue))

    def 聲音檔(self):
        return 聲音檔.對檔案讀(self.音檔檔案)

    @property
    def 音檔所在(self):
        return self.音檔所在表[self.音檔]

    @property
    def 音檔檔案(self):
        return join(settings.SUISIANN_ROOT, self.音檔所在)

    @property
    def 音檔網址(self):
        return reverse('imtong', args=(self.id, 0, self.聲音檔().時間長度()))

    class Meta:
        verbose_name = "句表"
        verbose_name_plural = verbose_name
        constraints = [
            models.UniqueConstraint(
                fields=['音檔'], condition=~models.Q(音檔=''), name='imtong_bokang'
            ),
        ]


class 語料狀況表(models.Model):
    狀況 = models.CharField(unique=True, max_length=30)

    class Meta:
        verbose_name = "語料狀況表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{} {}'.format(self.pk, self.狀況)
