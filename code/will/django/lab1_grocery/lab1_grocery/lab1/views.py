from pickle import FALSE
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from lab1.models import GroceryItem
from django.utils import timezone
# Create your views here.

def index(request):
    latest_grocery_list = GroceryItem.objects.all().order_by('-append_time')

    completed = latest_grocery_list.filter(task_completed = True)
    not_completed = latest_grocery_list.filter(task_completed = False)
    context = {
        'latest_grocery_list': latest_grocery_list,
        'completed' : completed,
        'not_completed' : not_completed
    }
    return render(request, 'lab1/index.html', context)


def create(request):
    
    grocery_item_add = request.POST['grocery_item']
    print(grocery_item_add)
    item = GroceryItem(grocery_description = grocery_item_add, task_completed = False)
    item.save()
    return HttpResponseRedirect(reverse('lab1:index'))


def complete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    if item.task_completed:
        item.task_completed = False
        item.completed_date = None
        item.save()

    else:
        item.task_completed = True
        item.date_completed = timezone.now()
        item.save()
    return HttpResponseRedirect(reverse ('lab1:index'))

def delete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.delete()
    
    return HttpResponseRedirect(reverse('lab1:index'))

