from django.contrib import admin
from sunko.models import 句表, 文章表
from sunko.admins.句後台 import 句後台

# Register your models here.


admin.site.register(文章表)
admin.site.register(句表, 句後台)
