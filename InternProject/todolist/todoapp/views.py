from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodolistSerializer
from .models import Todolist

# Create your views here.

class TodolistView(viewsets.ModelViewSet):
    serializer_class = TodolistSerializer
    queryset = Todolist.objects.all()