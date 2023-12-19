from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login_details', views.login_details, name='login_details'),
    path('match', views.match, name='match')
]
