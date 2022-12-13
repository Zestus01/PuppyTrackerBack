from .models import *
from rest_framework import serializers

## These fields provide a bridgeway for what info the serializer is looking for
class BreedListingField(serializers.RelatedField):
    ## to_representation is similar to a get request. Its the representation of breeds
    def to_representation(self, instance):
        return instance.name
    ## to_internal_value is used for posts. It queries the model for the breed name given
    def to_internal_value(self, data):
        return Breed.objects.get(name=data)

class OwnerListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return f"{instance.id}: {instance.username} {instance.first_name} {instance.last_name}"
    
    def to_internal_value(self, data):
        return CustomUser.objects.get(id=data)

class DogListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.name

    def to_internal_value(self, data):
        return Dog.objects.get(id=data)    

class ActivityListListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.name

    def to_internal_value(self, data):
        return ActivityList.objects.get(name=data)    