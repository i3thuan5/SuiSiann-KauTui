from django.contrib import admin
from sunko.admins.對齊thai仔 import 對齊thai仔
from django.utils.html import format_html
from sunko.admins.放音檔欄位 import 放音檔欄位



class 句後台(admin.ModelAdmin, 放音檔欄位):
    list_display = ['id', '放音檔', '漢字', '臺羅', '對齊狀態']
    list_filter = ['來源', 對齊thai仔]
    ordering = ['id']
    list_per_page = 10
    
    
