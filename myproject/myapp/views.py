# myapp/views.py
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import UserSerializer
from .models import Building
from .serializers import BuildingSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'])
    def list_users(self, request):
        users = User.objects.all()
        data = [{'username': user.username, 'password': '******'} for user in users]
        return Response(data)



class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer