from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser


class Dog(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]
    name = models.CharField(max_length=200)
    age = models.SmallIntegerField(default=1, validators=[MinValueValidator(0)])
    owner = models.ManyToManyField('CustomUser', through='DogUser', related_name='dog_user')
    gender = models.CharField(max_length=12, choices=GENDER_CHOICES)
    weight = models.SmallIntegerField(default=40)
    height = models.SmallIntegerField(null=True, blank=True)
    breed = models.ManyToManyField('Breed', through='DogBreed', related_name='dog_breed')

    def __str__(self):
        return f"{self.name} ({self.gender}) owner is {self.owner}"

class Breed(models.Model):
    name = models.CharField(max_length=200)

    min_height_female = models.SmallIntegerField(default=5)
    max_height_female = models.SmallIntegerField(default=40)
    min_height_male = models.SmallIntegerField(default=8)
    max_height_male = models.SmallIntegerField(default=45)
    
    min_weight_female = models.SmallIntegerField(default=5)
    max_weight_female = models.SmallIntegerField(default=40)
    min_weight_male = models.SmallIntegerField(default=8)
    max_weight_male = models.SmallIntegerField(default=45)

    def __str__(self):
        return self.name

class DogBreed(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            ['dog', 'breed']
        )
    
    def __str__(self):
        return f"{self.dog} => {self.breed}"

class DogUser(models.Model):
    dog = models.OneToOneField(Dog, on_delete=models.CASCADE)
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            ['dog', 'user']
        )

    def __str__(self):
        return f"{self.dog}"

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"