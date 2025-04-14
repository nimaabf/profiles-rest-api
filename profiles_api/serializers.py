from rest_framework import serializers
from django.conf import settings
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    # serialize ProfileFeed Items
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text',
                  'created_on')  # type: ignore
        extra_kwargs = {'user_profile':
                        {
                            'read_only': True
                        }
                        }
