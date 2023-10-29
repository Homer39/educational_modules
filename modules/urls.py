from django.urls import path

from modules.apps import ModulesConfig
from modules.views import ModuleCreateAPIView, ModuleListAPIView

app_name = ModulesConfig.name

urlpatterns = [
    path('module/create/', ModuleCreateAPIView.as_view(), name='module-create'),
    path('modules/', ModuleListAPIView.as_view(), name='module-list'),


]
