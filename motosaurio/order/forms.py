from django import forms
from django.core.exceptions import ValidationError

class OrderForm(forms.Form):
    tipos_pago = [
        ["Cr", "Contrareembolso"],
        ["T", "Tarjeta"]
    ]

    first_name = forms.CharField()
    email = forms.EmailField()
    direction = forms.CharField()
    postal_code = forms.IntegerField()
    payment_type = forms.ChoiceField(choices = tipos_pago, initial='Cr', help_text = "Método de pago")
    card_number = forms.IntegerField(help_text = "", required=False)