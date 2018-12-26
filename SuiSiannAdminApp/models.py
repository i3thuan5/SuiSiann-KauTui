from django.db import models
from SuiSiannAdminApp.management.檢查對齊狀態 import 檢查對齊狀態


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

    def save(self, *args, **kwargs):
        self.對齊狀態 = 檢查對齊狀態(self.漢字, self.臺羅)
        super().save(*args, **kwargs)  # Call the "real" save() method.
