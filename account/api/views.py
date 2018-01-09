from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import SepetModelSerializer
from field.models import Sepet
from field.models import Field

from django.http import Http404

class SepetAPIView(generics.ListAPIView):

    serializer_class = SepetModelSerializer

    def get_queryset(self, *args, **kwargs):

        return Sepet.objects.all()

class SepetCreateAPIView(generics.CreateAPIView):
    serializer_class = SepetModelSerializer
    permission_classes = [permissions.IsAuthenticated]



    def perform_create(self, serializer):
        print("ssss")

        _ = serializer.save(user=self.request.user,field=Field.objects.get(slug=self.request.data.get("fieldSlug")))
        return Response(_)

    
    def dispatch(self, request, *args, **kwargs):
        return super(SepetCreateAPIView, self).dispatch(request, *args, **kwargs)

