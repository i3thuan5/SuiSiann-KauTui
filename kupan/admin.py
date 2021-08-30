from django.contrib import admin

from SuiSiannAdminApp.admins.句後台 import 句後台
from kupan.models import Le, Khuán
from SuiSiannAdminApp.admins.對齊thai仔 import 對齊thai仔


@admin.register(Le)
class LekuAdmin(句後台):
    list_filter = ['tó一款句辦', 對齊thai仔, ]

    save_on_top = True
    readonly_fields = (
        '對齊狀態',
        '海湧',
        '修改時間',
    )
    fields = (
        '漢字', '羅馬字含口語調',
        '海湧',
        '對齊狀態',
        'tó一款句辦', '備註',
        '修改時間',
    )
    autocomplete_fields = ['tó一款句辦']


@admin.register(Khuán)
class KhuánAdmin(admin.ModelAdmin):
    search_fields = ['id', 'miâ']
