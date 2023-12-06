from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    rating = forms.ChoiceField(label='Puntuación',choices=RATING_CHOICES,required=True,)
    comment = forms.CharField(label='Opinión',required=False,widget=forms.Textarea(attrs={'rows': 10, 'cols': 70}))

    class Meta:
        model = Product
        fields = ['rating', 'comment']
