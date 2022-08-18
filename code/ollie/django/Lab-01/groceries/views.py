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

def create(request):
    item = request.POST['item_text']
    GroceryItem.objects.create(item_text=item, created_date=GroceryItem.completed_date)
    return HttpResponseRedirect(reverse('groceries:index'))

def update(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    if item.complete:
        item.complete = False
        item.completed_date = None
        item.save()
    else:
        item.complete = True
        item.completed_date = GroceryItem.completed_date
        item.save()
    return HttpResponseRedirect(reverse('groceries:index'))

def delete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('groceries:index'))