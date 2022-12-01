from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http.response import Http404
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, permissions, viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import *
from .serializers import *

class DogDetail(APIView):
    """
    Retrieve, update or delete a Dog instance.
    """
    def get_object(self, pk):
        try:
            return Dog.objects.get(pk=pk)
        except Dog.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dog = self.get_object(pk)
        serializer = DogSerializer(dog)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        dog = self.get_object(pk)
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        dog = self.get_object(pk)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

## Can also use the dog's name and activity name 
## ?dog__id=7&activities__id=3 Gets the activities for dog 7 and activity 3
class ActivityViewSet(ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['dog__id', 'dog__name', 'activities__name', 'activities__id']

class ActivityIDViewSet(ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivityIDSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['dog__id', 'dog__name', 'activities__name', 'activities__id']    

class ActivityListViewSet(ModelViewSet):
    queryset = ActivityList.objects.all()
    serializer_class = ActivityListSerializer
    permission_classes = (permissions.AllowAny,)

class DogViewSet(ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogBestSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['owner__id', 'owner__username']

class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = OwnerSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class ObtainTokenPairWithColorView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class CustomUserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (permissions.AllowAny,)

class ActivityDetail(APIView):
    """
    Retrieve, update or delete an Activity instance.
    """
    def get_object(self, pk):
        try:
            return Activity.objects.get(pk=pk)
        except Activity.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        activity = self.get_object(pk)
        serializer = ActivitySerializer(activity)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        activity = self.get_object(pk)
        serializer = ActivitySerializer(activity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        activity = self.get_object(pk)
        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)