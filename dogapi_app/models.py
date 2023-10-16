from django.db import models

# Create your models here.
# dogapi_app/models.py

class Breed(models.Model):
    

    # Choices for 'size' field
    SIZE_CHOICES = [
        ('Tiny', 'Tiny'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    ]

    # Choices for friendliness, trainability, sheddingamount, and exerciseneeds fields
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    name = models.CharField(max_length=100, unique=True)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    friendliness = models.IntegerField(choices=RATING_CHOICES)
    trainability = models.IntegerField(choices=RATING_CHOICES)
    sheddingamount = models.IntegerField(choices=RATING_CHOICES)
    exerciseneeds = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    favoritefood = models.CharField(max_length=100)
    favoritetoy = models.CharField(max_length=100)
