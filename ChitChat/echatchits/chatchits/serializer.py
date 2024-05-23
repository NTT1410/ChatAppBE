from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User, Message, Group


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
