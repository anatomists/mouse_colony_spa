# Generated by Django 5.0.7 on 2024-07-28 01:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BreedingPair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Litter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField()),
                ('size', models.IntegerField()),
                ('breeding_pair', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.breedingpair')),
            ],
        ),
        migrations.CreateModel(
            name='Mouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ear_tag', models.CharField(max_length=20, unique=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('date_of_birth', models.DateField()),
                ('genotype', models.CharField(max_length=100)),
                ('strain', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cage_number', models.CharField(max_length=20, unique=True)),
                ('capacity', models.IntegerField(default=5)),
                ('mice', models.ManyToManyField(related_name='cages', to='api.mouse')),
            ],
        ),
        migrations.AddField(
            model_name='breedingpair',
            name='female',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='female_breedings', to='api.mouse'),
        ),
        migrations.AddField(
            model_name='breedingpair',
            name='male',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='male_breedings', to='api.mouse'),
        ),
    ]
