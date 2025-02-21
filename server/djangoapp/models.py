# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    TYPE_CHOICES = [
        ('suv', 'SUV'),
        ('sedan', 'Sedan'),
        ('hatchback', 'Hatchback'),
        ('coupe', 'Coupe'),
        ('Minivan', 'minivan'),
        ('pickup', 'Pickup'),
        ('convertible', 'Convertible')
    ]

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=15, choices=TYPE_CHOICES, default='SUV')
    year = models.IntegerField(default=2023, validators= [MinValueValidator(2015), MaxValueValidator(2023)])

    def __str__(self):
        return self.name