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

class DogCreate(APIView):
    """
    Creating a dog using breed index
    """
    def get(self, request, format=None):
        dog = Dog.objects.all()
        serializer = DogIDSerializer(dog, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DogIDSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def dog_create(request):
    """
    Gets the dog data with ID
    """
    if request.method == 'GET':
        dog = Dog.objects.all()
        serializer = DogIDSerializer(dog, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DogIDSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class DogTestViewSet(ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogTestSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


