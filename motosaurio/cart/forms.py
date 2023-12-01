from django import forms


class CestaAddProductForm(forms.Form):
    quantity = forms.IntegerField(label='Cantidad',min_value=1,max_value=20, initial=1)

    override = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
    