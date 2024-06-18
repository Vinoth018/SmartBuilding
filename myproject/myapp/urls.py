# myapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from .views import UserViewSet, BuildingViewSet
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'buildings', BuildingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
