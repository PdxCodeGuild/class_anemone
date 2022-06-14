from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Gitem

def index(request):
    recent_item = Gitem.objects.order_by('-comdate')
    context = {
        'recent_item':recent_item
    }
    return render(request, 'groceries/index.html', context)

# def detail(request, gitem_id):
#     gitem = get_object_or_404(Gitem, pk=gitem_id)
#     recent_item = Gitem.objects.all()
#     context = {
#         'recent_item':recent_item
#     }
#     return render(request, 'groceries/index.html', {'gitem':gitem})

# def remove(request, gitem_id):
#     gitem = get_object_or_404(Gitem, pk=gitem_id)
#     selected = Gitem.items.get(pk=request.POST['item'])
#     try:
#         for item in selected:
#             Gitem.objects.filter(id=id).delete(item)    

#     except (KeyError, Gitem.DoesNotExist):
#         return render(request, 'groceries/list.html', {
#             'gitem':gitem,
#             'error_message': "Please select an item or home"
#         })
    
#     Gitem.save()
#     return render()
#  <form action="{% url 'groceries:createitem'%}" method="post">
#         {% csrf_token %}
#         <h1>New item</h1>
#         <input type="text" name="item_text" id="item_text" value=""><label for="gitem_text">Item Name</label><br>
#         <input type="text" name="item_num" id="item_num" value=""><label for="item_num">Item number</label><br>
#         <input type="date" name="cdate" id="cdate"><label for="cdate">Create Date</label><br>
#         <input type="date" name="comdate" id="comdate"><label for="comdate">Complete Date</label><br>
#         <input type="submit" value="create">
#     </form> 

# def createlist(request):
#     gitem= Gitem.objects.all()
#     gitem_text = request.POST['Gitem_text']
#     cdate = request.POST['cdate']
#     comdate = request.POST['comdate']
#     data = gitem_text, cdate, comdate
#     Gitem.save(data)
#     return index()

def createitem(request, ):
    gitem = Gitem.objects.create(request.P, created_date= timezone.now())
    nitem_text = request.POST['item_text']
    nitem_num = request.POST['item_num']
    new_item=Gitem.items.create(Gitem, item_text= nitem_text, item_num=nitem_num, status = 'No')
    Gitem().save(new_item)
    return HttpResponseRedirect(reverse('groceries/list.html', args=(gitem.id,)))

# def compelted(request, Gitem_id):
#     return

    


    
    
        



# # Create your views here.
