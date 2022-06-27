from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import ShortUrl
import random, string

def index(request):
    # url item is a list of the codes and their urls
    # still need to figure out how to make the code randomly generated
    # url needs to be user input
    url_items = ShortUrl.objects.all()
    context = {'url_items':url_items}
    return render(request, 'short_url/index.html', context)

# create view to take in a url and create a code associated with it
def code(request):
    url = request.POST['url']
    code_characters = string.ascii_letters + string.digits
    code_list = []
    while 6 > len(code_list):
        code_list.append(random.choice(code_characters))
        if 6 == len(code_list):
            code = ''.join(code_list)
    url_item = ShortUrl(url=url, code=code)
    url_item.save()
    return HttpResponseRedirect(reverse('short_url:index'))

# create a view to redirect a user to a url associated with a short code
def redirect(request, code):
    url = get_object_or_404(ShortUrl, code=code)
    return HttpResponseRedirect(url.url)

    
