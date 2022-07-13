from django.contrib import admin
from sekchi.models import Sekchi


# Register your models here.
@admin.register(Sekchi)
class SekchiAdmin(admin.ModelAdmin):
    list_display = ('漢字', 'part', '編號', '修改時間')
