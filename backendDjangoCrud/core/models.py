from django.db import models

# Create your models here.

# Définition de la classe Student,
# qui hérite de la classe Model de Django
class Student(models.Model):
    nom = models.CharField(max_length=100)
    cours = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)


"""
La classe Model de Django est une classe de base abstraite fournie par le module django.db.models. Elle sert de base pour la création de modèles de données dans le cadre du développement d'applications utilisant le framework Django.

L'utilisation de la classe Model permet aux développeurs de définir la structure de leurs données de manière orientée objet, et Django se charge ensuite de créer et de maintenir la base de données en fonction de ces modèles.

Lorsqu'une classe hérite de Model, elle peut définir différents champs de données, tels que des champs de caractères, des champs entiers, des champs de date, etc. Ces champs définissent la structure des données qui seront stockées dans la base de données.
"""