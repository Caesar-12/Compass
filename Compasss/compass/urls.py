from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('verify', views.verify, name='verify'),
    path('validates', views.validates, name='validates'),
    path('login', views.login, name='login'),
    path('get_agenda', views.get_agenda, name='get_agenda'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('rend_tt', views.rend_tt, name='rend_tt'),
    path('goals', views.goals, name='goals'),
    path('tasks', views.tasks, name='tasks')
]
