from django import forms
from django.db.models.query import QuerySet
from .models import *
from bikecustomer.models import Bikeasset, Depots
from django.utils.safestring import mark_safe
from django.forms import ModelForm

class track_bike(forms.Form):
    bike_id = forms.ModelChoiceField(queryset=Bikeasset.objects.all(), label=mark_safe('<h2>All Bikes</h2>'))

class move_bike(forms.Form):
    bike_id_move = forms.ModelChoiceField(queryset=Bikeasset.objects.filter(need_repair=False,status=False), label=mark_safe('<h2>Bikes that can be moved</h2>'))

class start_depoto(forms.Form):
    start_depot = forms.ModelChoiceField(queryset=Depots.objects.all(), label=mark_safe('<h2>Depots</h2>'))

class repair_bike(forms.Form):
    bike_id_repair = forms.ModelChoiceField(queryset=Bikeasset.objects.filter(need_repair=True), label=mark_safe('<h2>Bikes that needs repair</h2>'))
