from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic
from django.views.generic import View
from .forms import *
from .models import *

# Create your views here.
def stage_acceuil(request):
    return render(request, 'stage/accueil.html')

def ajout_etudiant(request):
	#etudiant_list = Etudiant.objects.all().order_by('num_identite')
	submitted = False
	# if this is a POST request we need to process the form data
	if request.method == "POST":
		# create a form instance and populate it with data from the request:
		etudiant_form = EtudiantForm(request.POST)
		# check whether it's valid:
		if etudiant_form.is_valid():
			# process the data in form.cleaned_data as required
			etudiant_form.save()
			# redirect to a new URL:
			return 	HttpResponseRedirect('./ajout_etudiant?submitted=True')
			#messages.success(request, 'Nouveau étudiant ajouté')
		else:
			return HttpResponse("Remplir les champs vides")
	# if a GET (or any other method) we'll create a blank form
	else:
		etudiant_form = EtudiantForm

	return render(request, 'stage/nouveau_etudiant.html',{'etudiant_form':etudiant_form})

def search_etudiant(request):
	if request.method == "POST":
		searched = request.POST['searched']
		etudiants = Etudiant.objects.filter(prenom__contains=searched)
		return render(request, 'stage/search_etudiant.html', {'etudiants':etudiants, 'searched': searched})
	else:
		return render(request,'stage/search_etudiant.html',{})


class list_etudiant(View):
    #login_url = "guesthouse:signin"
    template_name = "stage/list_etudiant.html"

    def get(self, request, *args, **kwargs):
        
        all_student = Etudiant.objects.all().order_by('-nom')#.values('idreservation','administration','datedeb','datefin')
       
        # if filters applied then get parameter and filter based on condition else return object
        context = {
            "all_student":all_student,
        }
        return render(request, self.template_name, context)




def ajout_stage(request):
	#submitted = False
	
	if request.method == "POST":
		#if request.user.is_superuser:
			stage_form = StageForm(request.POST)
			etudiant_form = EtudiantForm(request.POST)
			if stage_form.is_valid() and etudiant_form.is_valid():
				stage_form.save()
				etudiant_form.save()
				return HttpResponse("Enregistrer")
			else:
				return HttpResponse("Vérifier les champs vides")
	else:
		# Just Going To The Page, Not Submitting 
		stage_form = StageForm
		etudiant_form = EtudiantForm

	return render(request, 'stage/nouveau_stage.html', {'stage_form':stage_form,'etudiant_form':etudiant_form})

