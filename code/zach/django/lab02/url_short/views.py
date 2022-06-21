from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
    return render(request, 'url_short/base.html')