from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

from .models import GroceryItem

# Create your views here.
def index(request):
    # Filter incomplete items by date created
    incomplete_items = GroceryItem.objects.filter(shop_complete=False).order_by('date_created')
    # Filter complete items by date completed in reverse order
    complete_items = GroceryItem.objects.filter(shop_complete=True).order_by('-date_complete')
    # A dictionary containing complete/incomplete items
    context = {
        'incomplete_items': incomplete_items,
        'complete_items': complete_items
    }
    return render(request, 'grocerylist/index.html', context)

def add_item(request):
    description = request.POST['description']
    # new_item = GroceryItem(text_description=text_description, date_created=timezone.now(), date_complete=False)
    # new_item.save()
    GroceryItem.objects.create(text_description=description, date_created=timezone.now(), shop_complete=False)
    return HttpResponseRedirect(reverse('grocerylist:index'))

def complete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    if item.shop_complete:
        item.shop_complete = False
        item.date_complete = None
        item.save()
    else:
        item.shop_complete = True
        item.date_complete = timezone.now()
        item.save()
    return HttpResponseRedirect(reverse('grocerylist:index'))

def delete(request, pk):
    item = get_object_or_404(GroceryItem, pk)
    item.delete()
    return HttpResponseRedirect(reverse('grocerylist:index'))


