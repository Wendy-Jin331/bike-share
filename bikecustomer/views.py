from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Depots,Hiresession
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django import forms


# Create your views here.
def login(request):
    return render(request, 'login.html', {})

def logot(request):
    return render(request, 'logout.html', {})

def home(request):
    return render(request,'home.html', {})

def hirebike(request):
    return render(request,'hirebike.html', {})

def base(request):
    return render(request,'base.html', {})

def hiresession(request):
    return render(request,'hiresession.html', {})

def depots(request):
    results=Depots.objects.all()
    return render(request,'hirebike.html', {"depots": results})
#class depots(ListView):
    model = Depots
    context_object_name = 'starting depots'

#class depots(forms.Form):
    Hiresession.start_depot= forms.CharField(label='Starting point?', widget=forms.Select(choices=Depots))
