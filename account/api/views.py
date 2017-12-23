from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import SepetModelSerializer
from field.models import Sepet



class SepetAPIView(generics.ListAPIView):

    serializer_class = SepetModelSerializer

    def get_queryset(self, *args, **kwargs):

        return Sepet.objects.all()

