from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import studentView

# from core import admin

urlpatterns = (
    path('api/', studentView),
)
