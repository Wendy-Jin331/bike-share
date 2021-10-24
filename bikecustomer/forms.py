from django import forms
from django.db.models.query import QuerySet
from .models import Customer,Depots, Bikeasset, Hiresession
from django.utils.safestring import mark_safe

class start_depotf(forms.Form):
    start_depot = forms.ModelChoiceField(queryset=Depots.objects.all(),label=mark_safe('<h2>Origin Depot</h2>'))
class end_depotf(forms.Form):
    end_depot = forms.ModelChoiceField(queryset=Depots.objects.all(),label=mark_safe('<h2>Destination Depot</h2>'))
