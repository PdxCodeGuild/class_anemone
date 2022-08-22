from datetime import *
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import GroceryItem



def index(request):
    incomplete_items = GroceryItem.objects.filter(completed=False).order_by('created_date')
    complete_items = GroceryItem.objects.filter(completed=True).order_by('-completed_date')
    context = {
        'incomplete_items': incomplete_items,
        'complete_items': complete_items
    }
    return render(request, 'grocerylist_app/index.html', context)

def add_item(request):
    text_description = request.POST['text_description']
    GroceryItem.objects.create(text_description=text_description, created_date=timezone.now(), completed=False)
    return HttpResponseRedirect(reverse('grocerylist_app:index'))


def complete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    if item.completed:
        item.completed = False
        item.completed_date = None
        item.save()
    else:
        item.completed = True
        item.completed_date = timezone.now()
        item.save()
    return HttpResponseRedirect(reverse('grocerylist_app:index'))

def delete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('grocerylist_app:index'))
