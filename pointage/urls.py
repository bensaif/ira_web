from django.urls import path
from .views import *
from . import views

app_name = 'pointage'
urlpatterns = [
    #Details
    path('pointage/ajout/', views.ajout_pointage, name='ajout_pointage'),

]
