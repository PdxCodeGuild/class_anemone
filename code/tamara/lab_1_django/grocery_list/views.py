from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import GroceryItem

# view is used to get the info you want to display in the template
def index(request):
    # creates 2 query sets 
    incomplete_items = GroceryItem.objects.filter(is_complete=False).order_by('date_created') # oldest to newest
    completed_items = GroceryItem.objects.filter(is_complete = True).order_by('-date_completed') # most recently completed to oldest
    # creates 2 seperate lists for the 2 query sets
    context = {'incomplete_items':incomplete_items, 'completed_items': completed_items}
    return render(request, 'grocery_list/index.html', context)

def create(request):
    # gets the text that the user POSTed and assigns it to grocery_text
    grocery_text = request.POST['grocery_text']
    date_created = timezone.now()
    grocery_item = GroceryItem(grocery_text=grocery_text, date_created=date_created)
    grocery_item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def complete(request, pk):
    # get the grocery item based on its primary key -- looks through all of the groceryitems for a pk that matches the pk POSTed by user
    grocery_item = get_object_or_404(GroceryItem, pk=pk)
    if grocery_item.is_complete == False:
        grocery_item.is_complete = True
        date_completed = timezone.now()
        grocery_item.save()
    else:
        grocery_item.is_complete = False
        grocery_item.date_completed = None
        grocery_item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def delete(request, pk):
    grocery_item = get_object_or_404(GroceryItem, pk=pk)
    grocery_item.delete()
    return HttpResponseRedirect(reverse('grocery_list:index'))




