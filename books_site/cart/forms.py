from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(label="Количество", choices=PRODUCT_QUANTITY_CHOICES, coerce=int, initial = '1', widget=forms.HiddenInput)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    

class Promo(forms.Form):
    promo = forms.CharField(widget=forms.TextInput(attrs={"id":"promo"}))