from django.urls import path, include
from .views import *
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

router = routers.SimpleRouter()
router.register(r'dog', DogViewSet)  ## Base view, majority of information
router.register(r'user', UserViewSet)  ## For user information
router.register(r'activity', ActivityViewSet)  ## Just has the activitiy list name, not nested
router.register(r'list', ActivityListViewSet)  ## For the lsit of possible activities input
router.register(r'create', ActivityIDViewSet)  ## Create ativities, uses ID
router.register(r'nested', ActivityNestedViewSet)  ## Nested serializers
router.register(r'weight', WeightChangeViewSet)  ## For weight change
router.register(r'height', HeightChangeViewSet)  ## For height change
router.register(r'weightarray', WeightArrayViewSet)  ## Returns an array for the dog
router.register(r'heightarray', HeightArrayViewSet)  ## Returns an array of the heights for the dog
router.register(r'breed', BreedPostViewSet)  ## For detail view about breeds
router.register(r'breedlist', BreedListViewSet)  ## For just an array of breeds. 

urlpatterns = [
    path('user/create/', CustomUserCreate.as_view()),  ## For creating users
    path('', include(router.urls)),  ## base URLS
    path('edit/dog/<int:pk>/', DogDetail.as_view()),  ## For editing dogs 
    path('token/obtain/', ObtainTokenPairWithColorView.as_view(), name='token_create'), ## For login purposes
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),  ## For refresh 
    path('edit/activity/', ActivityDetail.as_view()),  ## For activity detail
    path('edit/activity/<int:pk>/', ActivityDetail.as_view()),  ## For editing activities 

]