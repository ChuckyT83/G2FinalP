from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Character, Question, Answer, Choice

def index(request):
    question_list = Question.objects.order_by("id")
    context = {"question_list": question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choice_id = 1
    choice = get_object_or_404(Choice, pk=choice_id)
    if request.method=="POST":
        answer = request.POST['answer']
        if question_id == 1:
            choice.choiceOne = answer
        elif question_id == 2:
            choice.choiceTwo = answer
        elif question_id == 3:
            choice.choiceThree = answer
        elif question_id == 4:
            choice.choiceFour = answer
        print(answer)
        choice.save()
        try:
            question_id = question_id + 1
            question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            question_list = Question.objects.order_by("id")
            questions = {"question_list": question_list}
            return render(request, "polls/index.html", questions)
    return render(request, "polls/detail.html", {"question": question})

def results(request):
    question_list = Question.objects.order_by("id")
    choice_list = Choice.objects.get(id=1)
    questions = {"question_list": question_list}
    choices = {"choice_list": choice_list}
    print(choices)
    print(choice_list)
    return render(request, "polls/results.html", questions, choices)

def survey(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/survey.html", {"question": question})

def vote(request, question_id):
    choice_id = 1
    question = get_object_or_404(Question, pk=question_id)
    choice = get_object_or_404(Choice, pk=choice_id)
    answer = request.POST['answer']
    choice.choiceOne = answer
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    return HttpResponseRedirect(reverse(request, "polls/index.html"))
    
