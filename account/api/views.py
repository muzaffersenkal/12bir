from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import SepetModelSerializer
from field.models import Sepet
from field.models import Field



class SepetAPIView(generics.ListAPIView):

    serializer_class = SepetModelSerializer

    def get_queryset(self, *args, **kwargs):

        return Sepet.objects.all()

class SepetCreateAPIView(generics.CreateAPIView):
    serializer_class = SepetModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user,field=Field.objects.first())

