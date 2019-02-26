from os.path import join, relpath

from django.conf import settings
from django.db import models
from kaldi.liansuann import tuìtsê
from jsonfield.fields import JSONField


from SuiSiannAdminApp.management.檢查對齊狀態 import 檢查對齊狀態
from SuiSiannAdminApp.management.算音檔網址 import 音檔網址表
from 臺灣言語工具.語音辨識.聲音檔 import 聲音檔
from kaldi.lib.換算切音所在 import 換算切音所在


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
    kaldi切音時間 = JSONField(default=[])

    @property
    def 羅馬字(self):
        return self.臺羅

    @羅馬字.setter
    def 羅馬字(self, value):
        self.臺羅 = value

    @property
    def 原始羅馬字(self):
        return self.原始臺羅

    @原始羅馬字.setter
    def 原始羅馬字(self, value):
        self.原始臺羅 = value

    def __str__(self):
        return '{}{}'.format(self.pk, self.漢字)

    def save(self, *args, **kwargs):
        self.對齊狀態 = 檢查對齊狀態(self.漢字, self.臺羅)
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def 重對齊(self):
        tuitse = self.kaldi_tuìtsê()
        self.kaldi切音時間 = 換算切音所在(self.聲音檔().時間長度(), tuitse)
        self.save()
        return tuitse, self.kaldi切音時間

    def kaldi切音時間網址(self):
        for kui, (thau, bue) in enumerate(self.kaldi切音時間, start=1):
            yield (kui, '/音檔/{}/{}/{}/audio.wav'.format(self.id, thau, bue),)

    def kaldi_tuìtsê(self):
        return tuìtsê(relpath(音檔網址表[self.音檔], settings.MEDIA_URL), self.臺羅.split('\n'))

    def 聲音檔(self):
        return 聲音檔.對檔案讀(
            join(settings.MEDIA_ROOT, relpath(
                音檔網址表[self.音檔], settings.MEDIA_URL))
        )

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
