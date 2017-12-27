from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.urls import reverse_lazy
from  field.models import Sepet
from django.contrib.auth.models import User
from field.api.serializers import FieldModelSerializer

class UserDisplaySerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = [
            "username",
            "email"

        ]



class SepetModelSerializer(serializers.ModelSerializer):

    user = UserDisplaySerializer(read_only=True)
    field = FieldModelSerializer(read_only=True)

    class Meta:
        model = Sepet
        fields = [
            "user",
            "field",
             "selected",
            # "created",
            # "pay",



        ]

    # def get_follower_count(self,obj):
    #     return 0
    # def get_url(self,obj):
    #     return reverse_lazy("detail", kwargs={"slug":obj.slug})








