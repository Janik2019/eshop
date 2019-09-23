from django import forms
from django.forms import widgets
from .models import PRODUCT_CATEGORY_CHOICES


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Name')
    description = forms.CharField(max_length=2000, required=False, widget=widgets.Textarea, label='Description')
    category = forms.ChoiceField(required=True, choices=PRODUCT_CATEGORY_CHOICES, label='Category')
    amount = forms.IntegerField(required=True, min_value=0, label='Amount')
    price = forms.DecimalField(required=True, max_digits=7, decimal_places=2, label='Price')


class SearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Name')