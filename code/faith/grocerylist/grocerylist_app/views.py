from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from grocerylist.grocerylist_app.models import GroceryItem
def index(request):
    return HttpResponse('hello world!')

def index(request):
    incomplete_items = GroceryItem.objects.filter(complete=False)
    complete_items = GroceryItem.objects.filter(complete=True)
    context = {
        'incomplete_items': incomplete_items,
        'complete_items': complete_items
    }
    return render(request, 'grocerylist_app/index.html', context)