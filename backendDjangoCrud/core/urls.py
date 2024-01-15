from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import StudentViewSet

"""fourni, les deux lignes suivantes sont utilisées pour configurer les routes (URLs) dans le cadre d'un projet Django utilisant le framework Django REST Framework (DRF) :"""
router = DefaultRouter()
router.register('student', StudentViewSet, basename='student')

urlpatterns = (
    path('api/', include(router.urls)),
)
