from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from pesca_app.serializers import GroupSerializer, UserSerializer

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permissions_class = [permissions.IsAuthenticated]

class GroupViewset(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]