from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'dog', DogList)
router.register(r'test', DogTestViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dog/<int:dog_id>/', DogDetail.as_view()),
    path('dog/create/', DogCreate.as_view()),
    path('dog/test/', dog_create),

]