import code, random, string
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from .models import ShortUrlCode

def index(request):
    url_info = ShortUrlCode.objects.order_by('-create_date')
    context = {
        'url_info': url_info
    }
    return render(request, 'short_url/index.html', context)


def generate_code():
    code = ''
    alphanumeric = string.ascii_letters + '123456789'

    for i in range(6):
        code += random.choice(alphanumeric)

    return code


def add(request):
    url = request.POST.get('url', False) # get the value the user entered into the 'url' field
    create_date = timezone.now()    
    code = generate_code()
    
    add_code = ShortUrlCode(code=code, url=url, create_date=create_date) # create an instance of our model
    add_code.save() # save a new row to the database
    return HttpResponseRedirect(reverse('short_url:index'))


def redirect(request, code):
    url = get_object_or_404(ShortUrlCode, code=code)
    try:
        entered_code = url.get(code=request.POST['code'])
    except (KeyError, ShortUrlCode.DoesNotExist):
        return render(request, 'short_url/index.html', {
            'code': code,
            'error_message': "Code not found. Please enter a valid short URL code from the above list."
        })
    return HttpResponseRedirect(url)

