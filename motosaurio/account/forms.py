from django import forms
from motosaurio.models import MiUsuario

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña',widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Contraseña',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repite la contraseña',
                                widget=forms.PasswordInput)
    tarjeta = forms.IntegerField(label='Tarjeta de crédito', required=False)

    class Meta:
        model = MiUsuario
        fields = ['username', 'first_name', 'email', 'direccion']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return cd['password2']
    
class UserProfileForm(forms.ModelForm):
    tarjeta = forms.IntegerField(label='Tarjeta de crédito', required=False)
    direccion = forms.CharField(label='Dirección postal', required=False)
    class Meta:
        model = MiUsuario
        fields = ['direccion']

