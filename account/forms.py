from django import forms
from django.contrib import auth

class LoginForm(auth.forms.AuthenticationForm):
    username = forms.CharField(label=_("Username"), max_length=30,
                               widget=forms.TextInput(attrs={'class': 'loginput'}))