
import calendar
import json
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.views import generic
from django.views.generic import View

from .models import *
from .utils import Calendar
from django.utils.safestring import mark_safe

from datetime import date, datetime, timedelta
#import datetime
from django.utils.translation import gettext_lazy as _
from .forms import *
from django.contrib import messages


# Create your views here.
"""def gh_acceuil(request):
    return render(request, 'guesthouse/accueil.html', {})"""

""" def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			user = authenticate(email=email, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {email}.")
				return redirect("guesthouse:accueil")
			else:
				messages.error(request,"Invalid email or password.")
		else:
			messages.error(request,"Invalid email or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="guesthouse/signin.html", context={"login_form":form}) """


class gh_acceuil(generic.View):
   # login_url = "guesthouse:signin"
    template_name = "guesthouse/accueil.html"

    def get(self, request, *args, **kwargs):
        
           
            #today = datetime.datetime.now()
            #current_month = datetime.now().month
            #start_of_month = datetime.date.today().replace(day=1)
            today = date.today()
            seven_day_after = today + timedelta(days=7)

            reservation = Reservation.objects.filter(datefin__gte=today, statutres = 'Annulée')
            hebergement = Hebergement.objects.filter(datesortie__gte=today, statuthebg='Annulé')
            
            running_reserve = Reservation.objects.filter(datefin=today).order_by("datedeb")
            running_hosting = Hebergement.objects.filter(datesortie=today).order_by("dateheberg")
            
            latest_reserve = Reservation.objects.filter(datefin__gte=seven_day_after, statutres = 'Réservation confirmée').order_by("datedeb")
            latest_hosting = HbgRecap.objects.filter(dates__gte=seven_day_after, statut='Confirmé').order_by("dateh")

            context = {
                "total_reserve": reservation.count(),
                "total_hosting": hebergement.count(),
                "running_reserve": running_reserve.count(),
                "running_hosting": running_hosting.count(),
                "latest_reserve": latest_reserve,
                "latest_hosting": latest_hosting,
            }
            return render(request, self.template_name, context)


class CalendarView(generic.ListView):
    model= Reservation
    template_name = "guesthouse/calendar.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

         # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

         # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split("-"))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


