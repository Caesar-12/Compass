from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import UserProfile, DailyAgenda
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def index(request):
    """Homepage of the compass web app"""
    return render(request, 'index.html')


def home(request):
    pass


def signup(request):
    """Recieves user basic data for account creation"""
    new_user = UserProfile()

    if request.method == 'POST':
        # Validations
        if request.POST['c_password'] == request.POST['password']:
            if UserProfile.objects.filter(email=new_user.email).exists:
                messages.info(request, 'Email already in use...')
                return redirect('signup')
            elif UserProfile.objects.filter(user_name=new_user.username).exists:
                messages.info(request, 'Username already in use...')
                return redirect('signup')
            else:
                new_user.new()
                return redirect('login')
        else:
            messages.info(request, 'Password does not match')
            return redirect('signup')

    return render(request, 'signup.html')


def login(request):
    """Receives user login data """
    return render(request, 'login.html')


def dashboard(request):
    """Gets a user data and loads the dashboard"""
    pass
