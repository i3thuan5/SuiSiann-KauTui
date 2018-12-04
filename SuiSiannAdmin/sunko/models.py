from django.db import models


class 文章表(models.Model):
    文章名 = models.TextField(max_length=30, unique=True)

    def __str__(self):
        return self.文章名


class 句表(models.Model):
    來源 = models.ForeignKey(文章表, null=True,
                           related_name='+', on_delete=models.CASCADE)
    音檔 = models.FileField(blank=True)
    漢字 = models.CharField(blank=True, max_length=200)
    臺羅 = models.CharField(blank=True, max_length=200)
    修改時間 = models.DateTimeField(null=True)
    對齊狀態 = models.CharField(blank=True, max_length=200)

    def __str__(self):
        return self.漢字
