

def 重對齊(modeladmin, request, queryset):
    for obj in queryset:
        obj.重對齊()


重對齊.short_description = "用kaldi對齊切音，提著一句一句ê音檔"
