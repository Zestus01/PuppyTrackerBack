from django.urls import path, include
from .views import *
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

router = routers.SimpleRouter()
router.register(r'dog', DogViewSet)
router.register(r'user', UserViewSet)
router.register(r'activity', ActivityViewSet)
router.register(r'list', ActivityListViewSet)
router.register(r'create', ActivityIDViewSet)

urlpatterns = [
    path('user/create/', CustomUserCreate.as_view()),
    path('', include(router.urls)),
    path('edit/dog/<int:pk>/', DogDetail.as_view()),
    path('token/obtain/', ObtainTokenPairWithColorView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('edit/activity/<int:pk>/', ActivityDetail.as_view()),
    path('edit/activity/', ActivityDetail.as_view()),

]