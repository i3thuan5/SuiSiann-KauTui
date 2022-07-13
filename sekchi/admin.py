from django.contrib import admin
from sekchi.models import Sekchi
from django.utils.html import format_html
from tuitse import kiamtsa
from tuitse.html import tuitse_html


# Register your models here.
@admin.register(Sekchi)
class SekchiAdmin(admin.ModelAdmin):
    list_display = ('漢字', 'part', '編號', '修改時間')
    fields = ('音檔檔案', '漢字', '羅馬字含口語調', '對齊', 'part', '編號', '修改時間')
    readonly_fields = ('音檔檔案', '對齊', 'part', '編號', '修改時間')

    def 音檔檔案(self, obj):
        音檔html = '''<div>
                <audio controls><source src='{}'>
                Your browser does not support the audio element.</audio>
                </div>
                '''
        return format_html(音檔html, obj.音檔.url)

    def 對齊(self, obj):
        return tuitse_html(kiamtsa(obj.漢字, obj.羅馬字含口語調))
