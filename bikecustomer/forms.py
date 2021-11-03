from django import forms
from django.db.models.query import QuerySet
from .models import *
from bikecustomer.models import Depots
from django.utils.safestring import mark_safe
from django.forms import ModelForm


class start_depotf(forms.Form):
    start_depot = forms.ModelChoiceField(queryset=Depots.objects.all(), label=mark_safe('<h2>Origin Depot</h2>'))


class end_depotf(forms.Form):
    end_depot = forms.ModelChoiceField(queryset=Depots.objects.all(), label=mark_safe('<h2>Destination Depot</h2>'))


YEARS = [x for x in range(1940, 2021)]


class RegistrationForm(ModelForm):
    firstname = forms.CharField(max_length=100, label=mark_safe('<br />First Name'),required=False)
    lastname = forms.CharField(max_length=100, label=mark_safe('<br />Last Name'),required=False)
    username = forms.CharField(max_length=100, label=mark_safe('<br />Username'),required=False)
    password = forms.CharField(widget=forms.PasswordInput(), label=mark_safe('<br />Password'),required=False)
    dob = forms.DateField(widget=forms.SelectDateWidget(years=YEARS), label=mark_safe('<br />Data of Birth'),required=False)
    email = forms.CharField(widget=forms.EmailInput(), label=mark_safe('<br />Email'),required=False)

    # phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$',label= mark_safe('<br />Phone number'),error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
    # validators should be a list

    class Meta:
        model = Customer
        fields = ["username", "password", "dob", "email"]


class PaymentForm(ModelForm):
    class Meta:
        model = payment
        fields = '__all__'
