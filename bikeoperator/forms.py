from django import forms
from django.db.models.query import QuerySet
from .models import *
from bikecustomer.models import Bikeasset, Depots
from django.utils.safestring import mark_safe
from django.forms import ModelForm

class track_bike(forms.Form):
    bike_id = forms.ModelChoiceField(queryset=Bikeasset.objects.all(), label=mark_safe('<br><b>All Bikes   '),required=False)

class move_bike(forms.Form):
    bike_id_move = forms.ModelChoiceField(queryset=Bikeasset.objects.filter(need_repair=False,status=False),required=False, label=mark_safe('<br><b>Bikes '))

class start_depoto(forms.Form):
    start_depot = forms.ModelChoiceField(queryset=Depots.objects.all(), label=mark_safe('<br><b>Depots '),required=False)

class repair_bike(forms.Form):
    bike_id_repair = forms.ModelChoiceField(queryset=Bikeasset.objects.filter(need_repair=True),required=False, label=mark_safe('<br><b>Bikes that needs repair '))

class logino(forms.Form):
    username = forms.CharField(label=mark_safe('Username: '),widget=forms.TextInput(),required=False)
    password = forms.CharField(label=mark_safe('<br>Password: '),widget=forms.PasswordInput(),required=False)