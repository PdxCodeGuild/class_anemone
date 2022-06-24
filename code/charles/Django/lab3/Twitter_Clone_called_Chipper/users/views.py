from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def profile(request, username):
    user_profile= get_object_or_404(User, username=username)
    context={
        'user_profile':user_profile
    }
    return render(request, 'account.html', context)

def new_account(request):
    user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
    signin(request)
    return render(request, 'posts:account.html')

def signin(request):
    username=request.POST['username']
    password=request.POST['password']
    user=authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, profile(request, request.POST['username']))
    else:
        error_message = "Your password or username is not valid."
        return render(request, 'login.html', error_message)

def signout(request):
    logout(request)
    return render(request, 'posts:home_page')

@login_required(login_url='users:signin')
def editprofile(request):
    user = request.POST['username']
    data = User.objects.all()

    for x in data:
        if user == x:
            x.username = user
            x.password = request.POST['password']
            if request.POST['email'] != request.POST['blank=True']:
                x.email = request.POST['email']
            if request.POST['first_name'] != request.POST['blank=True']:
                x.first_name = request.POST['first_name']
            if request.POST['last'] != request.POST['blank=True']:
                x.last_name = request.POST['last_name']
            x.save()
            return render(request, 'posts:account.html')

    


# Create your views here.
