from django import forms
from django.forms import ModelForm
from .models import GroceryItem

class GroceryItemForm(ModelForm):
    class Meta:
        model = GroceryItem
        fields = ("description","complete")
        labels = {
            "description" : "Item",
            "complete": "Complete"
        }
        # widgets = {
        #     "description" : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Grocery Item'})
        # }
        
# class CompletedItemForm(ModelForm):
#     class Meta:
#         model = GroceryItem
#         fields = ('complete',)



