from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings
import uuid

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='custom_user',
    )
    verification_token = models.CharField(max_length=36, unique=True, default=uuid.uuid4)
    is_verified = models.BooleanField(default=False)

class Mouse(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    ear_tag = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    genotype = models.CharField(max_length=100)
    strain = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Mouse {self.ear_tag} ({self.gender})"

class Cage(models.Model):
    cage_number = models.CharField(max_length=20, unique=True)
    capacity = models.IntegerField(default=5)
    mice = models.ManyToManyField(Mouse, related_name='cages')

    def __str__(self):
        return f"Cage {self.cage_number}"

class BreedingPair(models.Model):
    name = models.CharField(max_length=100)
    male = models.ForeignKey(Mouse, related_name='male_breedings', on_delete=models.SET_NULL, null=True)
    female = models.ForeignKey(Mouse, related_name='female_breedings', on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Breeding Pair: {self.name}"

class Litter(models.Model):
    breeding_pair = models.ForeignKey(BreedingPair, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    size = models.IntegerField()

    def __str__(self):
        return f"Litter from {self.breeding_pair} born on {self.date_of_birth}"
