from rest_framework import serializers
from .models import Dog, DogBreed, DogUser, Breed, CustomUser, Activity, ActivityList, HeightChange, WeightChange
from .fields import BreedListingField, OwnerListingField, ActivityListListingField, DogListingField
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

## Will return all the info for the breed combos
class DogBreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = DogBreed
        fields = "__all__"

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name']

## For pulling the breed name and individual ID
class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['id', 'name']

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ['id', 'name', 'gender', 'weight', 'height', 'breed']

## Most commonly used dog serializers, pulls the data and pieces I like.
class DogBestSerializer(serializers.ModelSerializer):
    breed = BreedListingField(many=True, queryset=Breed.objects.all(), required=True)
    owner = OwnerListingField(many=True, queryset=CustomUser.objects.all(), required=False)
    class Meta:
        model = Dog
        fields = ['id', 'name', 'gender', 'weight', 'height', 'breed', 'owner']

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    username = serializers.CharField()
    password = serializers.CharField(min_length=4, write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token

class ActivityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityList
        fields = ['id', 'name', 'dimension', 'verb']
## Pulls he activity and allows posting with the dog's name
class ActivitySerializer(serializers.ModelSerializer):
    dog = DogListingField(many=False, queryset=Dog.objects.all(), required=True)
    activities = ActivityListListingField(many=False, queryset=ActivityList.objects.all(), required=False)
    class Meta:
        model = Activity
        fields = ['id', 'dog', 'activities', 'amount', 'description', 'time']
## The serializer that uses the dog's id to post
class ActivityIDSerializer(serializers.ModelSerializer):
    activities = ActivityListListingField(many=False, queryset=ActivityList.objects.all(), required=False)
    class Meta:
        model = Activity
        fields = ['id', 'dog', 'activities', 'amount', 'description', 'time']        

class ActivityNestedSerializer(serializers.ModelSerializer):
    activities = ActivityListSerializer(many=False)
    dog = DogListingField(many=False, queryset=Dog.objects.all(), required=True)
    class Meta:
        model = Activity
        fields = ['id', 'dog', 'activities', 'amount', 'description', 'time']

class WeightChangeSerializer(serializers.ModelSerializer):
    dog = DogListingField(many=False, queryset=Dog.objects.all(), required=True)
    class Meta:
        model = WeightChange
        fields = ['id', 'weight', 'time', 'dog',]

class HeightChangeSerializer(serializers.ModelSerializer):
    dog = DogListingField(many=False, queryset=Dog.objects.all(), required=True)
    class Meta:
        model = HeightChange
        fields = ['id', 'height', 'time', 'dog',]
## Gets a dog's weight change into an array
class WeightArraySerializers(serializers.ModelSerializer):
    weight = serializers.SerializerMethodField()

    class Meta:
        model = WeightChange
        fields = ['weight']

    def get_weight(self, object):
        dogWeights = WeightChange.objects.filter(dog=object.id);
        weightArray = []

        for item in dogWeights:
            weightArray.append(item.weight)
        
        return weightArray

class HeightArraySerializers(serializers.ModelSerializer):
    height = serializers.SerializerMethodField()

    class Meta:
        model = HeightChange
        fields = ['height']

    def get_height(self, object):
        dogHeights = HeightChange.objects.filter(dog=object.id);
        heightArray = []

        for item in dogHeights:
            heightArray.append(item.height)
        
        return heightArray

class BreedPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Breed
        fields = "__all__"

class BreedListSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Breed
        fields = ['name']
    
    def get_name(self, object):
        breedList = Breed.objects.all();
        nameArray = []

        for item in breedList:
            nameArray.append(item.name)
        
        return nameArray

## Objective to get all the needed data in one big object to mess with front end
class BigDataSerializer(serializers.ModelSerializer):
    pass