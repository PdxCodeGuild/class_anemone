from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import GroceryItem

def index (request):
    latest_grocery_list = GroceryItem.objects.order_by('-create_date')
    completed_items = latest_grocery_list.filter(is_completed=True)
    incomplete_items = latest_grocery_list.filter(is_completed=False)
    context = {
        'latest_grocery_list' : latest_grocery_list,
        'completed_items' : completed_items,
        'incomplete_items' : incomplete_items,
    }

    return render(request, 'grocery_list/index.html', context)

# def create (request):
#     redirect
#     .objects.create()

# def markcomplete (request):
#     if else statement
#     redirect

# def delete (request):
#     redirect