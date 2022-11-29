from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'dog', DogTestViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dog/<int:dog_id>/', DogDetail.as_view()),

]