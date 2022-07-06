from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Users

def profile(request, username):
    user_profile= get_object_or_404(Users, username=username)
    print(user_profile)
    context={
        'user_profile':user_profile
    }
    return render(request, 'users/account.html', context)

def new_account(request):
    user = Users.objects.create(username=request.POST['username'], password=request.POST['password'], email=request.POST['email'], first_name=request.POST['first_name'], last_name=request.POST['last_name'])
    signin(request)
    return render(request, 'users/account.html')

def signin(request):
    username=request.POST['username']
    password=request.POST['password']
    user=authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        for log in Users:
            if username == Users.username:
                Users.authenticated = True
        return profile(request, request.POST['username'])
    else:
        error_message = "Your password or username is not valid."
        return render(request, 'login.html', error_message)

def signout(request, userid):
    username = get_object_or_404(Users, userid)
    username.authenticated = False
    logout(request)
    return render(request, 'posts:home_page')

@login_required(login_url='users:signin')
def editprofile(request):
    user = request.POST['username']
    data = Users.objects.all()

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
