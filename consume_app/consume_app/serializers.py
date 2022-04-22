from rest_framework import serializers
from .models import Candidato

class CandidatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidato
        fields = ['id','imgPol','imgPart', 'imgUF', 'siglaPart', 'nomeCand','email', 'twitter']
