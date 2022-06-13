from django.shortcuts import render

from .models import List, Choice

def index(request):
    latest_grocery_list = List.objects.order_by('-pub_date')[:5]
    context = {
        'latest_grocery_list': latest_grocery_list
    }
    return render(request, 'grocery/index.html', context)
