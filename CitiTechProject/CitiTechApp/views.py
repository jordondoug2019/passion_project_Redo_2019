from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .models import Event, UserChoices, User
from .forms import UserSignUp, UserLogin, UserChoices, ChoiceField


# Create your views here.
def index(request):
    if request.method == 'POST':
        user_login = authenticate(username=request.POST['username'], password=request.POST["password"])
        if user_login is not None:
            login(request, user_login)
            print(User.objects.tech_experience)
            return redirect('home')
        else:
            messages.error(request, "Email or Password is incorrect")
            return redirect('logIn')
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
            return redirect('home')
        else:
            messages.error(request, "Information already Exist!")
            return redirect('signUp')
    context = {
        'UserRegistration': UserSignUp
    }
    return render(request, 'CitiTechApp/SignUp.html', context)


def home(request):
    context = {
        'homeChoices': ChoiceField,
        'event': Event.objects.all(),
        # 'choice1': choice1
    }
    return render(request, 'CitiTechApp/home.html', context)
