from SuiSiannAdminApp.management.正規化漢字 import 提掉漢字的括號


def 漢字括號共提掉(modeladmin, request, queryset):
    for obj in queryset:
        obj.漢字 = 提掉漢字的括號(obj.漢字)
        obj.save()


漢字括號共提掉.short_description = "全形括號kah半形括號攏總共提掉"
