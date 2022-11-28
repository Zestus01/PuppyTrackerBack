from django.urls import path
from database.views import *

urlpatterns = [
    path('dog/', DogList.as_view()),
    path('dog/<int:dog_id>/', DogDetail.as_view())
]