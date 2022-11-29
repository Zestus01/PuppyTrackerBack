from rest_framework import serializers
from .models import Dog, DogBreed, DogUser, Breed, CustomUser
from .fields import BreedListingField, OwnerListingField

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
        fields = ['id', 'username', 'first_name', 'last_name']

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['id', 'name']

class DogSerializer(serializers.ModelSerializer):
   ## owner = OwnerSerializer()
    breed = BreedSerializer(many=True)
    class Meta:
        model = Dog
        fields = ['id', 'name', 'gender', 'weight', 'height', 'breed']

class DogTestSerializer(serializers.ModelSerializer):
    breed = BreedListingField(many=True, queryset=Breed.objects.all(), required=True)
    owner = OwnerListingField(many=True, queryset=CustomUser.objects.all(), required=False)
    class Meta:
        model = Dog
        fields = ['id', 'name', 'gender', 'weight', 'height', 'breed', 'owner']
  