from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Glist, Gitem

def index(request):
    recent_list = Glist.objects.order_by('-date to be completed')[:6]
    context = {
        'recent_list':recent_list
    }
    return render(request, 'groceries/index.html', context)

def detail(request, glist_id):
    glist = get_object_or_404(Glist, pk=glist_id)
    return render(request, 'groceries/list.html', {'glist':glist})

def remove(request, glist_id):
    glist = get_object_or_404(Glist, pk=glist_id)
    selected = glist.items.get(pk=request.POST['item'])
    try:
        for item in selected:
            Gitem.objects.filter(id=id).delete(item)    

    except (KeyError, Gitem.DoesNotExist):
        return render(request, 'groceries/list.html', {
            'glist':glist,
            'error_message': "Please select an item or home"
        })
    
    Gitem.save()
    return render()

def createlist(request):
    glist = Glist()
    glist.glist_text = request.form['glist']
    glist.cdate = request.form['cdate']
    glist.comdate = request.form['comdate']
    glist.save()
    return HttpResponseRedirect('groceries:index.html')

def createitem(request, glist_id):
    gitem = Gitem()
    gitem.glist = glist_id
    gitem.item_text = request.form['item_text']
    gitem.item_num = request.form['item_num']
    gitem.save()
    return HttpResponseRedirect('groceries:list.html')

def compelted(request, glist_id):
    return

    


    
    
        



# Create your views here.
