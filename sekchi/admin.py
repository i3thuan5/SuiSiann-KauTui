from django import forms
from django.contrib import admin
from sekchi.models import Sekchi
from django.utils.html import format_html
from tuitse import kiamtsa
from tuitse.html import tuitse_html


class SekchiForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["羅馬字含口語調"].widget = forms.widgets.Textarea(
        attrs={'class': 'phiaua'})


# Register your models here.
@admin.register(Sekchi)
class SekchiAdmin(admin.ModelAdmin):
    form = SekchiForm
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

    class Media:
        css = {
            'all': ('sekchi/css/tuitse.css',)
        }
        js = (
            'https://cdn.tiny.cloud/1/7r771z07171zzo2b460fzfdmi25680770i1u6nf3mz6uh1fs/tinymce/5/tinymce.min.js',
            'phiaua/js/lomaji.js',
            'phiaua/js/suan_lomaji.js',
        )
