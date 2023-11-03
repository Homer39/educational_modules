from django.shortcuts import render
from rest_framework import generics

from modules.models import Module
from modules.serializers import ModuleSerializer


class ModuleCreateAPIView(generics.CreateAPIView):
    "Контролер для создания модуля"
    serializer_class = ModuleSerializer

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()


class ModuleListAPIView(generics.ListAPIView):
    "Контролер для просмотра списка модулей"
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()


class ModuleRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер для просмотра одного модуля"""
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()


class ModuleUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ModuleSerializer

    def get_queryset(self):
        return Module.objects.filter(owner=self.request.user)


class ModuleDestroyAPIView(generics.DestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
