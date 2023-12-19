from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    """Homepage of the compass web app"""
    return render(request, 'index.html')


def home(request):
    pass


def signup(request):
    """Recieves user basic data for account creation"""
    return render(request, 'signup.html')


def login_details(request):
    """Receives user login data """
    user_data = {}
    for data in ['firstName', 'lastName', 'age', 'ed_level']:
        user_data[data] = request.POST[data]

    return render(request, 'login_details.html')


def match(request):
    """Checks if a user already exists or not"""
    user_log_det = {}
    for detail in ['email', 'password', 'c_password']:
        user_log_det[detail] = request.POST[detail]
    if user_log_det['password'] != user_log_det['c_password']:
        login_details(request)
    return render(request, 'matc.html')


def dashboard(request):
    """Gets a user data and loads the dashboard"""
    pass
