# -*- coding: utf-8 -*-
from django import forms

from .models import Field,Review

import itertools
from django.template.defaultfilters import slugify


class AddForm(forms.ModelForm):

    # # For images (requires Pillow for validation):
    # attachmentss = MultiMediaField(
    #     min_num=1,
    #     max_num=3,
    #     max_file_size=1024 * 1024 * 5,
    #     media_type='video'  # 'audio', 'video' or 'image'
    # )


    class Meta:
        model = Field
        fields = (
            'name',
            'desc',
            'price',
            'picture',
            # 'attachmentss',
            'city',
        )

class ReviewModelForm(forms.ModelForm):
    RATING_CHOICES = [
        ('0', '0- Çok Kötü'),
        ('1', '1- İdare Eder'),
        ('2', '2- Normal'),
        ('3', '3 - İyi'),
        ('4', '4 - Çok İyi'),
        ('5', '5 - Mükemmel'),
    ]
    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Konu Başlığı Giriniz', 'class': 'input-text full-width'}))

    review = forms.CharField(label='Başlık',widget=forms.Textarea(attrs={'placeholder': 'Yorumunuz','class':'input-text full-width'}))
    rating = forms.CharField(label='Puanlama ', widget=forms.Select(attrs={"class":"selector"},choices=RATING_CHOICES))

    class Meta:
        model= Review
        fields = [
            # "user",
            "title",
            "review",

        ]











