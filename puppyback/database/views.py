from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http.response import Http404
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, permissions, viewsets
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *

class DogList(ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

class DogDetail(APIView):
    """
    Retrieve, update or delete a artist instance.
    """
    def get_object(self, pk):
        try:
            return Dog.objects.get(pk=pk)
        except dog.DoesNotExist:
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

class DogUserDetailView(APIView):

    def get_object(self, pk):
        try:
            return Dog.objects.get(owner=pk)
        except dog.DoesNotExist:
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

class DogUserViewSet(ModelViewSet):
    serializer_class = CustomUserSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        return CustomUser.objects.get(username=self.request.user.username)

