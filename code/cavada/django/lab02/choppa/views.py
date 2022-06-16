from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from .models import UrlChoppa
from django.utils import timezone

class Code():
    def code_six(self):
        import random
        import string
        letters = string.ascii_letters
        digits = string.digits

        all_characters = letters + digits 
        pass_length = 6
        password = []
        pass_length = float(pass_length)
        while len(password) < pass_length:
            password.append(random.choice(all_characters))
        code = (''.join(password))   
        # print(temp_pass)
        # request = input("""
        # Press enter to reset your password: """)
        # print(f"""
        #     Your temporary password: {code}
        #     """)
        return code


# Create your views here.
def index(request):
    url_chopped = UrlChoppa.objects.all()
    context = {'url_chopped':url_chopped}
    return render(request,'choppa/index.html', context)

def url_chop(request):
    url_submit = request.POST['url']
    print(url_submit)
    code = Code()
    url_chopp = code.code_six()
    u = UrlChoppa(url=url_submit,pub_date=timezone.now(),url_code=url_chopp,ip_addy='')
    u.save()
    return HttpResponseRedirect (reverse("choppa:index"))

def remove(request):
    id = request.POST['remove']
    u = UrlChoppa.objects.get(pk=id)    
    u.delete()
    return HttpResponseRedirect (reverse("choppa:index"))