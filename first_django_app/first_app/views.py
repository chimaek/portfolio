from django.shortcuts import render, HttpResponse

# Create your views here.
from first_app.models import Question


def index(req):
    lust = Question.objects.order_by('pub_date')[:5]
    # output = ','.join([q.question for q in lust])
    # return render(req, 'index.html', {'date': lust})
    con = {'lust', lust}
    return render(req, "index.html", {'lust': lust})


def detail(req, question_id):
    return HttpResponse(f'detail :{question_id}')


def results(req, question_id):
    return HttpResponse(f"result: {question_id}")


def vote(req, question_id) -> HttpResponse:
    return HttpResponse(f"vote: {question_id}")
