from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import GroceryItem

def index(request):
    incomplete_items = GroceryItem.objects.filter(done=False).order_by('pub_date')
    copmpleted_items = GroceryItem.objects.filter(done=True).order_by('-complete_date')
    context={
        'incomplete_items': incomplete_items,
        'completed_items': copmpleted_items
    }
    return render(request, 'grocery/index.html', context)

def add(request):
    grocery_text = request.POST['description']
    # new_item = GroceryItem(grocery_text=grocery_text, pub_date=timezone.now(), done=False)
    # new_item.save()
    GroceryItem.objects.create(grocery_text=grocery_text, pub_date=timezone.now(), done=False)
    return HttpResponseRedirect(reverse('grocery:index'))

def complete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    if item.done:
        item.done = False
        item.complete_date = None
        item.save()
    else:
        item.done = True
        item.complete_date = timezone.now()
        item.save()

    return HttpResponseRedirect(reverse('grocery:index'))

def delete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.delete()

    return HttpResponseRedirect(reverse('grocery:index'))