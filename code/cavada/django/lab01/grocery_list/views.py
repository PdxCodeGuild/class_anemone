from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

# Create your views here.
from .models import GroceryItem

def index(request):
    grocery_list= GroceryItem.objects.all().order_by("-date_created")
    completed = grocery_list.filter(status=True)
    incomplete = grocery_list.filter(status=False)
    print("index",grocery_list)
    context = {
        'grocery_list': grocery_list,
        'completed': completed,
        'incomplete':incomplete
    }
    return render (request, 'grocery_list/index.html', context)

def add(request):
    new_item = request.POST['new']
    if new_item == '':
        message= "please enter a valid input"
        context={"message":message}
        return HttpResponseRedirect (reverse("grocery_list:index"),context)
    
    print("add",new_item)
    g = GroceryItem(desc=new_item,date_created = timezone.now(),status=False, date_fulfilled = None)
    g.save()
    grocery_list= GroceryItem.objects.all()
    context = {
        'grocery_list': grocery_list
    }
    return HttpResponseRedirect (reverse("grocery_list:index"),context)

def update(request):
    id = request.POST['item']
    print("update",id)
    g = GroceryItem.objects.get(pk=id)
    if g.status==False:
        g.status=True
        g.date_fulfilled=timezone.now()
        g.save()
        grocery_list= GroceryItem.objects.all()
        context = {
            'grocery_list': grocery_list
        }
        print("update-status",grocery_list)
        return HttpResponseRedirect (reverse("grocery_list:index"),context)
        
    else:
        g.status=False
        g.date_fulfilled=None
        g.save()
        grocery_list= GroceryItem.objects.all()
        context = {
            'grocery_list': grocery_list
        }
        print("update-status",grocery_list)
        print("update-status",grocery_list)
        return HttpResponseRedirect (reverse("grocery_list:index"),context)


def delete(request):
    id = request.POST['delete']
    print(id)
    g = GroceryItem.objects.get(pk=id)
    g.delete()
    grocery_list= GroceryItem.objects.all()
    print("delete",grocery_list)
    context = {
        'grocery_list': grocery_list
    }
    print("update-status",grocery_list)
    return HttpResponseRedirect (reverse("grocery_list:index"), context)

