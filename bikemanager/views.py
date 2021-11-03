from typing import ContextManager
from django.shortcuts import render
from bikemanager.forms import *
from bikemanager.models import *
from django.shortcuts import redirect
from bikecustomer.models import *
from bikeoperator.models import *
import matplotlib.pyplot as plt
from matplotlib import pylab
from pylab import *

from plotly.offline import plot
import plotly.graph_objects as go

# Create your views here.
def loginmg(request):
    form = loginmgr(request.POST)
    error = ''
    message=''
    flag = False
    flag1= False
    if request.method == 'POST' and 'login' in request.POST:
        form = loginmgr(request.POST)
        if form.is_valid():
            flag = True
            name = form.cleaned_data.get("username")
            pwd  = form.cleaned_data.get("password")
            try:
                if name == Manager.objects.get(name=name).name and pwd == Manager.objects.get(password=pwd).password:
                    return redirect('http://127.0.0.1:8000/bikemanager/homemgr/')
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
    return render(request, 'loginmgr.html', context=context)

def homemgr(request):
    flag = False
        
    graphics = []
    sessions = Hiresession.objects.all()
    depots = Depots.objects.all()

    date_start = timezone.now()
    date_end = timezone.now()

    depot_dict = dict((depot.depot_name, len([i for i in sessions.filter(start_depot = depot)])) for depot in depots)

    graphics.append(
        go.Bar(x=list(depot_dict.keys()), y=list(depot_dict.values()), name='Line y1')
    )

    layout1 = {
        'title': 'Frequency of rides from each depot',
        'xaxis_title': 'Depots',
        'yaxis_title': 'Frequency',
        'height': 420,
        'width': 560,
    }
    plot_div = plot({'data': graphics, 'layout': layout1}, output_type='div')

    context = {
        'flag': flag,
        'plot_div': plot_div,
        'depot_dict': depot_dict
     }
    return render(request, 'homemgr.html', context = context)

"""
1. Depot Frequency
- Number of bike rides starting at each depot (histogram)

"""