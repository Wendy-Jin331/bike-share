from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from .models import Bikeasset, Depots,Hiresession
from .models import *
from django import forms
from bikecustomer.forms import *

# Create your views here.
def login(request):
    return render(request, 'login.html', {})

def logout(request):
    return render(request, 'logout.html', {})

def home(request):
    return render(request,'home.html', {})

def hirebike(request):
    depots= Depots.objects.all()
    bikes = Bikeasset.objects.filter(need_repair = False, status = False)
    available_bikes = []
    selected_bike = Bikeasset()
    form1 = start_depotf(request.POST)
    form2 = end_depotf(request.POST)
    flag = False
    error =''
    if request.method == 'POST' and 'check' in request.POST:
        form1 = start_depotf(request.POST)
        form2 = end_depotf(request.POST)
        error =''
        if form1.is_valid() and form2.is_valid():
            start_depot = form1.cleaned_data.get("start_depot")
            flag = True
            selected_depot = depots.filter(depot_name=start_depot)[0]
            available_bikes = bikes.filter(current_depot=selected_depot)
            selected_bike = available_bikes[0]
           

    elif request.method == 'POST' and 'startride' in request.POST:
        if flag == False:
            error = 'Choose Origin and Destination'
        form1 = start_depotf(request.POST)
        form2 = end_depotf(request.POST)
        if form1.is_valid() and form2.is_valid():
            start_depot = form1.cleaned_data.get("start_depot")
            selected_depot = depots.filter(depot_name=start_depot)[0]
            available_bikes = bikes.filter(current_depot=selected_depot)
            selected_bike = available_bikes[0]  
            Bikeasset.objects.filter(pk=selected_bike.bike_id).update(status= True) 
            
    context = {
        'depots' : depots,
        'bikes' : bikes,
        'form1' : form1,
        'form2' : form2,
        'error' : error,
        'available_bikes' : available_bikes,
        'selected_bike' : selected_bike
    }
    return render(request,'hirebike.html', context=context)

def base(request):
    return render(request,'base.html', {})

def hiresession(request):
    return render(request,'hiresession.html', {})

#class depots(ListView):
    model = Depots
    context_object_name = 'starting depots'

#class depots(forms.Form):
    Hiresession.start_depot= forms.CharField(label='Starting point?', widget=forms.Select(choices=Depots))
