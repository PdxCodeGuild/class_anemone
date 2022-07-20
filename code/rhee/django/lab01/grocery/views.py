from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from .models import GroceryItems
from django.utils import timezone
from django.urls import reverse
# Create your views here.

def home(request):
    completed = GroceryItems.objects.filter(completed=True)
    incompleted = GroceryItems.objects.filter(completed=False)
    context = {
        'completed':completed,
        'incompleted': incompleted
    }
    return render(request, 'home.html', context)

def create(request):
    description = request.POST['description']    
    GroceryItems.objects.create(description=description, created_date=timezone.now(), completed=False)
    return HttpResponseRedirect(reverse('grocery:home'))

def complete(request, pk):
    item = get_object_or_404(GroceryItems, pk=pk)
    if item.completed:
        item.completed = False
        item.completed_date = None
    else:
        item.completed = True
        item.completed_date = timezone.now()
    item.save()
    return HttpResponseRedirect(reverse('grocery:home'))

def delete(request, pk):
    item = get_object_or_404(GroceryItems, pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('grocery:home'))