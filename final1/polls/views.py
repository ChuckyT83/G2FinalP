from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm
from django.contrib.auth import logout

from .models import Character, Question, Choice

def index(request):
    return render(request, "polls/index.html")

#loads the survey template that renders the questions for the survey
@login_required
def survey(request):
    current_user = request.user
    try:
        choice = get_object_or_404(Choice, user=current_user)
    except:
        choice = Choice.objects.create(user=current_user)
    questions = Question.objects.all()
    
    #saves the users choices to their associated choice model in the database
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

#compares the user's choices to the characters in the character model database then displays the result
@login_required
def compare(request):
    current_user = request.user
    try:
        choices = Choice.objects.values_list("choiceOne","choiceTwo", "choiceThree", "choiceFour", "choiceFive", "choiceSix", "choiceSeven","choiceEight","choiceNine").get(user=current_user)
    except:
        return render(request, "polls/tryagain.html")
    countList = []
    characterCount = Character.objects.all().count()

    for i in range(characterCount): 
        #itterates through the character list and compares each character to the choices made by the user
        #then stores a count of each matching choice in a list.
        character_id = i+1
        characterTraits = Character.objects.values_list("human",'goodOrBad',"sex","support","range","weapons","otherOne","otherTwo","otherThree").get(id=character_id)
        countList.append(sum(x==y for x, y in zip(choices, characterTraits))) #compares each choice with character traits and gives a sum of total matches
    characterIndex = max(range(len(countList)), key=countList.__getitem__) + 1 #finds the index of the highest match count in the comparison list. 
    #This is suboptimal as it doesn't account for results that have the same value and just pulls the first index.
    charPick = Character.objects.values_list("charName", flat = True).get(id=characterIndex) #pulls the character that matches the index

    return render(request, "polls/compare.html", {"charPick": charPick})

#renders a pages if there is an issue with saving the users results to the database
def tryAgain(request):
    return render(request, "polls/tryagain.html")

#allos the users to register an account
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