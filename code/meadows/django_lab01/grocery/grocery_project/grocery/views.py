from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import GroceryList

def index(request):
    need = GroceryList.objects.filter(created_complete=False).order_by('-created_date')
    have = GroceryList.objects.filter(created_complete=True).order_by('-date_complete')
    context = {
        'need':need,
        'have':have
    }
    return render(request, 'grocery/index.html', context)

def add(request):
    created_item = request.POST['created_item']
    GroceryList.objects.create(created_item=created_item, created_date=timezone.now(), created_complete=request.POST['created_complete'])
    return HttpResponseRedirect(reverse('grocery:index'))

def complete(request, pk):
    new = get_object_or_404(GroceryList, pk=pk)
    if new.created_complete:
        new.created_complete=False
        new.date_complete=None
        new.save()
    else:
        new.created_complete=True
        new.date_complete=timezone.now()
        new.save()
    return HttpResponseRedirect(reverse('grocery:index'))

def delete(request, pk):
    new = get_object_or_404(GroceryList,pk=pk)
    new.delete()
    return HttpResponseRedirect(reverse('grocery:index'))
