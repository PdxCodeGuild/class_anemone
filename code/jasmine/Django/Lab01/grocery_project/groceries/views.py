from tkinter.messagebox import RETRY
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Grocery_Item


# Create your views here.
def index(request):
    incomplete_items = Grocery_Item.objects.filter(complete=False).order_by('created_date')
    completed_items = Grocery_Item.objects.filter(complete=True).order_by('-completed_date')
    context = {
        'incomplete_items': incomplete_items,
        'completed_items': completed_items
    }
    return render(request, 'groceries/index.html', context)

def create(request):
    description = request.POST['description']
    Grocery_Item.objects.create(description=description, created_date=timezone.now(), complete=False)
    return HttpResponseRedirect(reverse('grocery:index'))

def complete(request, pk):
    item = get_object_or_404(Grocery_Item, pk=pk)
    if item.complete:
        item.complete = False
        item.completed_date = None
        item.save()
    else:
        item.complete = True
        item.completed_date = timezone.now()
        item.save()
    return HttpResponseRedirect(reverse('grocery:index'))

def delete(request, pk):
    item = get_object_or_404(Grocery_Item, pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('groceries:index'))