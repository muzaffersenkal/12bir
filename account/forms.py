# -*- coding: utf-8 -*-
from django import forms
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit,Div
from field.models import Address,Order



class UserCreationForm(forms.Form):
    username = forms.RegexField(regex=r'^[\w.@+-]+$',max_length=30,label='Username')
    email = forms.EmailField(label="E-mail")
    password1 = forms.CharField(widget=forms.PasswordInput,label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput,label="Repeat Password")

    class Meta:
        models = User
        fields = ('username','email','password1','password2')


class AddressForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        # NEW:
        self.helper.label_class = ''
        self.helper.field_class = ''
        self.helper.textarea_class = ''


        self.helper.layout = Layout(
            Div(
                Div(Field('title', css_class='input-text full-width'), css_class='col-sm-6 col-md-5'),css_class="form-group row"),

            Div(
            Div(Field('firstName', rows="3", css_class='input-text full-width'),css_class='col-sm-6 col-md-5'),
            Div(Field('lastName', rows="3", css_class='input-text full-width'),css_class='col-sm-6 col-md-5'),css_class="form-group row"),

            Div(
                Div(Field('email', rows="3", css_class='input-text full-width'), css_class='col-sm-6 col-md-5'),
                Div(Field('phone_number', rows="3", css_class='input-text full-width'), css_class='col-sm-6 col-md-5'),
                css_class="form-group row"),

            Div(
                Div(Field('city', rows="3", css_class='input-text full-width'), css_class='col-sm-6 col-md-5'),
                Div(Field('ilce', rows="3", css_class='input-text full-width'), css_class='col-sm-6 col-md-5'),
                css_class="form-group row"),

            Div(
                Div(Field('address', rows="4", placeholder='Adresi giriniz'), css_class='col-sm-12 col-md-12'),
               css_class="form-group row"),



            # NEW:
            # ButtonHolder(
            #     Submit('submit', 'Submit', css_class='input-text full-width')
            # )
        )
        self.fields['title'].label = "Adres Başlığı"
        self.fields['firstName'].label = "İsim"
        self.fields['lastName'].label = "Soyisim"
        self.fields['email'].label = "Email Adresi"
        self.fields['phone_number'].label = "Telefon Numarası"
        self.fields['city'].label = "Şehir"
        self.fields['ilce'].label = "İlçe"
        self.fields['address'].label = "Adres"

    class Meta:
        model = Address
        fields = ['title', 'firstName','lastName','email','phone_number','city','ilce','address']

class OrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        # NEW:
        self.helper.label_class = ''
        self.helper.field_class = ''
        self.helper.textarea_class = ''


        self.helper.layout = Layout(
            Div(
                Div(Field('cartnum', css_class='input-text full-width'), css_class='col-sm-6 col-md-5'),
                Div(Field('name', rows="3", css_class='input-text full-width'), css_class='col-sm-6 col-md-5'),
                css_class="form-group row"),



            Div(
                Div(Field('sonKullanma', rows="3", css_class='input-text full-width'), css_class='col-sm-6 col-md-5'),
                Div(Field('cvv', rows="3", css_class='input-text full-width'), css_class='col-sm-6 col-md-5'),
                css_class="form-group row"),







            # NEW:
            # ButtonHolder(
            #     Submit('submit', 'Submit', css_class='input-text full-width')
            # )
        )
        self.fields['cartnum'].label = "Kart Numarası"
        self.fields['name'].label = "İsim Soyisim"

        self.fields['sonKullanma'].label = "Son Kullanma Tarihi"

        self.fields['cvv'].label = "Güvenlik numarası"

    cartnum = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Konu Başlığı Giriniz', 'class': 'input-text full-width'}))

    name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Konu Başlığı Giriniz', 'class': 'input-text full-width'}))

    sonKullanma = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Konu Başlığı Giriniz', 'class': 'input-text full-width'}))

    cvv = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Konu Başlığı Giriniz', 'class': 'input-text full-width'}))

    class Meta:
        model = Order
        fields = [
            # "user",
            "cartnum",
            "name",
            "sonKullanma",
            "cvv"


        ]




