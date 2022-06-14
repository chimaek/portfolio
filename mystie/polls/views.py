from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Question


def index(req):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ", ".join([q.question_text for q in latest_question_list])
    # template = loader.get_template('polls/index.html')
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(req, 'index.html', context)


def detail(request, question_id):
    try:
        que = get_object_or_404(Question, pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "detail.html", {'que': que})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def temp(self, maximus):
    return HttpResponse(f"kim{maximus}")
