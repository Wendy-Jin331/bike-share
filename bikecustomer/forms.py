from django import forms
from django.db.models.query import QuerySet
from .models import Customer,Depots, Bikeasset, Hiresession
from django.utils.safestring import mark_safe
from django.forms import ModelForm

class start_depotf(forms.Form):
    start_depot = forms.ModelChoiceField(queryset=Depots.objects.all(),label=mark_safe('<h2>Origin Depot</h2>'))
class end_depotf(forms.Form):
    end_depot = forms.ModelChoiceField(queryset=Depots.objects.all(),label=mark_safe('<h2>Destination Depot</h2>'))

class RegistrationForm(ModelForm):
    firstname = forms.CharField(max_length=100, label=mark_safe('<br />First Name'))
    lastname = forms.CharField(max_length=100, label=mark_safe('<br />Last Name'))
    username = forms.CharField(max_length=100, label=mark_safe('<br />Username'))
    password = forms.CharField(widget=forms.PasswordInput(), label=mark_safe('<br />Password'))
    email = forms.CharField(widget=forms.EmailInput(), label=mark_safe('<br />Email'))

    class Meta:
        model = Customer
        fields = ["username", "password", "email"]