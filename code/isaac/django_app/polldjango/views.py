from time import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polldjango/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question.objects.filter(pub_date__lte=timezone.now()), pk=question_id)
    return render(request, 'polldjango/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question.objects.filter(pub_date__lte=timezone.now()), pk=question_id)
    return render(request, 'polldjango/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question.objects.filter(pub_date__lte=timezone.now()), pk=question_id)
    try:
        selected_choice = question.choices.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polldjango/detail.html', {
            'question': question,
            'error_message': "Please select a choice."
        })
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polldjango:results', args=(question.id,))) 