from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from field.models import Field
from .serializers import FieldModelSerializer
from ..models import Field
from django.db.models import Q


class FieldAPIView(generics.ListAPIView):
    serializer_class = FieldModelSerializer

    queryset = Field.objects.all()

