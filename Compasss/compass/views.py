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

    if request.method == "POST":
        # Validations
        print('{}'.format(request.POST))
        if request.POST['c_password'] == request.POST['password']:
            if UserProfile.objects.filter(email=request.POST['email']).exists():
                messages.info(request, 'this {} has been used'.format(request.POST['email']))
                messages.info(request, 'Email already in use...')
                return redirect('signup')
            elif UserProfile.objects.filter(username=new_user.username).exists():
                messages.info(request, 'Username already in use...')
                return redirect('signup')
            else:
                for k, v in request.POST.items():
                    setattr(new_user, k, v)

                new_user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password does not match')
            return redirect('signup')

    return render(request, 'signup.html')


def login(request):
    """Receives user login data """
    if request.POST:
        g_email = request.POST['email']
        g_pass = request.POST['password']

    if request.method == "POST":
        if UserProfile.objects.filter(email=g_email).exists():
            user = UserProfile.objects.get(email=g_email)
            if user.password == g_pass:
                return render(request, 'dashboard.html')
            else:
                messages.info(request, 'Invalid password')
                return redirect('login')
        else:
            messages.info(request, 'User not found')
            return redirect('login')

    return render(request, 'login.html')


def dashboard(request):
    """POSTs a user data and loads the dashboard"""
    pass
