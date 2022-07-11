from datetime import timezone
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import GroceryItem


def index(request):
    return HttpResponse('hello world!')

def index(request):
    incomplete_items = GroceryItem.objects.filter(completed=False)
    complete_items = GroceryItem.objects.filter(completed=True)
    context = {
        'incomplete_items': incomplete_items,
        'complete_items': complete_items
    }
    return render(request, 'grocerylist_app/index.html', context)

def add_item(request):
    text_description = request.POST['text_description']
    GroceryItem.objects.create(text_description=text_description, created_date=timezone.now(), completed=False)
    return HttpResponseRedirect(reverse('grocerylist_app:index'))


def complete(request, pk):
    new_item = get_object_or_404(GroceryItem, pk=pk)
    if new_item.completed:
        new_item.completed = False
        new_item.completed_date = None
        new_item.save()
    else:
        new_item.completed = True
        new_item.completed_date = timezone.now()
        new_item.save()
    return HttpResponseRedirect(reverse('grocery:index'))

def delete(request, pk):
    new_item = get_object_or_404(GroceryItem, pk=pk)
    new_item.delete()
    return HttpResponseRedirect(reverse('grocery:index'))
