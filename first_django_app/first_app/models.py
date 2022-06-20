from django.db.models import *

from datetime import datetime

#모델 추가시  py manage.py migrations <app name >

class Question(Model):
    question = CharField(max_length=200)
    pub_date = DateTimeField(auto_now=True, name="Date Published")


class Choice(Model):
    question = ForeignKey(Question, on_delete=CASCADE)
    choice_text = CharField(max_length=100)
    votes = IntegerField(default=0)
