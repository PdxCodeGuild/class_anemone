from django.shortcuts import render

from .models import GroceryItem
# Create your views here.
def index(request):
    item_list = GroceryItem.objects.all()
    context = {
        'item_list' : item_list
    }
    return render(request, 'grocery_list/index.html', context)