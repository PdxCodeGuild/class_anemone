from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
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

def create (request):
    new_item = request.POST['additem']
    GroceryItem.objects.create(item_text=new_item, create_date=timezone.now())
    return HttpResponseRedirect(reverse('grocery_list:index'))

def markcomplete (request, item_id):
    item = get_object_or_404(GroceryItem, pk=item_id)
    if item.is_completed == True:
        item.is_completed = False
    else:
        item.is_completed = True
    item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def delete (request, item_id):
    item = get_object_or_404(GroceryItem, pk=item_id)
    item.delete()
    return HttpResponseRedirect(reverse('grocery_list:index'))