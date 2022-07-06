from django import forms
from .models import UrlData

class UrlForm(forms.ModelForm):
    class Meta:
        model = UrlData
        fields = ('url',)
        widgets = {
            'url': forms.TextInput(attrs={'class': 'form-control'})
        }
