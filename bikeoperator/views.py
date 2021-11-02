from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect
from bikeoperator.forms import *
from bikecustomer.forms import *
from bikecustomer.models import *
from django import forms
import random as rd
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib import messages

# Create your views here.


def homeop(request):
    if request.method == 'POST' and 'track' in request.POST:
        return redirect('http://127.0.0.1:8000/bikeoperator/track/')
    elif request.method == 'POST' and 'repair' in request.POST:
        return redirect('http://127.0.0.1:8000/bikeoperator/repair/')
    elif request.method == 'POST' and 'move' in request.POST:
        return redirect('http://127.0.0.1:8000/bikeoperator/move/')
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
    if request.method == 'POST' and 'check' in request.POST :
        form = track_bike(request.POST)
        error = ''
        check = True
        if form.is_valid():
            flag = True
            bikes_id: Bikeasset = form.cleaned_data.get("bike_id")
            cur_depot = bikes_id.current_depot
            status = bikes_id.status
            repair = bikes_id.need_repair
        elif flag == False :
            error = 'Choose bike id'
    if request.method == 'POST' and 'move' in request.POST :
        #flag = True
        if flag == False:
            error = 'Choose bike id'
        else:
            return redirect('http://127.0.0.1:8000/bikeoperator/move/')
    if request.method == 'POST' and 'repair' in request.POST :
        #flag = True
        if flag == False:
            error = 'Choose bike id'
        else:
            return redirect('http://127.0.0.1:8000/bikeoperator/repair/')
    context = {
        'flag': flag,
        'cur_depot': cur_depot,
        'bikes': bikes,
        'status': status,
        'repair': repair,
        'form' : form,
        'error': error,
        'bikes_id' : bikes_id,
        'check' : check
    }
    return render(request,'track.html',context = context)


def repair(request):
    form = repair_bike(request.POST)
    flag= False
    error = ''
    bikes_id = Bikeasset()
    repair = False
    if request.method == 'POST':
        form = repair_bike(request.POST)
        error=''
        if form.is_valid():
            flag = True
            bikes_id: Bikeasset = form.cleaned_data.get("bike_id_repair")

    if request.method == 'POST' and 'repair' in request.POST:
        if flag==False:
            error = 'Choose bike id'
        repair=True
        Bikeasset.objects.filter(bike_id = bikes_id.bike_id).update(need_repair=False)

    context = {
        'form': form,
        'flag': flag,
        'bikes_id': bikes_id,
        'error': error,
        'repair': repair
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
    if request.method == 'POST':
        form = move_bike(request.POST)
        form1 = start_depoto(request.POST)
        error = ''
        if form.is_valid() and form1.is_valid():
            flag = True
            bikes_id: Bikeasset = form.cleaned_data.get("bike_id_move")
            cur_depot = bikes_id.current_depot
            move_depot: Depots = form1.cleaned_data.get("start_depot")
    if request.method == 'POST' and 'move' in request.POST:
        if flag==False:
            error = 'Choose bike id'
        move = True
        Bikeasset.objects.filter(bike_id = bikes_id.bike_id).update(current_depot = move_depot.depot_id)
    context = {
        'form' : form,
        'move' : move,
        'cur_depot' : cur_depot,
        'form1' : form1,
        'move_depot' : move_depot,
        'bikes_id' : bikes_id,
        'error' : error,
        'flag' : flag
    }
    return render(request,'move.html',context = context)