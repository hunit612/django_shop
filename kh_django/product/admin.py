from django.contrib import admin
from django.utils.html import format_html
from django.contrib.humanize import intcomma
from .models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_format', 'styled_stock')

    def price_format(self, obj):
        pric = intcomma(obj.price)
        return f'{price} 원'

    def styled_stock(self, obj):
        stock = obj.stock
        if stock <= 50:
            stock = intcomma(stock)
            return format_html(f'<b><span style="color:red">{stock} 개</span></b>')
        return f'{intcomma(stock)} 개' 

    styled_stock.short_description = '재고'
    price_format.short_description = '가격'

admin.site.register(Product, ProductAdmin)