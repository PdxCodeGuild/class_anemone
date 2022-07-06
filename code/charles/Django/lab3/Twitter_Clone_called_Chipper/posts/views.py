from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Posts
from users.models import Users



def home_page(request):
    posts= Posts.objects.order_by('-created')
    context = {
        'posts':posts
    }
    return render(request, 'posts/home_page.html', context)

def bsignup(request):
    bsing = 'text'
    bsignin = {'bsing':bsing}
    
    return render(request, 'posts/home_page.html', bsignin)


def newpost(request, userid):
    user = get_object_or_404(Users, userid)
    if user.authenticated == True:
        title=request.POST['title']
        author= Users.username.id
        body=request.POST['body']
        created=request.POST['created']
        updated_last = request.POST['updated_last']
        Posts.objects.create(title=title, author=author, body=body, created=created, updated_last=updated_last)
    else:
        error_message = 'You must be logged in to create a post'
        error = {
            'error_message':error_message
        }
        return home_page(request, error)
    
def edited(request, postid, userid):
    user = get_object_or_404(Users, pk=userid)
    post = get_object_or_404(Posts, pk=postid)
    if user != post.author:
        error_message = "You do did not create this so you cannot edit it."
        na = {
            'error_message':error_message
        }
        return render(request, 'posts:home_page.html', na)
    elif user == post.author:
        title = request.POST['title']
        body = request.POST['body']
        updated_last = request.POST['updated_last']

        post.title = title
        post.body = body
        post.updated_last = updated_last
        post.save()

def userprofile(request, reuserid):
    posts = Posts.objects.order_by('author')
    user = get_object_or_404(Users, pk=reuserid)
    pots = []
    for post in posts:
        if posts.author == user.username:
            pots.apppend['pots':post]
    return render(request, 'users/userprofile.html', pots)



# Create your views here.
