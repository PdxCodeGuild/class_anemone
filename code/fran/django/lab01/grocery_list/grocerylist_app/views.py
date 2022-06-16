from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import GroceryItem

def index(request):
    grocery_list = GroceryItem.objects.order_by('create_date')
    incomplete_items = grocery_list.filter(completed=False)
    completed_items = grocery_list.filter(completed=True)

    context = {
        'grocery_list': grocery_list,
        'incomplete_items': incomplete_items,
        'completed_items': completed_items
    }

    return render(request, 'grocerylist_app/index.html', context)


def add(request):
    # print(request.POST) # verify we received the form data
    grocery_item_name = request.POST['grocery_item_name'] # get the value the user entered into the 'grocery item name' field
    completed = request.POST.get('completed', False) # get the value the user entered into the 'completed' field
    completed_date = request.POST.get('completed_date') # get the value the user entered into the 'completed date' field
    
    if not completed_date:
        completed_date = None
    
    create_date = request.POST['create_date'] # get the value the user entered into the 'create date' field
    add_item = GroceryItem(grocery_item_name=grocery_item_name, completed=completed, completed_date=completed_date, create_date=create_date) # create an instance of our model
    add_item.save() # save a new row to the database
    return HttpResponseRedirect(reverse('grocerylist_app:index'))


def update(request):
    completed = True
    completed_date = 
    update_item = GroceryItem(grocery_item_name=grocery_item_name, completed=completed, completed_date=completed_date, create_date=create_date) # create an instance of our model
