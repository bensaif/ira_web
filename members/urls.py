from django.urls import path
from .views import *
from . import views

app_name = 'members'
urlpatterns = [

    #User paths
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user'),
]