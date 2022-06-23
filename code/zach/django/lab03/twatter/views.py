from django.shortcuts import render
from userprofile.models import Member

# Create your views here.
def home(request):
    all = Member.objects.all
    context = {
        'all' : all       
    }

    return render(request, 'base.html', context)