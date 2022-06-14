from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import GroceryItem

def index(request):
    latest_grocerylist = GroceryItem.objects.order_by('-date_created')
    context = {
        'latest_grocerylist': latest_grocerylist
    }
    print(latest_grocerylist)
    return render(request, 'grocerylist/index.html', context)
