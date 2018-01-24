# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from django.views.generic.edit import FormView
from .forms import UserCreationForm
from django.views.generic import ListView , TemplateView,DetailView,DeleteView,CreateView
from .mixins import LoggedInMixin
from django.contrib.auth.models import User
from field.models import Sepet,Address
from django.core.urlresolvers import reverse_lazy
from .forms import AddressForm

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

class SepetView(LoggedInMixin,ListView,FormView):
    template_name = "sepetim.html"

    form_class = AddressForm
    context_object_name ="sepet_list"
    success_url = reverse_lazy('sepetim')

    def form_valid(self, form):
        print(form)
        address = form.save(commit=False)
        address.user = self.request.user
        address.save()
        return super(SepetView, self).form_valid(form)


    def get_queryset(self):
        return Sepet.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(SepetView, self).get_context_data(*args, **kwargs)
        # Add in a QuerySet of all the books
        address = Address.objects.filter(user=self.request.user)

        totalPrice = 0;
        sepet_list = self.get_queryset()
        for sepet in sepet_list:
            totalPrice += sepet.field.price




        context['totalPrice'] = totalPrice
        context['address_list'] = address

        return context


class SepetDeleteView(DeleteView):
    model = Sepet
    success_url = reverse_lazy('sepetim')

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(SepetDeleteView, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

class AddressAddView(CreateView):
    model = Address




def sepetHeader(request):


    user = request.user;
    if user.is_authenticated:
        list = Sepet.objects.filter(user=user)


        return { "sepetNumber":list.count}
    return {}