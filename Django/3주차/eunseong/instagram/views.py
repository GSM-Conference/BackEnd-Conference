from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    사용자를 보거나 편집할 수 있는 API endpoint
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GruopViewSet(viewsets.ModelViewSet):
    """
    사용자를 보거나 편집할 수 있는 API endpoint
    """
    queryset = Group.objects.all()
    serializer_class =  GroupSerializer
    permissions_classes = [permissions.IsAuthenticated]

