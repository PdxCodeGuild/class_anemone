from django.http import HttpResponse

def index(request):

    # questions = Question.objects.all()

    return HttpResponse("Hello world!")