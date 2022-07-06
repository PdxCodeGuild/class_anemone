from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import GroceryItem
from .forms import GroceryItemForm
# Create your views here.


def index(request):
    form = GroceryItemForm
    submitted = False
    incomplete_items = GroceryItem.objects.filter(
        complete=False).order_by('created_date')
    completed_items = GroceryItem.objects.filter(
        complete=True).order_by('completed_date')
    context = {
        'incomplete_items': incomplete_items,
        'completed_items': completed_items,
        'aform': form,
        'submitted': submitted
        
    }
    return render(request, 'grocery_list/index.html', context)


def add_item(request):
    submitted = False
    if request.method == "POST":
        form = GroceryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('grocery_list:index'), {'form': form, 'submitted': submitted})
    else:
        print('error')
        form = GroceryItem
        if 'submitted' in request.GET:
            submitted = True
    # form = GroceryItemForm        
    return HttpResponseRedirect(reverse('grocery_list:index'), {'form': form, 'submitted': submitted})

    
def update_item(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    print(item)
    if item.complete:
        item.complete = False
        item.completed_date = None
        item.save()
    else:
        item.complete = True
        item.completed_date = timezone.now()
        item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))


