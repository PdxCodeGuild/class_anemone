from django.forms import ModelForm
from .models import Input
from django import forms


class InputForm(forms.ModelForm):
    class Meta:
        model = Input
        fields ='__all__'
