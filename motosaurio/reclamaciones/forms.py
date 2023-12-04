from django import forms
from .models import Reclamacion

class ReclamacionForm(forms.ModelForm):
    titulo = forms.CharField(label='Título', required=True)
    descripcion = forms.CharField(label='Descripción', required=True,widget=forms.Textarea(attrs={'rows': 10, 'cols': 70}))
    class Meta:
        model = Reclamacion
        fields = ['titulo','descripcion']