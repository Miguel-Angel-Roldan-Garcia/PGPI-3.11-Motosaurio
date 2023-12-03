from django import forms
from django.core.exceptions import ValidationError

class OrderForm(forms.Form):
    tipos_pago = [
        ["Cr", "Contrareembolso"],
        ["T", "Tarjeta"]
    ]

    tipos_envio = [
        ["D", "A domicilio"],
        ["R", "Recoger en tienda"]
    ]

    first_name = forms.CharField()
    email = forms.EmailField()
    direction = forms.CharField()
    postal_code = forms.IntegerField()
    payment_type = forms.ChoiceField(choices = tipos_pago, initial='T', help_text = "Método de pago")
    card_number = forms.CharField(max_length = 16, min_length = 16, required=False)
    delivery_type = forms.ChoiceField(choices = tipos_envio, initial = "D", help_text = "Método de envío")