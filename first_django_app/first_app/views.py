from django.shortcuts import render, HttpResponse

# Create your views here.
from first_app.models import Question


def index(req):
    lust = Question.objects.order_by('Date Published')[:5]
    return render(req, 'index.html', {'date': lust})
