from django.contrib import admin
from .models import Khuser
# Register your models here.


class KhuserAdmin(admin.ModelAdmin):
    list_display = ('email', )

    def changelist_view(self, request, extra_context=None):
        extra_context = { 'title': '사용자 목록' }
        return super().changelist_view(request,extra_context)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        khuser = Khuser.objects.get(pk=object_id)      
        extra_context = { 'title': f'{khuser.email} 수정하기' }
        return super().changeform_view(request, object_id, form_url, extra_context)

    
admin.site.register(Khuser, KhuserAdmin)
admin.site.site_header = '후니'
admin.site.index_title = '후니 타이틀'
admin.site.site_title = '후니 사이트 타이틀'