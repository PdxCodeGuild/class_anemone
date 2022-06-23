from django.shortcuts import render, get_list_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Posts


def home_page(request):
    post= Posts.objects.order_by('-created')
    context = {
        'post':post
    }
    return render(request, 'home_page.html', context)


# Create your views here.
