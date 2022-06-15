from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

# Create your views here.
from .models import GroceryItem

def index(request):
    grocery_list= GroceryItem.objects.all()
    print("index",grocery_list)
    context = {
        'grocery_list': grocery_list
    }
    return render (request, 'grocery_list/index.html', context)

def add(request):
    new_item = request.POST['new']
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

# def new_item(request):
    

# def vote(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    # try:
    #     selected_choice = question.choices.get(pk=request.POST['choice'])
    # except (KeyError, Choice.DoesNotExist):
    #     return render(request, 'polls/detail.html', {
    #         'question': question,
    #         'error_message': "Please select a choice."
    #     })
    # selected_choice.votes += 1
    # selected_choice.save()
    # return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

