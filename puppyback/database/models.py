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
    weight = models.DecimalField(default=5, max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])
    height = models.DecimalField(default=23, max_digits=5, decimal_places=2, blank=True, validators=[MinValueValidator(0)])
    breed = models.ManyToManyField('Breed', through='DogBreed', related_name='dog_breed')

    def __str__(self):
        return f"{self.name} ({self.gender})"

class Breed(models.Model):
    name = models.CharField(max_length=200)

    min_height_female = models.DecimalField(default=5, max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])
    max_height_female = models.DecimalField(default=25, max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])
    min_height_male = models.DecimalField(default=5, max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])
    max_height_male = models.DecimalField(default=25, max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])
    
    min_weight_female = models.DecimalField(default=5, max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])
    max_weight_female = models.DecimalField(default=55, max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])
    min_weight_male = models.DecimalField(default=5, max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])
    max_weight_male = models.DecimalField(default=55, max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

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
    """ 
    only pull in the PROVIDED DJANGO USER FIELDS that are going to be used in creating a user, 
    and then add your extended fields,
    __all__' pulls in all fields and creates an error for the validation step below
    """
    extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"

class ActivityList(models.Model):
    name = models.CharField(max_length=40, unique=True)
    dimension = models.CharField(max_length=20)
    verb = models.CharField(max_length=20, null=True);

    def __str__(self):
        return f"{self.name}: {self.dimension}"

class Activity(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name="activity_dog")
    activities = models.ForeignKey(ActivityList, on_delete=models.PROTECT, related_name="activity_activityaist")
    amount = models.TextField(max_length=15 ,blank=False)
    description = models.TextField(max_length=300, blank=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.dog} did {self.activities} {self.amount} at {self.time}"
    
    class Meta: 
        ordering = ['-time']

class WeightChange(models.Model):
    weight = models.DecimalField(default=5, max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])       
    time = models.DateTimeField(auto_now_add=True)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name="weight_dog")

    def __str__(self):
        return f"{self.dog} {self.weight} at {self.time}"

    class Meta:
        ordering = ['time']

class HeightChange(models.Model):
    height = models.DecimalField(default=23, max_digits=5, decimal_places=2, blank=True, validators=[MinValueValidator(0)])
    time = models.DateTimeField(auto_now_add=True)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name="height_dog")

    def __str__(self):
        return f"{self.dog} {self.height} at {self.time}"

    class Meta:
        ordering = ['time']