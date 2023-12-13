from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Character, Question, Answer, Choice

def index(request):
    return render(request, "polls/index.html")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    current_user = request.user
    choice_id = current_user.id
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
            return compare(request)
    return render(request, "polls/detail.html", {"question": question})

def results(request):
    question_list = Question.objects.order_by("id")
    choice_list = Choice.objects.filter(user = 1).values()
    questions = {"question_list": question_list}
    choices = {"choice_list": choice_list}
    print(choices)
    print(choice_list)
    return render(request, "polls/results.html", {"question_list": question_list, "choice_list": choice_list})

def survey(request):
    current_user = request.user
    choice_id = current_user.id
    choice = get_object_or_404(Choice, pk=choice_id)
    questions = Question.objects.all()
    print(questions)
    
    if request.method=="POST":
        try:
            choice.choiceOne = request.POST.get("answer1")
            choice.choiceTwo = request.POST.get("answer2")
            choice.choiceThree = request.POST.get("answer3")
            choice.choiceFour = request.POST.get("answer4")
            choice.choiceFive = request.POST.get("answer5")
            choice.choiceSix = request.POST.get("answer6")
            choice.choiceSeven = request.POST.get("answer7")
            choice.choiceEight = request.POST.get("answer8")
            choice.choiceNine = request.POST.get("answer9")
            choice.save()
            return compare(request)
        except:
            return render(request, "polls/tryagain.html")
    return render(request, "polls/survey.html", {"questions": questions})

def vote(request, question_id):
    choice_id = 1
    question = get_object_or_404(Question, pk=question_id)
    choice = get_object_or_404(Choice, pk=choice_id)
    answer = request.POST['answer']
    choice.choiceOne = answer
    return HttpResponse(request, "polls/index.html")

def compare(request):
    current_user = request.user
    choice_id = current_user.id
    choices = Choice.objects.values_list("choiceOne","choiceTwo", "choiceThree", "choiceFour", "choiceFive", "choiceSix", "choiceSeven","choiceEight","choiceNine").get(id=choice_id)
    print(choices)
    countList = []
    for i in range(27):
        character_id = i+1
        characterTraits = Character.objects.values_list("human",'goodOrBad',"sex","support","range","weapons","otherOne","otherTwo","otherThree").get(id=character_id)
        countList.append(sum(x==y for x, y in zip(choices, characterTraits)))
        print(list(zip(choices, characterTraits)))
        print(countList)
    characterIndex = max(range(len(countList)), key=countList.__getitem__) + 1
    print(characterIndex)
    print(Character.objects.values_list("charName", flat = True).get(id=characterIndex))
    charPick = Character.objects.values_list("charName", flat = True).get(id=characterIndex)
    print(charPick)
    return render(request, "polls/compare.html", {"charPick": charPick})