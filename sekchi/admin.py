from django.contrib import admin
from sekchi.models import Sekchi


# Register your models here.
@admin.register(Sekchi)
class SekchiAdmin(admin.ModelAdmin):
    list_display = ('漢字', 'part', '編號', '修改時間')
    fields = ('音檔', '漢字', '羅馬字含口語調', 'part', '編號', '修改時間')
    readonly_fields = ('part', '編號', '修改時間')
