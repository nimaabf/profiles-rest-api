from rest_framework import serializers
from django.conf import settings


class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
