from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Interest


class InterestsSerializer(serializers.ModelSerializer):
    user = StringRelatedField()
    class Meta:
        model = Interest
        fields = ['id', 'interests', 'user']