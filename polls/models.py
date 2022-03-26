import datetime

from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Group(models.Model):
    group_name = models.CharField(max_length=150)
    days_left = models.IntegerField(default=0)
    size = Person_set.count()
    rank = ArrayField(models.IntegerField())
    def __str__ (self):
        return self.group_name

class Person(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    def __str__ (self):
        return self.name
        
class Exercise(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    def __str__ (self):
        return self.duration