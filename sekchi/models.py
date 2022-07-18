from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from phiaua.clean import clean_html, get_lomaji


# Create your models here.
class Sekchi(models.Model):
    音檔所在 = models.FilePathField(
        match='.*.wav',
        unique=True,
        path=settings.SIKTSI_ROOT,
        recursive=True,
        allow_files=True,
        allow_folders=False,
        max_length=200,
    )
    漢字 = models.TextField()
    羅馬字含口語調 = models.TextField()
    羅馬字 = models.TextField(editable=False)
    part = models.CharField(max_length=5)
    編號 = models.CharField(max_length=10)
    修改時間 = models.DateTimeField(auto_now=True)
    修改人 = models.ForeignKey(
        User, editable=False, null=True,
        on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name = "汐止腔語料"
        verbose_name_plural = verbose_name

    def clean(self):
        sin_html = clean_html(self.羅馬字含口語調)
        self.羅馬字含口語調 = str(sin_html)
        self.羅馬字 = get_lomaji(sin_html)

    def __str__(self):
        return self.漢字