class CalendarViewNew(generic.View):
   # login_url = "guesthouse:signin"
    model = Reservation
    template_name = "guesthouse/reserve_calendar.html"

    def get(self, request, *args, **kwargs):
        
        today = date.today()
        seven_day_after = today + timedelta(days=7)

        all_events = Reservation.objects.filter(statutres = 'Réservation confirmée')#.values('idreservation','administration','datedeb','datefin')
        events_today = Reservation.objects.filter(datefin=today, statutres = 'Réservation confirmée').order_by("datedeb")
        events_month = Reservation.objects.filter(datefin__gte=seven_day_after, statutres = 'Réservation confirmée').order_by("datedeb")
        
        # if filters applied then get parameter and filter based on condition else return object
        if request.GET:  
            event_arr = []
            if request.GET.get('statutres') == "all":
                all_events = Reservation.objects.all()
            else:   
                all_events = Reservation.objects.filter(statutres = 'Réservation confirmée')

            for i in all_events:
                event_sub_arr = {}
                event_sub_arr['title'] = i.administration
                datedeb = datetime.datetime.strptime(str(i.datedeb.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
                datefin = datetime.datetime.strptime(str(i.datefin.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
                event_sub_arr['start'] = datedeb
                event_sub_arr['end'] = datefin
                event_arr.append(event_sub_arr)
            return HttpResponse(json.dumps(event_arr))

        context = {
            "events":all_events,
            "events_month": events_month, 
            "events_today": events_today
        }
        return render(request, self.template_name, context)
    
    """ def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            form = forms.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("guesthouse:reserve_calendar")
        context = {"form": forms}
        return render(request, self.template_name, context)  """


class reserve_details(View):
    template_name = "guesthouse/reserve_details.html"

    def get(self, request, *args, **kwargs):
        today = date.today()
        seven_day_after = today + timedelta(days=7)

        reservation = Reservation.objects.filter(datefin__gte=today, statutres = 'Annulée')
        
        running_reserve = Reservation.objects.filter(datefin=today).order_by("datedeb")
        
        latest_reserve = Reservation.objects.filter(datefin__gte=seven_day_after, statutres = 'Réservation confirmée').order_by("datedeb")

        occupied_meeting_room = Reservation.objects.extra(select={"Reservation.salle": "IN SELECT Salle.type FROM Salle"}).filter(statutres = 'Réservation confirmée', datefin=today)

        empty_meeting_room = Salle.objects.extra(
            select={"Salle.type": "NOT IN SELECT Reservation.salle FROM Resrvation WHERE statutres like 'Réservation confirmée' AND today BETWEEN datedeb AND datefin"}
        )

        context = {
            "total_reserve": reservation.count(),
            "running_reserve": running_reserve.count(),
            "total_empty_meeting_room": empty_meeting_room.count(),
            "total_occupied_meeting_room": occupied_meeting_room.count(),
            "latest_reserve": latest_reserve,
        }
        return render(request, self.template_name, context)


class CalendarViewHosting(generic.View):
    #login_url = "guesthouse:signin"
    model = HbgRecap
    template_name = "guesthouse/hosting_calendar.html"

    def get(self, request, *args, **kwargs):
        
        today = date.today()
        seven_day_after = today + timedelta(days=7)

        all_events = HbgRecap.objects.filter(statut='Confirmé')#.values('idreservation','administration','datedeb','datefin')
        events_today = HbgRecap.objects.filter(dates=today, statut='Confirmé').order_by("dateh")
        events_month = HbgRecap.objects.filter(dates__gte=seven_day_after, statut='Confirmé').order_by("dateh")
        
        # if filters applied then get parameter and filter based on condition else return object
        if request.GET:  
            event_arr = []
            if request.GET.get('statut') == "all":
                all_events = HbgRecap.objects.all()
            else:   
                all_events = HbgRecap.objects.filter(statut='Confirmé')

            for i in all_events:
                event_sub_arr = {}
                #event_sub_arr['id'] = i.idhebergement
                event_sub_arr['title'] = i.etablissement
               # event_sub_arr['cap'] = i.capacite
                dateh = datetime.datetime.strptime(str(i.dateh.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
                dates = datetime.datetime.strptime(str(i.dates.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
                event_sub_arr['start'] = dateh
                event_sub_arr['end'] = dates
                event_arr.append(event_sub_arr)
            return HttpResponse(json.dumps(event_arr))

        context = {
            "events":all_events,
            "events_month": events_month, 
            "events_today": events_today
        }
        return render(request, self.template_name, context)

class hosting_details(View):
    template_name = "guesthouse/hosting_details.html"

    def get(self, request, *args, **kwargs):
        #today = datetime.datetime.now()
        #current_month = datetime.now().month
        #start_of_month = datetime.date.today().replace(day=1)
        today = date.today()
        seven_day_after = today + timedelta(days=7)

        hebergement = Hebergement.objects.filter(datesortie__gte=today, statuthebg='Annulé')
        
        running_hosting = Hebergement.objects.filter(datesortie=today).order_by("dateheberg")
        
        latest_hosting = Hebergement.objects.filter(datesortie__gte=seven_day_after, statuthebg='Confirmé').order_by("dateheberg")

        occupied_room = Hebergement.objects.extra(select={"Hebergement.roomnum": "IN SELECT Chambre.numero FROM Chambre"}).filter(statuthebg='Confirmé', datesortie=today)

        empty_room = Chambre.objects.extra(
            select={"Chambre.numero": "NOT IN SELECT Hebergement.roomnum FROM Hebergement WHERE statuthebg like 'Confirmé' AND today BETWEEN dateheberg AND datesortie"}
        )

        context = {
            "total_hosting": hebergement.count(),
            "running_hosting": running_hosting.count(),
            "total_room_empty": empty_room.count(),
            "total_occupied_room": occupied_room.count(),
            "latest_hosting": latest_hosting,
        }
        return render(request, self.template_name, context)

