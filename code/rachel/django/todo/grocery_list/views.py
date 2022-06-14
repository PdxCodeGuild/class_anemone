from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import GroceryItem

def index (request):
    latest_grocery_list = GroceryItem.objects.order_by('-pub_date')[:5]
    context = {
        'latest_grocery_list' : latest_grocery_list
    }
    return render(request, 'grocery_list/index.html', context)