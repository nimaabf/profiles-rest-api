from django.shortcuts import render
from rest_framework.views import APIView  # type: ignore
from rest_framework.response import Response  # type: ignore
# Create your views here.


class HelloApiView(APIView):

    def get(self, request, format=None):
        an_apiview = ['Use Http method as function']
        return Response({"message": 'Hello', 'an_apiview': an_apiview})
