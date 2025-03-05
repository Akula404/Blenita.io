from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['item_name', 'item_price', 'customer_name', 'contact_number', 'quantity']
