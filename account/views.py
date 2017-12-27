# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import UserCreationForm
from django.views.generic import ListView , TemplateView,DetailView
from .mixins import LoggedInMixin
from django.contrib.auth.models import User
from field.models import Sepet

class UserRegister(FormView):
    template_name ="registration/register.html"
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        user = User.objects.create_user(form.cleaned_data['username'],
                                        form.cleaned_data['email'],
                                        form.cleaned_data['password1'])
        user.save()
        return super(UserRegister, self).form_valid(form)


class ProfileView(LoggedInMixin,TemplateView):

    template_name = "profile.html"

class SepetView(LoggedInMixin,ListView):
    template_name = "sepetim.html"

    queryset = Sepet.objects.all()



def sepetHeader(request):


    user = request.user;
    if user.is_authenticated:
        list = Sepet.objects.filter(user=user)


        return { "sepetNumber":list.count}
    return {}