from django.shortcuts import render, get_list_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Posts
from django.contrib.auth.models import User


def home_page(request):
    posts= Posts.objects.order_by('-created')
    context = {
        'posts':posts
    }
    return render(request, 'home_page.html', context)

def newpost(request):
    title=request.POST['title']
    author= User.username.id
    body=request.POST['body']
    created=request.POST['created']
    updated_last = request.POST['updated_last']
    new = Posts.objects.create(title=title, author=author, body=body, created=created, updated_last=updated_last)
    
def edited(request, postid):
        title = request.POST['title']
        author=User.username.id
        body=request.POST['body']
        updated_last= request.POST['updated_last']
        edit =    


# Create your views here.
