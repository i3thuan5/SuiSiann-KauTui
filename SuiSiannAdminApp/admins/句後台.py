from django.utils.timezone import now
from django.urls import path
from phiaua.admin.options import PhiauAModelAdmin
from SuiSiannAdminApp.admins.對齊thai仔 import 對齊thai仔
from SuiSiannAdminApp.admins.句表單 import 句表單
from SuiSiannAdminApp.admins.action正規化漢字 import 漢字括號共提掉
from SuiSiannAdminApp.views.diffView import DiffView


class 句後台(PhiauAModelAdmin):
    # change list
    list_display = [
        'id', '漢字', '羅馬字',
        '狀況', '備註', '對齊狀態',
        '修改時間', '修改人',
    ]
    list_filter = ['語料狀況', 對齊thai仔, '來源', '修改人', ]
    ordering = ['id', ]
    list_per_page = 10
    actions = [漢字括號共提掉]
    search_fields = ['id', '漢字', '羅馬字', '備註', ]

    # change view
    save_on_top = True
    readonly_fields = (
        '對齊狀態',
        '海湧', '音檔所在',
        '修改時間',
    )
    fields = (
        '漢字', '羅馬字含口語調',
        '海湧',
        '對齊狀態',
        '語料狀況', '備註',
        '音檔所在', '修改時間',
    )
    form = 句表單
    autocomplete_fields = ['語料狀況']

    # change list
    def 狀況(self, obj):
        陣列 = []
        for 狀況 in obj.語料狀況.order_by('id'):
            陣列.append(str(狀況.id))
        return ', '.join(陣列)

    # change view
    def save_model(self, request, obj, form, change):
        obj.修改時間 = now()
        obj.修改人 = request.user

        super(句後台, self).save_model(request, obj, form, change)

    def get_urls(self):
        urls = super().get_urls()
        suisiann_urls = [
            path('admin/edit_diff/', DiffView.as_view(), name='diff'),
        ]
        return suisiann_urls + urls

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
