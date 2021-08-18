from rest_framework import viewsets
from . import models
from . import serializers


class UrstoreViewset(viewsets.ModelViewSet):
    queryset = models.Urstore.objects.all()
    serializer_class = serializers.UrstoreSerializer
