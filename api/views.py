from rest_framework import viewsets, status
from .models import Mouse, Cage, BreedingPair, Litter, Role
from .serializers import UserSerializer, MouseSerializer, CageSerializer, BreedingPairSerializer, LitterSerializer, RoleSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

User = get_user_model()

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

def index(request):
    return HttpResponse("Welcome to the Mouse Colony Manager API. Go to /admin or /api for more information.")

class MouseViewSet(viewsets.ModelViewSet):
    queryset = Mouse.objects.all()
    serializer_class = MouseSerializer

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

class CageViewSet(viewsets.ModelViewSet):
    queryset = Cage.objects.all()
    serializer_class = CageSerializer

class BreedingPairViewSet(viewsets.ModelViewSet):
    queryset = BreedingPair.objects.all()
    serializer_class = BreedingPairSerializer

class LitterViewSet(viewsets.ModelViewSet):
    queryset = Litter.objects.all()
    serializer_class = LitterSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def update_roles(self, request, pk=None):
        user = self.get_object()
        roles = request.data.get('roles')
        user.roles.set(roles)
        user.save()
        return Response({'status': 'roles set'})

class PasswordResetView(APIView):
    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            # Generate token and send email (implementation depends on your setup)
            send_mail(
                'Password Reset Request',
                'Here is the message.',
                'from@example.com',
                [email],
                fail_silently=False,
            )
            return Response({'message': 'Password reset email sent.'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmailVerificationView(APIView):
    def get(self, request, token):
        try:
            user = User.objects.get(verification_token=token)
            user.is_verified = True
            user.save()
            return Response({'message': 'Email successfully verified.'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'Invalid token.'}, status=status.HTTP_400_BAD_REQUEST)
