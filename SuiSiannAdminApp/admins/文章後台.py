from django.contrib import admin
from django.db.models.aggregates import Count


class 文章後台(admin.ModelAdmin):
    # change list
    list_display = ['id', '文章名', '句數']
    ordering = ['id', ]
    list_per_page = 50

    def get_queryset(self, request):
        return (
            super().get_queryset(request)
            .annotate(句數資料=Count('句'))
        )

    def 句數(self, obj):
        return obj.句數資料
