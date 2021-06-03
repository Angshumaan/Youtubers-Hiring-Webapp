from django.urls import path
from .import context_processors

urlpatterns = [
    path('info', context_processors.info, name="info"),
]
