from rest_framework.serializers import ModelSerializer, StringRelatedField
from rest_framework import serializers
from .models import Question,Answer
from django.contrib.auth.models import User


class AnswerSerializer(serializers.ModelSerializer):
    '''create class to serializer model'''
    question = StringRelatedField()
    user = StringRelatedField()

    class Meta:
        model = Answer
        fields = ['id', 'question', 'answer', 'user']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_title']
