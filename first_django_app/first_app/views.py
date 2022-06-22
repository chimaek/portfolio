from django.http import Http404
from django.shortcuts import render, HttpResponse, get_object_or_404

# Create your views here.
from first_app.models import Question


def index(req):
    lust = Question.objects.order_by('pub_date')[:5]
    return render(req, "index.html", {'lust': lust})


def detail(req, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404(f"{question_id} does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(req, "detail.html", {'question': question})


def results(req, question_id):
    return HttpResponse(f"result: {question_id}")


def vote(req, question_id) -> HttpResponse:
    return HttpResponse(f"vote: {question_id}")


class me(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.database = 2123

    def generate(self):
        for i in range(1, self.database):
            print(i)
            yield i
