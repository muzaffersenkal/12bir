from django import forms

from .models import Field

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




