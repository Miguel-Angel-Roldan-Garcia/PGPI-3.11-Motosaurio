from django import forms
from motosaurio.models import MiUsuario
from django.core.validators import MaxValueValidator, MinValueValidator

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña',widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    tipos_pago = [
        ["Cr", "Contrareembolso"],
        ["T", "Tarjeta"]
    ]

    tipos_envio = [
        ["D", "A domicilio"],
        ["R", "Recoger en tienda"]
    ]
    password = forms.CharField(label='Contraseña',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repite la contraseña',
                                widget=forms.PasswordInput)
    tarjeta = forms.IntegerField(label='Tarjeta de crédito', required=False)
    payment_type = forms.ChoiceField(label='Método de pago',choices = tipos_pago, initial='T', required=False)
    delivery_type = forms.ChoiceField(label='Método de envío',choices = tipos_envio, initial = "D")

    class Meta:
        model = MiUsuario
        fields = ['username', 'first_name', 'email', 'direccion','codigo','payment_type','delivery_type']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return cd['password2']
    
class UserProfileForm(forms.ModelForm):
    tipos_pago = [
        ["Cr", "Contrareembolso"],
        ["T", "Tarjeta"]
    ]

    tipos_envio = [
        ["D", "A domicilio"],
        ["R", "Recoger en tienda"]
    ]
    tarjeta = forms.IntegerField(label='Tarjeta de crédito', required=False)
    direccion = forms.CharField(label='Dirección postal', required=False)
    codigo = forms.IntegerField(label='Código postal',validators=[MaxValueValidator(99999),MinValueValidator(00000)], required=False)
    payment_type = forms.ChoiceField(label='Método de pago',choices = tipos_pago, initial='T',required=False)
    delivery_type = forms.ChoiceField(label='Método de envío',choices = tipos_envio, initial = "D",required=False)
    class Meta:
        model = MiUsuario
        fields = ['direccion','codigo','tarjeta','payment_type','delivery_type']

    def codigo_invalido(self):
        cd = self.cleaned_data
        if cd['codigo'] == None:
            raise forms.ValidationError('El código postal es obligatorio')
        return cd['codigo']

    def direccion_invalida(self):
        cd = self.cleaned_data
        if cd['direccion'] == '':
            raise forms.ValidationError('La dirección es obligatoria')
        return cd['direccion']

