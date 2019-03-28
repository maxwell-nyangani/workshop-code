from rest_framework import serializers
from nonTrivialApp.models import Store
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
        )

class StoreSerializer(serializers.ModelSerializer):

    #user = UserSerializer(read_only=True)

    class Meta:
        model = Store
        fields = (
            'id',
            'user',
            'name',
            'logo',
            'banner',
            'is_active',
            'date_created',
            'rating',
        )