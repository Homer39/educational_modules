from django.shortcuts import render
from rest_framework import generics

from modules.serializers import ModuleSerializer


class ModuleCreateAPIView(generics.CreateAPIView):
    "Контролер для создания модуля"
    serializer_class = ModuleSerializer


class ModuleListAPIView(generics.ListAPIView):
    "Контролер для просмотра списка модулей"
    serializer_class = ModuleSerializer
