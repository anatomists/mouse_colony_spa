from rest_framework import viewsets
from .models import Mouse
from .serializers import MouseSerializer

class MouseViewSet(viewsets.ModelViewSet):
    queryset = Mouse.objects.all()
    serializer_class = MouseSerializer
