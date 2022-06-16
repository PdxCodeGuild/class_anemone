from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from .models import GroceryItem

def index(request):
    # grocery_list = GroceryItem.objects.order_by('create_date')
    grocery_list = GroceryItem.objects
    incomplete_items = grocery_list.filter(completed=False).order_by('create_date')
    completed_items = grocery_list.filter(completed=True).order_by('-completed_date')

    context = {
        'grocery_list': grocery_list,
        'incomplete_items': incomplete_items,
        'completed_items': completed_items
    }

    return render(request, 'grocerylist_app/index.html', context)


def add(request):
    grocery_item_name = request.POST['grocery_item_name'] # get the value the user entered into the 'grocery item name' field
    completed = request.POST.get('completed', False) # get the value the user entered into the 'completed' field
    completed_date = request.POST.get('completed_date') # get the value the user entered into the 'completed date' field
    
    if completed:
        completed = True
    else:
        completed = False
        
    if not completed_date:
        completed_date = None
    
    create_date = timezone.now()
    add_item = GroceryItem(grocery_item_name=grocery_item_name, completed=completed, completed_date=completed_date, create_date=create_date) # create an instance of our model
    add_item.save() # save a new row to the database
    return HttpResponseRedirect(reverse('grocerylist_app:index'))


def update(request, id):
    item = get_object_or_404(GroceryItem, pk=id)

    if item.completed:
        item.completed = False
        item.completed_date = None
        item.save()
    else:
        item.completed = True
        item.completed_date = timezone.now()
        item.save()
    return HttpResponseRedirect(reverse('grocerylist_app:index'))


def delete(request, id):
    item = get_object_or_404(GroceryItem, pk=id)
    item.delete()
    return HttpResponseRedirect(reverse('grocerylist_app:index'))
