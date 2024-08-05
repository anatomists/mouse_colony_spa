from rest_framework import serializers
from .models import Mouse, Cage, BreedingPair, Litter, Role
from django.contrib.auth import get_user_model

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

User = get_user_model()

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'roles', 'is_verified')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
