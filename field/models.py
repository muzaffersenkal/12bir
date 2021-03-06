# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django import forms
from django.conf import settings


# Create your models here.


class Field(models.Model):

    CITIES = (
        ('01','Izmir'),
        ('02','Mugla'),

    )

    name = models.CharField(max_length=30)
    desc = models.TextField(max_length=250)
    price = models.IntegerField()
    slug = models.SlugField(unique=True)
    city = models.CharField(max_length=25,choices=CITIES)
    address = models.CharField(max_length=25)





    picture = models.ImageField(upload_to='uploads/post_pics', blank=True)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug':self.slug})


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Field, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.CharField(max_length=30)
    review = models.TextField()
    rating = models.IntegerField(null=True, blank=True)
    post = models.ForeignKey('field',on_delete=models.CASCADE,related_name="review")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    def __str__(self):
        return self.title

class Sepet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    field = models.ForeignKey('Field',on_delete=models.CASCADE,related_name="field")
    selected = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.field.name+" => "+self.user.username


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    field = models.ForeignKey('Field',on_delete=models.CASCADE,related_name="fieldorder")
    address = models.ForeignKey('Address',on_delete=models.CASCADE,related_name="addressOrder")
    selected = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    desc = models.CharField(max_length=40,blank=True)

    def __str__(self):
        return self.field.name+" => "+self.user.username

class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=40)
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    city = models.CharField(max_length=40)
    ilce = models.CharField(max_length=40)
    address = models.TextField()
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.title







