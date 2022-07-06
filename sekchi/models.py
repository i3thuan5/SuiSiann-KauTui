from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Sekchi(models.Model):
    音檔 = models.FileField(blank=True)
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
