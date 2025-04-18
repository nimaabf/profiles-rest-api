from django.shortcuts import render
from rest_framework.views import APIView  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework import status  # type: ignore
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated


from profiles_api import serializers
from profiles_api import permissions
from profiles_api import models
# Create your views here.


class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiview = ['Use Http method as function']
        return Response({"message": 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        # put functionality
        return Response({'method': "PUT"})

    def patch(self, request, pk=None):
        # patch functionality
        return Response({'method': "PATCH"})

    def delete(self, request, pk=None):
        # delete functionality
        return Response({'method': "DELETE"})


class HelloViewSets(viewsets.ViewSet):

    def list(self, request):
        return Response({"message": "This is List Function"})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        # retrieve functionality
        return Response({'method': "retrieve"})

    def update(self, request, pk=None):
        # retrieve functionality
        return Response({'method': "update"})

    def partial_update(self, request, pk=None):
        # retrieve functionality
        return Response({'method': "partial_update"})

    def destroy(self, request, pk=None):
        # retrieve functionality
        return Response({'method': "destroy"})


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    # Handle Creating Updating and reading profiles feed
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnStatus,
                          IsAuthenticated)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()

    def perform_create(self, serializer):
        # Sets the user profile to loggedin
        serializer.save(user_profile=self.request.user)
