from django.shortcuts import render
from django.http import HttpResponse
from .models import GroceryItem

def index(request):
    latest_grocerylist = GroceryItem.objects.order_by('-pub_date')
    context = {
        'latest_grocerylist': latest_grocerylist
    }
    return render(request, 'grocerylist/index.html', context)
