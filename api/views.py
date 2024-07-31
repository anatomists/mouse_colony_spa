from rest_framework import viewsets
from .models import Mouse, Cage, BreedingPair, Litter
from .serializers import MouseSerializer, CageSerializer, BreedingPairSerializer, LitterSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

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