from django.contrib import admin
from SuiSiannAdminApp.admins.對齊thai仔 import 對齊thai仔
from SuiSiannAdminApp.admins.放音檔欄位 import 放音檔欄位
from SuiSiannAdminApp.admins.句表單 import 句表單
from SuiSiannAdminApp.admins.action正規化漢字 import 漢字括號共提掉
from django.utils.timezone import now
from SuiSiannAdminApp.admins.action重對齊 import 重對齊


class 句後台(admin.ModelAdmin, 放音檔欄位):
    # change list
    list_display = ['id', '漢字', '臺羅', '狀況', '備註', '對齊狀態', '修改時間', ]
    list_filter = ['語料狀況', 對齊thai仔, '來源', ]
    ordering = ['修改時間', 'id', ]
    list_per_page = 10
    actions = [漢字括號共提掉, 重對齊]
    search_fields = ['id', '漢字', '臺羅', '備註', ]

    # change view
    readonly_fields = ('音檔', '放切好音檔', '放音檔', '修改時間', '對齊狀態',)
    fields = ('漢字', '臺羅', '對齊狀態', '放切好音檔', '放音檔', '語料狀況',
              '備註', '音檔', '修改時間',)
    form = 句表單

    # change list
    def 狀況(self, obj):
        陣列 = []
        for 狀況 in obj.語料狀況.order_by('id'):
            陣列.append(str(狀況.id))
        return ', '.join(陣列)

    # change view
    def save_model(self, request, obj, form, change):
        obj.修改時間 = now()
        super(句後台, self).save_model(request, obj, form, change)
