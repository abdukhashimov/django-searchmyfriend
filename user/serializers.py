from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'firstname', 'lastname', 'email', 'username', 'password']