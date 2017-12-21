from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.urls import reverse_lazy
from  field.models import Field

User  = get_user_model()

class FieldModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Field
        fields = [
            "name",
            "desc",
            "price",
            "city",
            "slug"

        ]

    # def get_follower_count(self,obj):
    #     return 0
    # def get_url(self,obj):
    #     return reverse_lazy("profiles:detail", kwargs={"username":obj.username})
