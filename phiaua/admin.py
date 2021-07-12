from django.contrib import admin
from phiaua.models import Khuán, Luī, Iūnn
import nested_admin


class IūnnTsuā(
    nested_admin.NestedStackedInline,
):
    model = Iūnn
    fields = ['id', 'css']
    extra = 0


class LuīTsuā(
    nested_admin.SortableHiddenMixin,
    nested_admin.NestedStackedInline,
):
    model = Luī
    fields = ['id', 'miâ', 'siktsuí', 'singāu']
    extra = 1
    sortable_field_name = 'singāu'


@admin.register(Khuán)
class KuánKhuán(admin.ModelAdmin):
    list_display = ['id', 'miâ', ]
    ordering = ['id', ]
    list_per_page = 50
    inlines = [IūnnTsuā, LuīTsuā, ]
