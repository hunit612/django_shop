from django.contrib import admin
from .models import Khuser
# Register your models here.


class KhuserAdmin(admin.ModelAdmin):
    list_display = ('email', )

    
admin.site.register(Khuser, KhuserAdmin)