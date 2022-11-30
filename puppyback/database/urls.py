from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'dog', DogViewSet)
router.register(r'user', UserViewSet)
router.register(r'doguser', DogUserViewSet, basename='DogUser')

urlpatterns = [
    path('', include(router.urls)),
    path('dog/<int:dog_id>/', DogDetail.as_view()),
    path('test/<int:dog_id>/', DogUserDetailView.as_view()),

]