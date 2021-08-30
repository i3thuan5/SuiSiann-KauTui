from django.contrib import admin
from django import forms
from phiaua.admin.options import PhiauAModelAdmin
from kupan.models import Lē, Khuán, Tsònghóng
from SuiSiannAdminApp.admins.對齊thai仔 import 對齊thai仔


class LekuForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["漢字"].widget = forms.widgets.Textarea(
            attrs={'rows': 3, 'cols': '100'})
        self.fields["羅馬字含口語調"].widget = forms.widgets.Textarea(
            attrs={'class': 'phiaua'})
        self.fields["備註"].widget = forms.widgets.Textarea(
            attrs={'rows': 2, 'cols': 100})


@admin.register(Lē)
class LekuAdmin(PhiauAModelAdmin):
    list_display = [
        'id', '漢字', '羅馬字',
        '備註', '對齊狀態',
        '修改時間', '修改人',
    ]
    list_filter = ['tó一款句辦', '校對狀況', 對齊thai仔, ]
    ordering = ['id', ]
    list_per_page = 20
    search_fields = ['id', '漢字', '羅馬字', '備註', ]

    form = LekuForm
    save_on_top = True
    readonly_fields = (
        '對齊狀態',
        '放送',
    )
    fields = (
        '漢字', '羅馬字含口語調',
        '放送',
        '音檔',
        '對齊狀態',
        'tó一款句辦', '校對狀況', '備註',
    )
    autocomplete_fields = ['tó一款句辦', '校對狀況', ]

    def save_model(self, request, obj, form, change):
        obj.修改人 = request.user

        super().save_model(request, obj, form, change)


@admin.register(Khuán)
class KhuánAdmin(admin.ModelAdmin):
    search_fields = ['id', 'miâ']


@admin.register(Tsònghóng)
class TsònghóngAdmin(admin.ModelAdmin):
    search_fields = ['id', 'miâ']
