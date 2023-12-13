import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Character(models.Model):
    charName = models.CharField(max_length=20)
    human = models.CharField(max_length=20)
    sex = models.CharField(max_length=20)
    range = models.CharField(max_length=30)
    support = models.CharField(max_length=30)
    goodOrBad = models.CharField(max_length=20)
    weapons = models.CharField(max_length=40)
    otherOne = models.CharField(max_length=20)
    otherTwo = models.CharField(max_length=20)
    otherThree = models.CharField(max_length=20)

    def __str__(self):
        return self.charName
    
    def values(self):
        return Character.objects.all()
    
class Question(models.Model):
    question = models.CharField(max_length=200)
    answerOne = models.CharField(max_length=30)
    answerTwo = models.CharField(max_length=30)
    answerThree = models.CharField(max_length=30)
    answerFour = models.CharField(max_length=30)
    answerFive = models.CharField(max_length=30)
    answerSix = models.CharField(max_length=30)
    answerSeven = models.CharField(max_length=30)

    def __str__(self):
        return self.question

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answerOne = models.CharField(max_length=30)
    answerTwo = models.CharField(max_length=30)
    answerThree = models.CharField(max_length=30)
    answerFour = models.CharField(max_length=30)
    
    def __str__(self):
        return self.question.question
    

class Choice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choiceOne = models.CharField(max_length=30)
    choiceTwo = models.CharField(max_length=30)
    choiceThree = models.CharField(max_length=30)
    choiceFour = models.CharField(max_length=30)
    choiceFive = models.CharField(max_length=30)
    choiceSix = models.CharField(max_length=30)
    choiceSeven = models.CharField(max_length=30)
    choiceEight = models.CharField(max_length=30)
    choiceNine = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username
