from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Gitem
import datetime

def index(request):
    recent_item = Gitem.objects.order_by('status','comdate')
    context = {
        'recent_item':recent_item
    }
    return render(request, 'groceries/index.html', context)


def createitem(request):
    if request.method == 'POST':
        newitem = Gitem.objects.create(item_text = request.POST['item_text'], item_num = request.POST['item_num'], cdate= datetime.datetime.now(), comdate= request.POST['comdate'], status= False)
        return HttpResponseRedirect(reverse('groceries:index'))


def delete(request):
    recent_item = Gitem.objects.order_by('status','comdate')
    context = {
        'recent_item':recent_item
    }
    return render(request, 'groceries/delete.html', context)


def deleteitem(request):
    print(request.POST)
    if request.method == 'POST':
        for item in request.POST:
            d = get_object_or_404(Gitem, pk=request.POST['check'])
            print(d)
            Gitem.delete(d)
            return HttpResponseRedirect(reverse('groceries:delete'))

def status(request):
    recent_item = Gitem.objects.order_by('status','comdate')
    context = {
        'recent_item':recent_item
    }
    return render(request, 'groceries/status.html', context)


def statusupdate(request):
    print(request.POST)
    if request.method == 'POST':
        for item in request.POST:
            d = get_object_or_404(Gitem, pk=request.POST['check'])
            print(d.status)
            if d.status == False:
                d.status = True
                d.save()
                print(d.status)
            elif d.status == True:
                d.status = False
                d.save()
                print(d.status)
                
            return HttpResponseRedirect(reverse('groceries:status'))

# # Create your views here.
