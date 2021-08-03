from os.path import join

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from kaldi.liansuann import tuìtsê
from jsonfield.fields import JSONField
from bs4 import BeautifulSoup
from kesi.butkian.kongiong import si_lomaji


from SuiSiannAdminApp.management.檢查對齊狀態 import 檢查對齊狀態
from SuiSiannAdminApp.management.算音檔網址 import 算音檔所在
from 臺灣言語工具.語音辨識.聲音檔 import 聲音檔
from kaldi.lib.換算切音所在 import 換算切音所在
from 臺灣言語工具.基本物件.公用變數 import 標點符號


class 文章表(models.Model):
    文章名 = models.TextField(max_length=30, unique=True)

    def __str__(self):
        return self.文章名

    class Meta:
        verbose_name = "文章表"
        verbose_name_plural = verbose_name


class 句表(models.Model):
    來源 = models.ForeignKey(
        文章表, editable=False,
        related_name='句', on_delete=models.PROTECT
    )
    音檔 = models.FileField(editable=False)
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

    @staticmethod
    def clean_html(khaugi_html):
        parser = BeautifulSoup(khaugi_html, 'html.parser')
        p = parser.find('p')
        sin_html = BeautifulSoup('<p></p>', 'html.parser')
        for i, phiau in enumerate(p.contents):
            phiau_tag = phiau.extract()
            # 這个content是純文字
            if phiau_tag.name is None:
                sin_html.p.append(phiau_tag)
            else:
                lui = phiau_tag['class']
                tag = None
                for jiguan in phiau_tag.string:
                    if si_lomaji(jiguan):
                        if tag is None:
                            tag = sin_html.new_tag('span', attrs={'class': lui})
                            tag.string = ''
                        tag.string += jiguan
                    else:
                        if tag is not None:
                            sin_html.p.append(tag)
                        sin_html.p.append(jiguan)
                        tag = sin_html.new_tag('span', attrs={'class': lui})
                        tag.string = ''
                if tag.string:
                    sin_html.p.append(tag)

        return sin_html

    def clean(self):
        self.羅馬字 = BeautifulSoup(self.羅馬字含口語調, 'html.parser').get_text()
        self.對齊狀態 = 檢查對齊狀態(self.漢字, self.羅馬字)

    def __str__(self):
        return '{} {}'.format(self.pk, self.漢字)

    def 重對齊(self):
        self.kaldi切音時間 = self.kaldi_tuìtsê()
        self.save()
        return self.kaldi切音時間

    def kaldi切音時間網址(self):
        for thau, bue in 換算切音所在(self.聲音檔().時間長度(), self.kaldi切音時間):
            yield reverse('imtong', args=(self.id, thau, bue))

    def kaldi_tuìtsê(self):
        piautiam = ''.join(標點符號)
        lmj = []
        for tsua in self.羅馬字.split('\n'):
            lmj.append(tsua.strip().strip(piautiam))
        return tuìtsê(self.音檔所在, lmj)

    def 聲音檔(self):
        return 聲音檔.對檔案讀(self.音檔檔案)

    @property
    def 音檔所在(self):
        return self.音檔所在表[self.音檔]

    @property
    def 音檔檔案(self):
        return join(settings.MEDIA_ROOT, self.音檔所在)

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
