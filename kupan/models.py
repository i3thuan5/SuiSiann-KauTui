from django.db import models
from django.contrib.auth.models import User
from phiaua.clean import clean_html, get_lomaji
from SuiSiannAdminApp.management.檢查對齊狀態 import 檢查對齊狀態


class Le(models.Model):
    音檔 = models.FileField(editable=False)
    漢字 = models.TextField()
    羅馬字含口語調 = models.TextField()
    羅馬字 = models.TextField(editable=False)
    修改時間 = models.DateTimeField(auto_now=True)
    修改人 = models.ForeignKey(
        User, editable=False, null=True,
        on_delete=models.PROTECT,
    )
    對齊狀態 = models.CharField(blank=True, max_length=200, default="-")
    tó一款句辦 = models.ManyToManyField('Khuán', blank=True)
    校對狀況 = models.ManyToManyField('Tsònghóng', blank=True)
    備註 = models.TextField(blank=True)

    def clean(self):
        sin_html = clean_html(self.羅馬字含口語調)
        self.羅馬字含口語調 = str(sin_html)
        self.羅馬字 = get_lomaji(sin_html)
        self.對齊狀態 = 檢查對齊狀態(self.漢字, self.羅馬字, sin_html)

    def __str__(self):
        return '{} {}'.format(self.pk, self.漢字)

    @property
    def 音檔檔案(self):
        return self.音檔.path

    @property
    def 音檔網址(self):
        return self.音檔.url

    class Meta:
        verbose_name = "Le"
        verbose_name_plural = verbose_name


class Khuán(models.Model):
    miâ = models.CharField(unique=True, max_length=50)


class Tsònghóng(models.Model):
    miâ = models.CharField(unique=True, max_length=50)
