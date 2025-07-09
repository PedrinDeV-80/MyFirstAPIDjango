from rest_framework import serializers

from .models import Pessoa, Cotacao


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'
class CotacaoSerializers (serializers.ModelSerializer):
    class Meta: 
        model = Cotacao
        fields = '__all__'
        