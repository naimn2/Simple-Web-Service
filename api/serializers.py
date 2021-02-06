from rest_framework import serializers
from .models import Habitat, Animal

class HabitatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitat
        fields = ('name','desc')

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'