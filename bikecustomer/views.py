from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect
from bikecustomer.forms import *
from .models import *
from django import forms
from bikecustomer.forms import *
import random as rd
from datetime import datetime, timedelta
from django.utils import timezone

# Create your views here.
def register(request):
    form = RegistrationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            firstname = form.cleaned_data.get("firstname")
            lastname = form.cleaned_data.get("lastname")
            username = form.cleaned_data.get("username")
            dob = form.cleaned_data.get("dob")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            #phone = form.cleaned_data.get("phone")
            user = User.objects.create_user(username,email,password, is_active = True)
            customer = Customer(customer_name = username, password = password,customer_dob= dob,customer_email =email)#,customer_phone = phone)
            customer.save()
            user.first_name = firstname
            user.last_name = lastname
            my_group = Group.objects.get(name='Customers') 
            my_group.user_set.add(user)
            user.save()  
            
        return redirect('/')
    context = {
        'form' : form
    }
    return render(request, 'register.html', context=context)

def login(request):
    #if request.method == 'POST':
        #customer = Customer.objects.filter()
       # username = customer.objects.filter()
    return render(request, 'login.html', {})

@login_required
def logout(request):
    return render(request, 'logout.html', {})

@login_required
def home(request):
    return render(request,'home.html', {})

@login_required
def hirebike(request):
    depots= Depots.objects.all()
    current_user = request.user
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
            end_depot = form2.cleaned_data.get("end_depot")
            selected_depot = depots.filter(depot_name=start_depot)[0]
            
            available_bikes = bikes.filter(current_depot=selected_depot)
            selected_bike = available_bikes[0]  
            Bikeasset.objects.filter(pk=selected_bike.bike_id).update(status= True) 
            hiresession = Hiresession(session_id = rd.randint(1,2000), customer_id = current_user.id,start_depot = start_depot.depot_name,end_depot= end_depot.depot_name,bike_id= selected_bike)
            hiresession.save()
            request.session["session_id"] = hiresession.session_id
            return redirect('http://127.0.0.1:8000/bikecustomer/hiresession/')
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
    current_user = request.user
    session_id = request.session["session_id"]
    flag= False
    now = datetime.now(timezone.utc)
    hired_time = now
    hiresession = Hiresession.objects.filter(session_id = session_id)[0]
    price =0.0
    if request.method == 'POST' and 'endride' in request.POST:
        #Hiresession.objects.filter(session_id = session_id).update(end_date_time = timezone.now) 
        hiresession.end_date_time = timezone.now
        hired_time =  now - hiresession.start_date_time
        flag = True
        depot = Depots.objects.filter(depot_name=hiresession.end_depot)[0]
        Bikeasset.objects.filter(bike_id = hiresession.bike_id.bike_id).update(status= False,current_depot =depot)
        minutes = hired_time.total_seconds() / 60
        price = minutes * (5/60)
        price = round(price)
    if request.method == 'POST' and 'pay' in request.POST:
         return redirect('http://127.0.0.1:8000/bikecustomer/payment/')
    context = {
        'hiresession' : hiresession,
        'hired_time' : hired_time,
        'flag' : flag ,
        'price' : price      
     }
    return render(request,'hiresession.html', context=context)


