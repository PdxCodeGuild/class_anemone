from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import GroceryItem
# from .models import classes here
# check to make sure you are actully using these imports for this app

def index(request):
    grocery = GroceryItem.objects.all()
    context = {'grocery':grocery}
    # replace with whatever variable you need?
    return render(request, 'grocery_list/index.html', context)

