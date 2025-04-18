from django import forms
from django.forms import ModelForm
from .models import Etudiant, Chercheur, Destination, Bourse, Stage, Benefice


# Create Etudiant Form
class EtudiantForm(ModelForm):
	class Meta:
		model = Etudiant
		fields = ('id_etudiant', 'nom', 'prenom','date_naissannce', 'lieu_naissance', 'num_identite', 'email', 'telephone', 'adresse', 'statut', 'filiere', 'niveau')
		labels = {
			'id_etudiant': '',
			'nom': 'Nom *',
			'prenom': 'Prénom *',
			'date_naissannce': 'Date de naissance *',
			'lieu_naissance': 'Lieu de naissance *',
			'num_identite': 'NCIN *',
			'email': 'Email:',
			'telephone': 'N°Téléphone:',
			'adresse': 'Adresse:',
			'statut': 'Statut:',
			'filiere': 'Filière:',
			'niveau': 'Niveau:',			
		}
		widgets = {
			'id_etudiant': forms.TextInput(attrs={'class':'forms-group__input'}),
			'nom': forms.TextInput(attrs={'class':'forms-group__input', 'placeholder':'Nom'}),
			'prenom': forms.TextInput(attrs={'class':'forms-group__input', 'placeholder':'Prénom'}),
			'date_naissannce': forms.DateInput(format=('%Y-%m-%d'),attrs={'class':'forms-group__input', 'placeholder':'Date de naissance','type': 'date'}),
			'lieu_naissance': forms.TextInput(attrs={'class':'forms-group__input', 'placeholder':'Lieu de Naissance'}),
			'num_identite':forms.TextInput(attrs={'class':'forms-group__input', 'placeholder':'Num Identité'}),
			'email':forms.EmailInput(attrs={'class':'forms-group__input', 'placeholder':'Email'}), 
			'telephone':forms.TextInput(attrs={'class':'forms-group__input', 'placeholder':'Téléphone'}), 
			'adresse':forms.Textarea(attrs={'class':'forms-group__input', 'placeholder':'Adresse','rows':4, 'cols':18}), 
			'statut':forms.Select(attrs={'class':'form-select', 'placeholder':'Statut'}), 
			'filiere':forms.Select(attrs={'class':'form-select', 'placeholder':'Filière'}), 
			'niveau':forms.Select(attrs={'class':'form-select', 'placeholder':'Niveau'}),
		}

# Create Chercheur Form
class ChercheurForm(ModelForm):
	class Meta:
		model = Chercheur
		fields = ('id_chercheur', 'num_cin', 'id_ira', 'email', 'statut')
		labels = {
			'id_chercheur': '',
			'num_cin': 'XXXXXXXX',
			'id_ira': 'XXXXX',
			'email': 'exemple@nomdomaine.com',
			'statut': '',
		}
		widgets = {
			'id_chercheur': forms.TextInput(attrs={'class':'form-control'}),
			'num_cin':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Num Identité'}),
			'id_ira': forms.Select(attrs={'class':'form-select', 'placeholder':"Identifiant de l'IRA"}),
			'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}), 
			'statut': forms.Select(attrs={'class':'form-control', 'placeholder':'Statut'}),
		}


# Create Destination form
class DestinationForm(ModelForm):
	class Meta:
		model = Destination
		fields = ('id_destination', 'libelle', 'pays', 'ville')
		labels = {
			'id_destination': '',
			'libelle': '',
			'pays': '',
			'ville': '',	
		}
		widgets = {
			'id_destination': forms.TextInput(attrs={'class':'form-control'}),
			'libelle': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Nom de l'établissement"}),
			'pays': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Pays de l'établissement"}),
			'ville': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Ville de l'établissement"}),
		}

# Create Benefice form
class BeneficeForm(ModelForm):
	class Meta:
		model = Benefice
		fields = ('id_benefice', 'critere_logement', 'critere_repas', 'critere_bourse')
		labels = {
			'id_benefice': '',
			'critere_logement': '',
			'critere_repas': '',
			'critere_bourse': '',	
		}
		widgets = {
			'id_benefice': forms.TextInput(attrs={'class':'form-control'}),
			'critere_logement': forms.CheckboxInput(attrs={'class':'required checkbox form-control'}),
			'critere_repas': forms.CheckboxInput(attrs={'class':'required checkbox form-control'}),
			'critere_bourse': forms.CheckboxInput(attrs={'class':'required checkbox form-control'}),
		}

# Create Stage Form
class StageForm(ModelForm):
	class Meta:
		model = Stage
		fields = ('id_stage', 'titre', 'sujet','date_aller', 'date_retour', 'id_etudiant', 'id_chercheur', 'id_destination', 'id_benefice')
		labels = {
			'id_stage': '',
			'titre': '',
			'sujet': '',
			'date_aller': 'YYYY-MM-DD',
			'date_retour': 'YYYY-MM-DD',
			'id_etudiant': '',
			'id_Chercheur': '',
			'id_destination': '',
			'id_benefice': '',	
		}
		widgets = {
			'id_stage': forms.TextInput(attrs={'class':'form-control'}),
			'titre': forms.TextInput(attrs={'class':'form-control'}),
			'sujet': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Sujet du stage'}),
			'date_aller': forms.DateInput(attrs={'class':'form-control', 'placeholder':"Date d'aller"}),
			'date_retour':forms.TextInput(attrs={'class':'form-control', 'placeholder':"Date du retour"}),
			'id_etudiant':forms.EmailInput(attrs={'class':'form-control'}),
			'id_Chercheur':forms.TextInput(attrs={'class':'form-control'}),
			'id_destination':forms.TextInput(attrs={'class':'form-control'}),
			'id_benefice':forms.TextInput(attrs={'class':'form-control'}),
		}

# Create Bourse Form
class BourseForm(ModelForm):
	class Meta:
		model = Bourse
		fields = ('id_bourse', 'type_bourse', 'prise_en_charge','montant_total', 'frais_transport', 'frais_participation', 'date_attribution', 'id_stage')
		labels = {
			'id_bourse': '',
			'type_bourse': '',
			'prise_en_charge': '',
			'montant_total': '',
			'frais_transport': '',
			'frais_participation': '',
			'date_attribution': '',	
			'id_stage': '',	
		}
		widgets = {
			'id_bourse': forms.TextInput(attrs={'class':'form-control'}),
			'type_bourse': forms.TextInput(attrs={'class':'form-control'}),
			'prise_en_charge': forms.Select(attrs={'class':'form-control', 'placeholder':'Sujet du stage'}),
			'montant_total': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Montant total"}),
			'frais_transport': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Frais du transport"}),
			'frais_participation': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Frais du participation"}),
			'date_attribution': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Date d'attribution"}),
			'id_stage':forms.EmailInput(attrs={'class':'form-control'}),
		}
