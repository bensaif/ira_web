from django import forms
from django.forms import ModelForm
from guesthouse.models import *
from .widget import *

# Create a venue form
class PointageForm(ModelForm):
	class Meta:
		model = Pointage
		fields = ('mat', 'annee', 'mois', 'du', 'au', 'presence', 'absence')
		labels = {
			'mat': '',
			'annee': '',
			'mois': '',
			'du': 'Du',
			'au': 'Au',
			'presence': 'Présent(e)',
			'absence': 'Absent(e)',			
		}
		widgets = {
			'mat': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Nom d'Employé"}),
			'annee': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Année'}),
			'mois': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Mois'}),
			'du': DatePickerInput(),
			'au': DatePickerInput(),
			'presence': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':''}),
			'absence': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':''}),
		}