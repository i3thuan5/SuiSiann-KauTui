from django.contrib import admin
from SuiSiannAdminApp.admins.對齊thai仔 import 對齊thai仔
from django.utils.html import format_html
from SuiSiannAdminApp.admins.放音檔欄位 import 放音檔欄位
from SuiSiannAdminApp.admins.句表單 import 句表單
from SuiSiannAdminApp.admins.action正規化漢字 import 漢字括號共提掉



class 句後台(admin.ModelAdmin, 放音檔欄位):
    list_display = ['id', '放音檔', '漢字', '臺羅', '對齊狀態']
    list_filter = ['來源', 對齊thai仔]
    ordering = ['id']
    list_per_page = 10
    actions = [漢字括號共提掉]
    
    # change view
    readonly_fields = ('音檔','放音檔', '修改時間', '對齊狀態')
    fields = ('漢字', '臺羅', '對齊狀態', '放音檔', '音檔', '修改時間', )
    form = 句表單