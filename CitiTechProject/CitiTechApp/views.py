from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.urls import reverse

from .models import Event, UserChoices, User, EventSelection
from .forms import UserSignUp, UserLogin, UserChoices, ChoiceField


# Create your views here.
def index(request):
    if request.method == 'POST':
        user_login = authenticate(username=request.POST['username'], password=request.POST["password"])
        if user_login is not None:
            login(request, user_login)

            return redirect('home')
        else:
            messages.error(request, "Email or Password is incorrect")
            print()
            return redirect('index')
    context = {
        'loginForm': UserLogin
    }
    return render(request, 'CitiTechApp/index.html', context)


def signup(request):
    if request.method == 'POST':
        user_signup = UserSignUp(request.POST or None)
        if user_signup.is_valid():
            user_signup = User.objects.create_user(first_name=request.POST['first_name'],
                                                   last_name=request.POST['last_name'],
                                                   username=request.POST['username'],
                                                   email=request.POST['email'],
                                                   password=request.POST['password'])
            login(request, user_signup)
            return redirect('userChoice')
        else:
            messages.error(request, "Information already Exist!")
            return redirect('signup')
    context = {
        'UserRegistration': UserSignUp
    }
    return render(request, 'CitiTechApp/SignUp.html', context)


def userchoice(request):
    if request.method == 'POST':
        form = ChoiceField(request.POST or None)
        if form.is_valid():
            age = form.cleaned_data.get("age_group")
            skill = form.cleaned_data.get("skill_level")
            exp = form.cleaned_data.get("tech_experience")
        context = {'choice1': Event.objects.filter(event_age_group=age),
                   'choice2': Event.objects.filter(event_skill_level=skill),
                   'choice3': Event.objects.filter(event_category=exp),
                   'form': ChoiceField
                   }
        return render(request, 'CitiTechApp/userChoiceDisplay.html', context)
    context = {'choices': ChoiceField}
    return render(request, 'CitiTechApp/userChoice.html', context)


def choicedisplay(request):
    # context = {
    #
    #     'choice1': Event.objects.filter(event_age_group=),
    #     'choice2': Event.objects.filter(event_skill_level=request.session['skill_level']),
    #     'choice3': Event.objects.filter(event_category=request.session['tech_experience'])
    # }
    return render(request, 'CitiTechApp/userChoiceDisplay.html')


def home(request):
    # if Event.objects.filter(event_age_group="18 and Younger"):
    #     print(Event.event_age_group)
    # global temp, temp2, temp3
    temp = " "
    temp2 = " "
    temp3 = " "
    if request.method == 'POST':
        form = ChoiceField(request.POST or None)
        if form.is_valid():
            temp = form.cleaned_data.get("age_group")
            temp2 = form.cleaned_data.get("skill_level")
            temp3 = form.cleaned_data.get("tech_experience")

            print(temp)
            print(temp2)
            print(temp3)
            Event.objects.filter(event_age_group=temp)
            print(Event.objects.filter(event_age_group=temp))
            Event.objects.filter(event_skill_level=temp2)
            print(Event.objects.filter(event_skill_level=temp2))
            Event.objects.filter(event_category=temp3)
            print(Event.objects.filter(event_category=temp3))
    context = {
        'homeChoices': ChoiceField,
        'allEvents': Event.objects.all(),
        'eventAge': Event.objects.filter(event_age_group=temp),
        'eventSkill': Event.objects.filter(event_skill_level=temp2),
        'eventCat': Event.objects.filter(event_category=temp3)
        # 'choice1': choice1
    }
    return render(request, 'CitiTechApp/home.html', context)
