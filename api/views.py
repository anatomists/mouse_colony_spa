from rest_framework import viewsets
from .models import Mouse, Cage, BreedingPair, Litter
from .serializers import MouseSerializer, CageSerializer, BreedingPairSerializer, LitterSerializer

class MouseViewSet(viewsets.ModelViewSet):
    queryset = Mouse.objects.all()
    serializer_class = MouseSerializer

class CageViewSet(viewsets.ModelViewSet):
    queryset = Cage.objects.all()
    serializer_class = CageSerializer

class BreedingPairViewSet(viewsets.ModelViewSet):
    queryset = BreedingPair.objects.all()
    serializer_class = BreedingPairSerializer

class LitterViewSet(viewsets.ModelViewSet):
    queryset = Litter.objects.all()
    serializer_class = LitterSerializer