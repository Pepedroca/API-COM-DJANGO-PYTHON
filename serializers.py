from rest_framework import serializers
from .models import Jogos


class JogosSerialiazers(serializers.ModelSerializer):
    class Meta():
        model = Jogos
        fields = '__all__'