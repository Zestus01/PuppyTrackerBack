from rest_framework import serializers
from .models import Dog, DogBreed, DogUser, Breed, CustomUser

class DogBreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = DogBreed
        fields = "__all__"

class DogUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DogUser
        fields = "__all__"

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['id', 'name']

class DogSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()
    breed = BreedSerializer(many=True)
    class Meta:
        model = Dog
        fields = ['id', 'name', 'owner', 'gender', 'weight', 'height', 'breed']

