from .models import *
from rest_framework import serializers

class BreedListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.name
    
    def to_internal_value(self, data):
        return Breed.objects.get(name=data)