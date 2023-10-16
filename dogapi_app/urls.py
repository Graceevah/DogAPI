# myapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BreedList, BreedDetail, DogList, DogDetail

router = DefaultRouter()
router.register(r'breeds', BreedList, basename='breed')
router.register(r'dogs', DogList, basename='dog')

urlpatterns = [
    path('', include(router.urls)),
    path('api/dogs/', DogList.as_view(), name='dog-list'),
    path('api/dogs/<int:pk>/', DogDetail.as_view(), name='dog-detail'),
    path('api/breeds/', BreedList.as_view(), name='breed-list'),
    path('api/breeds/<int:pk>/', BreedDetail.as_view(), name='breed-detail'),
]