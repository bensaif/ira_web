from django.urls import path
from .views import *
from . import views

app_name = 'stage'
urlpatterns = [
    #path('', stage_acceuil.as_view(), name='stage'),
    path('',views.stage_acceuil, name='stage'),

    #Etudiant
    path('list_etudiant', views.list_etudiant.as_view(), name='list_etudiant'),
    path('ajout_etudiant', views.ajout_etudiant,name='ajout_etudiant'),
    #bourse alternance
    # path('bourse/ajout', views.CalendarViewNew.as_view(), name='bourse_ajout'), # ajouter bourse  
   # path('bourse/etat', views.hosting_details.as_view(), name='bourse_etat'), 
    
    #stage
    path('ajout', views.ajout_stage, name='ajout_stage'), # ajouter stage  
    #path('stage/etat', views.hosting_details.as_view(), name='stage_etat'),
   
    

]