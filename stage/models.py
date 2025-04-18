# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Benefice(models.Model):
    id_benefice = models.AutoField(primary_key=True)
    critere_logement = models.IntegerField(blank=True, null=True)
    critere_repas = models.IntegerField(blank=True, null=True)
    critere_bourse = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'benefice'
        app_label= 'stage'


class Bourse(models.Model):
    id_bourse = models.AutoField(primary_key=True)
    type_bourse = models.CharField(max_length=255, blank=True, null=True)
    prise_en_charge = models.CharField(max_length=1024, blank=True, null=True)
    montant_total = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    frais_transport = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    frais_participation = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    date_attribution = models.DateField(blank=True, null=True)
    id_stage = models.ForeignKey('Stage', models.DO_NOTHING, db_column='id_stage')

    class Meta:
        managed = True
        db_table = 'bourse'
        app_label= 'stage'


class Chercheur(models.Model):
    id_chercheur = models.AutoField(primary_key=True)
    num_cin = models.IntegerField()
    id_ira = models.IntegerField()
    email = models.CharField(max_length=255, blank=True, null=True)
    statut = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'chercheur'
        app_label= 'stage'


class Destination(models.Model):
    id_destination = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=1024, blank=True, null=True)
    pays = models.CharField(max_length=1024, blank=True, null=True)
    ville = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'destination'
        app_label= 'stage'


class Etudiant(models.Model):
    id_etudiant = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=255)
    date_naissannce = models.DateField()
    lieu_naissance = models.CharField(max_length=255)
    num_identite = models.IntegerField()
    email = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    choixStatut=(
        ('طالب','طالب'),
        ('طالبة','طالبة')
    )
    statut = models.CharField(max_length=255, choices=choixStatut)
    choixFiliere=(
        ('دكتوراه','دكتوراه'),
        ('ماجيستير','ماجيستير')
    )
    filiere = models.CharField(max_length=255, choices=choixFiliere)
    choixNiveau=(
		('الأولى','الأولى'),
		('الثانية','الثانية'),
		('الثالثة','الثالثة'),
		('الرابعة','الرابعة'),
		('الخامسة','الخامسة'),
	)
    niveau = models.CharField(max_length=255, choices=choixNiveau)

    class Meta:
        managed = True
        db_table = 'etudiant'
        unique_together = ["nom", "prenom", "num_identite"]


class Stage(models.Model):
    id_stage = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=255, blank=True, null=True)
    sujet = models.CharField(max_length=1024, blank=True, null=True)
    date_aller = models.DateField(blank=True, null=True)
    date_retour = models.DateField(blank=True, null=True)
    id_etudiant = models.ForeignKey(Etudiant, models.DO_NOTHING, db_column='id_etudiant', blank=True, null=True)
    id_chercheur = models.ForeignKey(Chercheur, models.DO_NOTHING, db_column='id_chercheur', blank=True, null=True)
    id_benefice = models.ForeignKey(Benefice, models.DO_NOTHING, db_column='id_benefice')
    id_destination = models.ForeignKey(Destination, models.DO_NOTHING, db_column='id_destination')

    class Meta:
        managed = True
        db_table = 'stage'
        app_label= 'stage'
