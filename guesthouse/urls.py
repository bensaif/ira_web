from django.urls import path
from .views import *
from . import views

app_name = 'guesthouse'
urlpatterns = [
    path('', gh_acceuil.as_view(), name='gh'),

    # Hébergement
    #path('hebergement/calendrier', views.CalendarView.as_view(), name='host_calendar'), #Calendar for Hosting

    #Calendars
    path('reservation/calendrier', views.CalendarViewNew.as_view(), name='reserve_calendar'), # Calendar for reservation  
    path('hebergement/calendrier', views.CalendarViewHosting.as_view(), name='hosting_calendar'), # Calendar for hosting 
    path("hebergement/calendrier", views.CalendarView.as_view(), name="calendar"),
    
    #Details
    path('reservation/details/', views.reserve_details.as_view() , name='reserve_details'),
    path('hebergement/details', views.hosting_details.as_view(), name='hosting_details'),
    

]
