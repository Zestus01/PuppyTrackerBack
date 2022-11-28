from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets

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

