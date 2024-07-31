from rest_framework import serializers
from .models import Mouse, Cage, BreedingPair, Litter

class MouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mouse
        fields = '__all__'

class CageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cage
        fields = '__all__'

class BreedingPairSerializer(serializers.ModelSerializer):
    class Meta:
        model = BreedingPair
        fields = '__all__'

class LitterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Litter
        fields = '__all__'