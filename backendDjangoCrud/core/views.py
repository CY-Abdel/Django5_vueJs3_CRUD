# from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
# def studentView(request):
#     return HttpResponse("hi juba")

from .models import Student
from .serializers import StudentSerializer

"""
from rest_framework import viewsets: Importe la classe viewsets du module rest_framework. Les viewsets de Django REST Framework sont des classes qui gèrent les opérations CRUD (Create, Retrieve, Update, Delete) pour un modèle particulier.
"""
from rest_framework import viewsets

"""
Définit une classe StudentViewSet qui hérite de viewsets.ModelViewSet. Cela signifie que cette classe est un viewset qui prend en charge les opérations CRUD pour le modèle Student.
"""
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all() #getAllStudents

    # Définit l'attribut serializer_class du viewset. Il spécifie la classe de sérialiseur à utiliser pour convertir les objets Student en représentations JSON et vice versa
    serializer_class = StudentSerializer