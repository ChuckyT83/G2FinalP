#from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

from .models import Character, Question, Answer, Choice

def index(request):
    return render(request, "polls/index.html")

@login_required
def survey(request):
    current_user = request.user
    choice_id = current_user.id
    try:
        choice = get_object_or_404(Choice, user=current_user)
    except:
        choice = Choice.objects.create(user=current_user)
    questions = Question.objects.all()
    
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

@login_required
def compare(request):
    current_user = request.user

    choices = Choice.objects.values_list("choiceOne","choiceTwo", "choiceThree", "choiceFour", "choiceFive", "choiceSix", "choiceSeven","choiceEight","choiceNine").get(user=current_user)
    countList = []
    characterCount = Character.objects.all().count()

    for i in range(characterCount): 
        #itterates through the character list and compares each character to the choices made by the user
        #then stores a count of each matching choice in a list.
        character_id = i+1
        characterTraits = Character.objects.values_list("human",'goodOrBad',"sex","support","range","weapons","otherOne","otherTwo","otherThree").get(id=character_id)
        countList.append(sum(x==y for x, y in zip(choices, characterTraits))) #compares each choice with character traits and gives a sum of total matches
    characterIndex = max(range(len(countList)), key=countList.__getitem__) + 1 #finds the index of the highest match count in the comparison list
    charPick = Character.objects.values_list("charName", flat = True).get(id=characterIndex) #pulls the character that matches the index

    return render(request, "polls/compare.html", {"charPick": charPick})

def tryAgain(request):
    return render(request, "polls/tryagain.html")


def register(request):
    if request.method != 'POST':
        form = CustomUserForm()
    else:
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/login.html')

    context = {'form': form}

    return render(request, 'polls/register.html', context)

def logoutRequest(request):
    logout(request)
    return render(request, "polls/index.html")