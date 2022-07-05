from django.db.models import *

from datetime import datetime, timedelta

# 모델 추가시  py manage.py migrations <app name >
from django.utils import timezone


class Question(Model):
    question = CharField(max_length=200)
    pub_date = DateTimeField(name="pub_date")

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timedelta(days=1)

    def __str__(self):
        return self.question


class Choice(Model):
    question = ForeignKey(Question, on_delete=CASCADE)
    choice_text = CharField(max_length=100)
    votes = IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class temp(Model):
    choice = ForeignKey(Choice, on_delete=CASCADE)
    temp_text = CharField(max_length=100)

    def __str__(self):
        return self.temp_text


class me(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

