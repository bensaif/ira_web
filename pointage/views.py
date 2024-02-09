from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import *
from django.contrib import messages
from .models import *

# Create your views here.
def ajout_pointage(request):
	selected_name = None
	employee_list = Employe.objects.all().order_by('nom_ar')
	if request.POST:
		selected_name = request.POST.get('nomEmp', None)
		employee_list = employee_list.filter(nom_ar=selected_name)
	employee_matricule = Employe.objects.order_by('nom_ar').values('matricule')
	context = {
			"employee_list":employee_list,
			"employee_matricule": employee_matricule
	}
	print(employee_list.query)
	print(employee_matricule.query)
	return render(request, "pointage/ajout_pointage.html", context)
