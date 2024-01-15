from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = '__all__'
        fields = ['id', 'nom', 'cours', 'email', 'genre']

"""
class StudentSerializer(serializers.ModelSerializer):: Définit une classe StudentSerializer qui hérite de serializers.ModelSerializer, indiquant que ce sérialiseur est destiné à être utilisé avec des modèles Django.

class Meta:: La classe interne Meta est utilisée pour fournir des métadonnées au sérialiseur. Ici, elle spécifie le modèle associé au sérialiseur et les champs à inclure dans la sérialisation.

model = Student: Indique que ce sérialiseur est associé au modèle Django Student.

fields = ['id', 'nom', 'cours', 'email', 'genre']: Définit les champs du modèle Student à inclure dans la sérialisation. Dans cet exemple, les champs id, nom, cours, email et genre sont inclus. Vous pouvez également utiliser fields = '__all__' pour inclure tous les champs du modèle.
"""
