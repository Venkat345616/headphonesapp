# forms.py
from django import forms

class CartActionForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput())
    action = forms.CharField(widget=forms.HiddenInput())
