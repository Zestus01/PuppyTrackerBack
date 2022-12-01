from rest_framework import serializers
from .models import Dog, DogBreed, DogUser, Breed, CustomUser, Activity, ActivityList
from .fields import BreedListingField, OwnerListingField, ActivityListingField, DogListingField
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class DogBreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = DogBreed
        fields = "__all__"

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name']

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['id', 'name']

class DogSmallSerializer(serializers.ModelSerializer):
   ## owner = OwnerSerializer()
    # breed = BreedSerializer(many=True)
    class Meta:
        model = Dog
        fields = ['id', 'name']

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
        fields = ['id', 'name', 'dimension']

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'dog', 'activities', 'amount', 'description', 'time']
