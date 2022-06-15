from multiprocessing import context
from unittest import result
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import GroceryItem,ItemChoice

def index(request):
    latest_grocery_list = GroceryItem.objects.order_by('-pub_date')[:5]
    context = {
        'latest_grocery_list': latest_grocery_list
    }
    return render(request, 'grocery/index.html', context)

def detail(request, grocery_item):
    if request.method=='POST':
        grocery_item = get_object_or_404(ItemChoice, pk=grocery_item.id)
    return render(request, 'grocery/detail.html', {'grocery_item': grocery_item})