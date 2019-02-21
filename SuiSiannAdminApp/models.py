from django.db import models
from kaldi.liansuann import tuìtsê
from SuiSiannAdminApp.management.檢查對齊狀態 import 檢查對齊狀態
from SuiSiannAdminApp.management.算音檔網址 import 音檔網址表


class 文章表(models.Model):
    文章名 = models.TextField(max_length=30, unique=True)

    def __str__(self):
        return self.文章名

    class Meta:
        verbose_name = "文章表"
        verbose_name_plural = verbose_name


class 句表(models.Model):
    來源 = models.ForeignKey(文章表, null=True,
                           related_name='+', on_delete=models.CASCADE)
    音檔 = models.FileField(blank=True)
    原始漢字 = models.CharField(max_length=500)
    原始臺羅 = models.CharField(max_length=2000)
    漢字 = models.CharField(max_length=500)
    臺羅 = models.CharField(max_length=2000)
    修改時間 = models.DateTimeField(null=True)
    對齊狀態 = models.CharField(blank=True, max_length=200, default="-")
    備註 = models.TextField(blank=True,)
    語料狀況 = models.ManyToManyField('語料狀況表', blank=True)

    def __str__(self):
        return '{}{}'.format(self.pk, self.漢字)

    def save(self, *args, **kwargs):
        self.對齊狀態 = 檢查對齊狀態(self.漢字, self.臺羅)
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def kaldi_tuìtsê(self):
        return tuìtsê(音檔網址表[self.音檔][6:], self.臺羅.split('\n'))

    class Meta:
        verbose_name = "句表"
        verbose_name_plural = verbose_name


class 語料狀況表(models.Model):
    狀況 = models.CharField(unique=True, max_length=30)

    class Meta:
        verbose_name = "語料狀況表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{} {}'.format(self.pk, self.狀況)
