from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect
from bikeoperator.forms import *
#from bikecustomer.forms import *
from bikecustomer.models import *
from django import forms
import random as rd
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib import messages
from django.views.decorators.cache import cache_control

# Create your views here.

def homeop(request):
    if request.method == 'POST' and 'track' in request.POST:
        return redirect('http://127.0.0.1:8000/bikeoperator/track/')
    elif request.method == 'POST' and 'repair' in request.POST:
        return redirect('http://127.0.0.1:8000/bikeoperator/repair/')
    elif request.method == 'POST' and 'move' in request.POST:
        return redirect('http://127.0.0.1:8000/bikeoperator/move/')
    elif request.method == 'POST' and 'back' in request.POST:
            return redirect('http://127.0.0.1:8000/bikecustomer/')
    return render(request,'homeop.html',{})

def track(request):
    bikes= Bikeasset.objects.all()
    form = track_bike(request.POST)
    cur_depot = Bikeasset()
    status = Bikeasset()
    repair = Bikeasset()
    bikes_id= Bikeasset()
    flag = False
    check = False
    error = ''
    f = False
    messages = " Select a value"
    try:
        if request.method == 'POST' and 'check' in request.POST :
            form = track_bike(request.POST)
            error = ''
            check = True
            if form.is_valid():
                flag = True
                try:
                    bikes_id: Bikeasset = form.cleaned_data.get("bike_id")
                    cur_depot = bikes_id.current_depot
                    status = bikes_id.status
                    repair = bikes_id.need_repair
                except AttributeError:
                    f=True
            elif flag == False :
                error = 'Choose bike id'
        if request.method == 'POST' and 'move' in request.POST :
                return redirect('http://127.0.0.1:8000/bikeoperator/move/')
        if request.method == 'POST' and 'repair' in request.POST :
                return redirect('http://127.0.0.1:8000/bikeoperator/repair/')
        if 'home' in request.POST:
            return redirect('http://127.0.0.1:8000/bikeoperator/homeop/')
    except AssertionError:
        f= True
    context = {
        'flag': flag,
        'cur_depot': cur_depot,
        'bikes': bikes,
        'status': status,
        'repair': repair,
        'form' : form,
        'error': error,
        'bikes_id' : bikes_id,
        'check' : check,
        'messages': messages,
        'f': f
    }
    return render(request,'track.html',context = context)


def repair(request):
    form = repair_bike(request.POST)
    flag= False
    error = ''
    f= False
    messages="Select a value"
    bikes_id = Bikeasset()
    repair = False
    try:
        if request.method == 'POST':
            form = repair_bike(request.POST)
            error=''
        try:
            if form.is_valid():
                flag = True
                bikes_id: Bikeasset = form.cleaned_data.get("bike_id_repair")

            if request.method == 'POST' and 'repair' in request.POST:
                repair=True
                Bikeasset.objects.filter(bike_id = bikes_id.bike_id).update(need_repair=False)
            if 'home' in request.POST:
                return redirect('http://127.0.0.1:8000/bikeoperator/homeop/')
        except AttributeError:
            f=True
    except AttributeError:
        f= True
    context = {
        'form': form,
        'flag': flag,
        'bikes_id': bikes_id,
        'error': error,
        'repair': repair,
        'f': f,
        'messages': messages
    }
    return render(request,'repair.html',context = context)


def move(request):
    bikes_id = Bikeasset()
    form = track_bike(request.POST)
    form1 = start_depoto(request.POST)
    move = False
    error = ''
    move_depot = Depots()
    cur_depot = Bikeasset( )
    flag = False
    messages = ''
    f=False
    bikes_id = None
    b = True
    if request.method == 'POST' :
        if bikes_id == None :
            b= False
        form = move_bike(request.POST)
        form1 = start_depoto(request.POST)
        if form.is_valid() and form1.is_valid():
            try:
                flag = True
                bikes_id: Bikeasset = form.cleaned_data.get("bike_id_move")
                cur_depot = bikes_id.current_depot
                move_depot: Depots = form1.cleaned_data.get("start_depot")
                if bikes_id :
                    b= True
            except AttributeError:
                f= True
                messages = " select values in fields "
    try:
        if 'move' in request.POST:
            move = True
            #bikes_id: Bikeasset = form.cleaned_data.get("bike_id_move")
            #cur_depot = bikes_id.current_depot
            #move_depot: Depots = form1.cleaned_data.get("start_depot")
            Bikeasset.objects.filter(bike_id = bikes_id.bike_id).update(current_depot = move_depot.depot_id)
        if 'home' in request.POST:
            return redirect('http://127.0.0.1:8000/bikeoperator/homeop/')
    except AttributeError:
        f= True
        messages = " select values in fields "
    
    context = {
        'form' : form,
        'move' : move,
        'cur_depot' : cur_depot,
        'form1' : form1,
        'move_depot' : move_depot,
        'bikes_id' : bikes_id,
        'error' : error,
        'flag' : flag,
        'f':f,
        'b': b,
        'messages': messages
    }
    return render(request,'move.html',context = context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def loginop(request):
    form = logino(request.POST)
    error = ''
    message=''
    flag = False
    flag1= False
    if request.method == 'POST' and 'login' in request.POST:
        form = logino(request.POST)
        if form.is_valid():
            flag = True
            name = form.cleaned_data.get("username")
            pwd  = form.cleaned_data.get("password")
            try:
                if name == Operator.objects.get(name=name).name and pwd == Operator.objects.get(password=pwd).password:
                    return redirect('http://127.0.0.1:8000/bikeoperator/homeop/')
            except:
                flag1 = True
                message = " Invalid credentials"

    if request.method == 'POST' and 'login' in request.POST:
        if flag==False:
            error = 'Fill the fields'
    
    context = {
        'form': form,
        'error': error,
        'message': message,
        'flag1': flag1
    }
    return render(request,'loginop.html',context = context)