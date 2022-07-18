from django import forms
from django.contrib import admin
from sekchi.models import Sekchi
from django.utils.html import format_html
from tuitse import kiamtsa
from tuitse.html import tuitse_html
from phiaua.admin.options import PhiauAModelAdmin


class SekchiForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["羅馬字含口語調"].widget = forms.widgets.Textarea(
            attrs={'class': 'phiaua'}
        )


class HoAhBeFilter(admin.SimpleListFilter):
    title = '校對ah袂'
    parameter_name = 'hoahbe'

    def lookups(self, request, model_admin):
        return (
            ('1', 'Ah-bē'),
            ('2', '好勢'),
        )

    def queryset(self, request, queryset):
        if self.value() == '1':
            return queryset.filter(修改人__isnull=True)
        if self.value() == '2':
            return queryset.filter(修改人__isnull=False)


@admin.register(Sekchi)
class SekchiAdmin(PhiauAModelAdmin):
    form = SekchiForm
    list_display = ('id', 'part', '編號', '漢字', '修改時間',)
    ordering = ('id',)
    list_filter = (HoAhBeFilter,)
    fields = ('音檔檔案', '漢字', '羅馬字含口語調', '對齊', 'part', '編號', '修改時間')
    readonly_fields = ('音檔檔案', '對齊', 'part', '編號', '修改時間')
    search_fields = ('part', '編號', '漢字',)

    def 音檔檔案(self, obj):
        音檔html = '''<div>
                <audio controls><source src='{}'>
                Your browser does not support the audio element.</audio>
                </div>
                '''
        return format_html(音檔html, obj.音檔.url)

    def 對齊(self, obj):
        return tuitse_html(kiamtsa(obj.漢字, obj.羅馬字))

    def save_model(self, request, obj, form, change):
        obj.修改人 = request.user
        super().save_model(request, obj, form, change)
