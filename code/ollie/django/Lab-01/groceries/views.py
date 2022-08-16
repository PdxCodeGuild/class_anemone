from django.http import HttpResponseRedirect

from django.urls import reverse

from django.shortcuts import render, get_object_or_404

from .models import GroceryItem

def index(request):
    complete_item = GroceryItem.objects.filter(complete=True)
    incomplete_item = GroceryItem.objects.filter(complete=False)
    context = {
        'complete_item': complete_item,
        'incomplete_item': incomplete_item
    }
    return render(request, 'index.html', context)

# def create(request):
#     item = request.POST['']
#     GroceryItem.objects.create()