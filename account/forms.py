from django import forms
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserCreationForm(forms.Form):
    username = forms.RegexField(regex=r'^[\w.@+-]+$',max_length=30,label='Username')
    email = forms.EmailField(label="E-mail")
    password1 = forms.CharField(widget=forms.PasswordInput,label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput,label="Repeat Password")

    class Meta:
        models = User
        fields = ('username','email','password1','password2')



