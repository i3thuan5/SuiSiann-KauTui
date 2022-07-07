from django.contrib import admin
from sekchi.models import Sekchi


# Register your models here.
@admin.register(Sekchi)
class SekchiAdmin(admin.ModelAdmin):
    pass
