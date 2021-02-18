from django import forms
from django.db.models import query
from .models import Order
from product.models import Product
from khuser.models import Khuser

class RegisterForm(forms.Form):
    def __init__(self, request, *args, **kwargs):
        res = super().__init__(*args, **kwargs)
        self.request = request
        

    quantity = forms.IntegerField(
        error_messages={
            'required': '수량을 입력해주세요.'
        },
        label='수량'
    )
    product = forms.IntegerField(
        error_messages={
            'required': '상품설명을 입력해주세요.'
        }, label='상품설명', widget=forms.HiddenInput
    )

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
        khuser = self.request.session.get('user')

        if quantity and product and khuser:
            order = Order(
                quantity=quantity,
                product=Product.objects.get(pk=product),
                khuser=Khuser.objects.get(email=khuser)
            )
            order.save()
        else:
            self.product = product
            self.add_error('quantity', '값이 없습니다')
            self.add_error('product', '값이 없습니다')
