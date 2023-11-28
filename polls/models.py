import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class Character(models.Model):
    charName = models.CharField(max_length=20)
    race = models.CharField(max_length=20)
    sex = models.CharField(max_length=20)
    charClass = models.CharField(max_length=20)
    support = models.CharField(max_length=20)
    goodOrBad = models.CharField(max_length=20)
    weapons = models.CharField(max_length=40)
    otherOne = models.CharField(max_length=20)
    otherTwo = models.CharField(max_length=20)
    otherThree = models.CharField(max_length=20)

    def __str__(self):
        return self.charName
    
    def was_published_recently(self):
         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def values(self):
        return Character.objects.all()
    
class Question(models.Model):
    question = models.CharField(max_length=200)
    answerOne = models.CharField(max_length=30)
    answerTwo = models.CharField(max_length=30)

    def __str__(self):
        return self.question

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answerOne = models.CharField(max_length=30)
    answerTwo = models.CharField(max_length=30)

class Choice(models.Model):
    choiceOne = models.CharField(max_length=30)
    choiceTwo = models.CharField(max_length=30)
    choiceThree = models.CharField(max_length=30)
    choiceFour = models.CharField(max_length=30)




