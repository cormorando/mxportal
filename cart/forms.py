from django import forms


class AddProductForm(forms.Form):
    quantity = forms.CharField()
