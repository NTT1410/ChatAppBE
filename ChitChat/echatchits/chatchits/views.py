from django.shortcuts import render
from rest_framework import viewsets, generics

from .models import Message
from .serializer import MessageSerializer


# Create your views here.

class MessageViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
