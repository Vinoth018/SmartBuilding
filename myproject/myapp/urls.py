# myapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, BuildingViewSet, CustomerViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'addbuildings', BuildingViewSet)
router.register(r'addcustomers', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
