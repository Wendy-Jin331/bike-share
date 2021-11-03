from django import forms
from .models import *
from django.utils.safestring import mark_safe

class loginmgr(forms.Form):
    username = forms.CharField(label=mark_safe('Username: '),widget=forms.TextInput(),required=False)
    password = forms.CharField(label=mark_safe('<br>Password: '),widget=forms.PasswordInput(),required=False)