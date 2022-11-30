from .models import *
from rest_framework import serializers

class BreedListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.name
    
    def to_internal_value(self, data):
        return Breed.objects.get(name=data)

class OwnerListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return f"{instance.id}: {instance.username} {instance.first_name} {instance.last_name}"
    
    def to_internal_value(self, data):
        return CustomUser.objects.get(username=data)