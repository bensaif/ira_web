from django.contrib import admin
from .models import Stage, Benefice, Bourse, Etudiant, Chercheur, Destination

# Register your models here.

@admin.register(Etudiant)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Chercheur)
class ResearcherAdmin(admin.ModelAdmin):
    pass

@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    pass

@admin.register(Bourse)
class BourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Benefice)
class BeneficeAdmin(admin.ModelAdmin):
    pass

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    pass