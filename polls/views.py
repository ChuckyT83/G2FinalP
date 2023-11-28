from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Character, Question, Answer, Choice

def index(request):
    question_list = Question.objects.order_by("id")[:5]
    context = {"question_list": question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

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
    try:
        selected_answer = question.answer_set.get(request.POST["answer"])
    except (KeyError, Answer.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        if selected_answer.pk == 1:
            choice.choiceOne = selected_answer
        elif selected_answer.pk == 2:
            choice.choiceTwo = selected_answer
        selected_answer.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id)))
    
