from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.core.signing import loads
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from django.db.models import Q

from .models import Event, UserChoices, User
from .forms import UserSignUp, UserLogin, UserChoices, ChoiceField


# Create your views here.
# def auth_user(request):
#     requestBodyInfo = loads(request.body)
#     bodyUsername = requestBodyInfo["username"]
#     bodyPassword = requestBodyInfo["password"]
#     allUsers = UserChoices.objects.filter(username=bodyUsername)
#     if (allUsers):
#             if allUsers[0].password == bodyPassword:
#                 return HttpResponse(allUsers[0].id)
#             else:
#                 return HttpResponse(False)
#         else:
#             return HttpResponse(False)
# context ={
#         'loginForm': UserLogin
#     }
#    return render(request,'CitiTechApp/auth_user.html', context)

def index(request):
    if request.method == 'POST':
        print(request.POST)
        user_login = authenticate(username=request.POST['username'], password=request.POST["password"])
        print(user_login)
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
            print(request.POST)
            user_signup = User.objects.create_user(username=request.POST['username'],
                                                   password=request.POST['password'])
            UserChoices.objects.get_or_create(userOnetoOne=user_signup, first_name=request.POST['first_name'],
                                              last_name=request.POST['last_name'],
                                              email=request.POST['email'],
                                              age_group=request.POST['age_group'],
                                              skill_level=request.POST['skill_level'],
                                              tech_experience=request.POST['tech_experience'])

            login(request, user_signup)
            return redirect('home')
        else:
            messages.error(request, "Information already Exist!")
            return redirect('signup')
    context = {
        'UserRegistration': UserSignUp
    }
    return render(request, 'CitiTechApp/SignUp.html', context)


# def userchoice(request):
#     if request.method == 'POST':
#         form = ChoiceField(request.POST or None)
#         if form.is_valid():
#             age = form.cleaned_data.get("age_group")
#             skill = form.cleaned_data.get("skill_level")
#             exp = form.cleaned_data.get("tech_experience")
#         context = {'choice1': Event.objects.filter(event_age_group=age),
#                    'choice2': Event.objects.filter(event_skill_level=skill),
#                    'choice3': Event.objects.filter(event_category=exp),
#                    'form': ChoiceField
#                    }
#         return render(request, 'CitiTechApp/home.html', context)
#     return render(request, 'CitiTechApp/userChoice.html', {'choices': ChoiceField})


def choicedisplay(request):
    if request.method == "GET":
        form = ChoiceField(request.GET or None)
        if form.is_valid():
            query = form.cleaned_data.get('age_group')
            query2 = form.cleaned_data.get('skill_level')
            query3 = request.GET.get('tech_experience')
    context = {
        'results': Event.objects.filter(event_age_group__contains=query),
        'results2': Event.objects.filter(event_skill_level__contains=query2),
        'results3': Event.objects.filter(event_category__contains=query3),
    }
    return render(request, 'CitiTechApp/userChoiceDisplay.html', context)


def home(request):
    pk = request.user
    UserChoices.objects.get(pk=request.user)
    # print(pk)
    # Event.objects.filter(event_age_group=UserChoices.userOnetoOne)
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
        'form': ChoiceField,
        # 'allEvents': Event.objects.all(),
        'eventAge': Event.objects.filter(event_age_group=temp),
        'eventSkill': Event.objects.filter(event_skill_level=temp2),
        'eventCat': Event.objects.filter(event_category=temp3),
        'userAge': Event.objects.filter(event_age_group=request.user.profile.age_group),
        'userSkill': Event.objects.filter(event_skill_level=request.user.profile.skill_level),
        'userExp': Event.objects.filter(event_category=request.user.profile.tech_experience)

        # 'choice1': Event.objects.get(event_age_group=request.age_group)
        # 'choice2': Event.objects.filter(event_skill_level=user_skill_choice),
        # 'choice3': Event.objects.filter(event_category=user_exp_choice)
    }
    return render(request, 'CitiTechApp/home.html', context)


def results(request):
    if request.method == "GET":
        query = request.GET.get('age_group')
        query2 = request.GET.get('skill_level')
        query3 = request.GET.get('tech_experience')
    context = {
        'results': Event.objects.filter(Q(event_age_group__contains=query) | Q(event_skill_level=query2) |
                                        Q(event_category=query3))
    }
    return render(request, 'CitiTechApp/results.html', context)
