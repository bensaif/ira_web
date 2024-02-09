# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Chambre(models.Model):
    idchambre = models.AutoField(primary_key=True)
    numero = models.CharField(max_length=11)
    type = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    prix = models.FloatField()
    maison = models.CharField(max_length=10)
    chambre = models.CharField(max_length=10)
    etage = models.IntegerField()
    local = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'chambre'


class Client(models.Model):
    idclient = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    numid = models.CharField(max_length=30, blank=True, null=True)
    genre = models.CharField(max_length=10, blank=True, null=True)
    datenaiss = models.DateField(blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=205, blank=True, null=True)
    telephone = models.CharField(max_length=45, blank=True, null=True)
    profession = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employe(models.Model):
    idemploye_cadeau = models.AutoField(primary_key=True)
    matricule = models.CharField(unique=True, max_length=45)
    nom_ar = models.CharField(max_length=255)
    service = models.CharField(max_length=255)
    nom_fr = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employe'


class Facture(models.Model):
    idfacture = models.AutoField(primary_key=True)
    idres = models.IntegerField(blank=True, null=True)
    idheb = models.IntegerField(blank=True, null=True)
    date = models.DateField()
    njours = models.IntegerField(blank=True, null=True)
    statut = models.CharField(max_length=45)
    ln = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facture'


class HbgRecap(models.Model):
    idhebergement_recap = models.AutoField(primary_key=True)
    idhebg = models.IntegerField(db_column='idHebg')  # Field name made lowercase.
    idresv = models.IntegerField(db_column='idResv', blank=True, null=True)  # Field name made lowercase.
    etablissement = models.CharField(max_length=512)
    dateh = models.DateField(db_column='dateH')  # Field name made lowercase.
    dates = models.DateField(db_column='dateS')  # Field name made lowercase.
    nuitee = models.IntegerField()
    capacite = models.IntegerField()
    statut = models.CharField(max_length=255)
    nc = models.CharField(db_column='nC', max_length=45)  # Field name made lowercase.
    statp = models.CharField(db_column='statP', max_length=45)  # Field name made lowercase.
    moyen = models.CharField(max_length=255)
    codeclient = models.CharField(max_length=45, blank=True, null=True)
    demandeur = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'hbg_recap'


class Hebergement(models.Model):
    idhebergement = models.IntegerField()
    roomnum = models.CharField(max_length=20)
    nomclient = models.CharField(max_length=255)
    note = models.CharField(max_length=2000, blank=True, null=True)
    reservid = models.IntegerField(blank=True, null=True)
    dateheberg = models.DateField()
    datesortie = models.DateField()
    nuitee = models.IntegerField()
    statutchambre = models.CharField(max_length=50)
    type = models.CharField(max_length=20, blank=True, null=True)
    etablissement = models.CharField(max_length=1024)
    sujet = models.CharField(max_length=512, blank=True, null=True)
    priseencharge = models.CharField(max_length=45, blank=True, null=True)
    categorie = models.CharField(max_length=25, blank=True, null=True)
    demandeur = models.CharField(max_length=100)
    ncourrierh = models.IntegerField()
    statuthebg = models.CharField(max_length=45, blank=True, null=True)
    capacite = models.IntegerField(blank=True, null=True)
    slno = models.AutoField(primary_key=True)
    capgroup = models.IntegerField()
    compt = models.IntegerField()
    statpay = models.CharField(db_column='statPay', max_length=45)  # Field name made lowercase.
    moyen = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hebergement'


class Payement(models.Model):
    idpayement = models.AutoField(primary_key=True)
    code_client = models.CharField(max_length=25)
    statutpay = models.CharField(max_length=11)
    resid = models.IntegerField(blank=True, null=True)
    hebgid = models.IntegerField(blank=True, null=True)
    datepay = models.DateField(blank=True, null=True)
    montant = models.CharField(max_length=13)
    note = models.CharField(max_length=1024, blank=True, null=True)
    idencaisse = models.CharField(max_length=125)
    nencaisse = models.CharField(max_length=13)
    dateencaisse = models.DateField()
    ln = models.CharField(max_length=45, blank=True, null=True)
    numpay = models.IntegerField(db_column='numPay')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payement'


class Pointage(models.Model):
    idpointage = models.AutoField(primary_key=True)
    mat = models.ForeignKey(Employe, models.DO_NOTHING, db_column='mat')
    annee = models.TextField()  # This field type is a guess.
    mois = models.DateTimeField()
    du = models.DateTimeField()
    au = models.DateTimeField()
    presence = models.IntegerField()
    absence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pointage'


class Reservation(models.Model):
    idreservation = models.IntegerField(primary_key=True)
    administration = models.CharField(max_length=255)
    coordinateur = models.CharField(max_length=250)
    codeclient = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=250)
    datedeb = models.DateField()
    datefin = models.DateField()
    nbrejours = models.IntegerField()
    logement = models.IntegerField(blank=True, null=True)
    nbrepersonne = models.IntegerField()
    salle = models.CharField(max_length=95)
    typeh = models.CharField(max_length=70, blank=True, null=True)
    piecejointe = models.TextField(blank=True, null=True)
    noter = models.CharField(max_length=2000, blank=True, null=True)
    lieu = models.CharField(max_length=255, blank=True, null=True)
    ncourrier = models.IntegerField()
    statutres = models.CharField(max_length=45)
    capreservation = models.IntegerField()
    nbrepcafe = models.IntegerField()
    nbredej = models.IntegerField()
    statres = models.CharField(db_column='statRes', max_length=45)  # Field name made lowercase.
    moyen = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'reservation'


class Restauration(models.Model):
    idrestauration = models.AutoField(primary_key=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    prix = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restauration'


class Salle(models.Model):
    idsalle = models.AutoField(primary_key=True)
    type = models.CharField(max_length=95)
    prix = models.FloatField()
    local = models.CharField(max_length=125)

    class Meta:
        managed = False
        db_table = 'salle'


class Session(models.Model):
    idsession = models.AutoField(primary_key=True)
    pseudo = models.CharField(max_length=45)
    connexion = models.DateTimeField(blank=True, null=True)
    deconnexion = models.DateTimeField(blank=True, null=True)
    ipadd = models.CharField(max_length=45, blank=True, null=True)
    hostname = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session'


class Statut(models.Model):
    idstatut = models.AutoField(primary_key=True)
    matricule = models.ForeignKey(Employe, models.DO_NOTHING, db_column='matricule')
    statut = models.CharField(max_length=45)
    num_conge = models.CharField(max_length=45, blank=True, null=True)
    num_autorisation = models.CharField(max_length=45, blank=True, null=True)
    remarque = models.CharField(max_length=45, blank=True, null=True)
    idpointage = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'statut'


class User(models.Model):
    nom = models.CharField(max_length=75, blank=True, null=True)
    prenom = models.CharField(max_length=75, blank=True, null=True)
    pseudo = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    role = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    is_staff = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    date_joined = models.DateField(blank=True, null=True)
    last_updated = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
