from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import GroceryItem

def index(request):
    grocery = GroceryItem.objects.all()
    incomplete_items = grocery.filter(is_complete=False)
    completed_items = grocery.filter(is_complete = True)
    context = {'grocery':grocery, 'incomplete_items':incomplete_items, 'completed_items': completed_items}
    return render(request, 'grocery_list/index.html', context)

def create(request):
    grocery_text = request.POST['grocery_text']
    date_created = timezone.now()
    grocery_item = GroceryItem(grocery_text=grocery_text, date_created=date_created)
    grocery_item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def complete(request, grocery_text_id):
    grocery_item = get_object_or_404(GroceryItem, pk=grocery_text_id)
    if grocery_item.is_complete == False:
        grocery_item.is_complete = True
        date_completed = timezone.now()
    else:
        grocery_item.is_complete = False
    grocery_item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def delete(request, grocery_text_id):
    grocery_item = get_object_or_404(GroceryItem, pk=grocery_text_id)
    grocery_item.delete()
    return HttpResponseRedirect(reverse('grocery_list:index'))




