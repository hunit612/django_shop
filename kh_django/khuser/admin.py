from django.contrib import admin
from .models import Khuser
# Register your models here.


class KhuserAdmin(admin.ModelAdmin):
    list_display = ('email', )

    
admin.site.register(Khuser, KhuserAdmin)
admin.site.site_header = '후니'
admin.site.index_title = '후니 타이틀'
admin.site.site_title = '후니 사이트 타이틀'