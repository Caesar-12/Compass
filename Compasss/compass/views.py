from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import UserProfile, DailyAgenda
from django.contrib.auth.models import User, auth
from django.contrib import messages
# from django.core.mail import send_mail, EmailMultiAlternatives
from .helper_funct import is_valid_email, generate_otp, send_email

import os


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
        u_email = request.POST['email']
        # print('{}'.format(request.POST))
        if request.POST['c_password'] == request.POST['password']:
            if UserProfile.objects.filter(email=u_email).exists():
                # messages.info(request, 'this {} has been used'.format(request.POST['email']))
                messages.info(request, 'Email already in use...')
                return redirect('signup')
            elif UserProfile.objects.filter(username=new_user.username).exists():
                messages.info(request, 'Username already in use...')
                return redirect('signup')
            else:
                if is_valid_email(u_email):
                    # create user
                    for k, v in request.POST.items():
                        setattr(new_user, k, v)
                    # save user
                    new_user.save()
                    os.environ['USER_MAIL'] = u_email
                    os.environ['USER_TOKEN'] = str(generate_otp())

                    return redirect('verify')
                    
                else:
                    messages.info(request, 'Invalid email...')
                    return redirect('signup')

                # return redirect('login')
        else:
            messages.info(request, 'Password does not match')
            return redirect('signup')

    return render(request, 'signup.html')


def verify(request):
    """verification"""
    send_email()
    messages.info(request, 'Verification email sent')
    return render(request, 'validates.html')

def validates(request):
    """Verifies user email"""

    if request.method == 'POST':
        if str(request.POST['vcode']) == os.getenv('USER_TOKEN'):
            v_user = UserProfile.objects.get(email=os.getenv('USER_MAIL'))
            setattr(v_user, 'status', True)
            v_user.save()
            messages.info(request, 'Verification successful')
            return render(request, 'login.html')
        else:
            messages.info(request, 'Incorrect verification code')
            return redirect('validates')
    else:
        return render(request, 'validates.html')


def login(request):
    """Receives user login data """

    if request.method == "POST":
        g_email = request.POST['email']
        g_pass = request.POST['password']
        if UserProfile.objects.filter(email=g_email).exists():
            user = UserProfile.objects.get(email=g_email)
            if user.password == g_pass:
                os.environ['USER_MAIL'] = g_email
                os.environ['USER_TOKEN'] = str(generate_otp())
                if not user.status:
                    return redirect('verify')

                return redirect('get_agenda')
            else:
                messages.info(request, 'Invalid password')
                return redirect('login')
        else:
            messages.info(request, 'User not found')
            return redirect('login')

    return render(request, 'login.html')


def get_agenda(request):
    """POSTs a user data and loads the dashboard"""
    cue = os.getenv('USER_MAIL')
    c_user = UserProfile.objects.get(email=cue)
    if DailyAgenda.objects.filter(user_id=c_user.user_id).exists():
        return render(request, 'dashboard.html')
    new_agenda = DailyAgenda()
    new_agenda.user_id = c_user
    new_agenda.save()
    return render(request, 'dashboard.html', {'u_name': c_user.username})


def create_time_table(request):
    """Creates class time table"""
    pass
    

def dashboard(request):
    """User dashboard"""
    return render(request, 'dashboard.html')


def rend_tt(request):
    """Renders timetable"""
    return render(request, 'rend_tt.html')

def goals(request):
    """Renders users goals"""
    return render(request, 'goals.html')


def tasks(request,):
    """Render users tasks"""
    return render(request, 'tasks.html')