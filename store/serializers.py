from rest_framework import serializers
from .models import Urstore


class UrstoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urstore
        fields = '__all__'
