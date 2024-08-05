from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from api.models import Mouse, Cage, BreedingPair, Litter
from django.utils import timezone
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Generate test data'

    def handle(self, *args, **kwargs):
        # Create users
        test_user = User.objects.create_user(
            username='testuser',
            password='password',
            email='testuser@example.com',
            first_name='Test',
            last_name='User'
        )

        # Create mice
        mice = []
        for i in range(10):
            mouse = Mouse.objects.create(
                ear_tag=f"A{i:03}",
                gender=random.choice(['M', 'F']),
                date_of_birth=timezone.now().date(),
                genotype=random.choice(['WT', 'KO']),
                strain=random.choice(['C57BL/6', 'BALB/c']),
                owner=test_user
            )
            mice.append(mouse)

        # Create cages
        cages = []
        for i in range(5):
            cage = Cage.objects.create(
                cage_number=f"C{i:03}",
                capacity=5
            )
            cage.mice.set(mice[i*2:(i+1)*2])
            cages.append(cage)

        # Create breeding pairs
        breeding_pairs = []
        for i in range(3):
            breeding_pair = BreedingPair.objects.create(
                name=f"Pair{i:02}",
                male=Mouse.objects.filter(gender='M').first(),
                female=Mouse.objects.filter(gender='F').first(),
                start_date=timezone.now().date()
            )
            breeding_pairs.append(breeding_pair)

        # Create litters
        for i in range(2):
            Litter.objects.create(
                breeding_pair=random.choice(breeding_pairs),
                date_of_birth=timezone.now().date(),
                size=random.randint(1, 10)
            )

        self.stdout.write(self.style.SUCCESS('Test data generated successfully'))
