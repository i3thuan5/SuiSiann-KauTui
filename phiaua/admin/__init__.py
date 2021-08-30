from django.contrib import admin
from phiaua.models import Khuán, Luī
import nested_admin


class LuīTsuā(
    nested_admin.SortableHiddenMixin,
    nested_admin.NestedTabularInline,
):
    model = Luī
    fields = ['id', 'miâ', 'siktsuí', 'singāu']
    extra = 0
    sortable_field_name = 'singāu'


@admin.register(Khuán)
class KuánKhuán(nested_admin.NestedModelAdmin):
    list_display = ['id', 'miâ', 'iūnn', ]
    ordering = ['id', ]
    inlines = [LuīTsuā, ]


admin.site.site_title = 'Suísiann'
admin.site.site_header = 'Suísiann Dataset'
admin.site.index_title = 'Kàu-tuì'
admin.site.site_url = 'https://github.com/i3thuan5/SuiSiann-KauTui'
