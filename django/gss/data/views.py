from rest_framework import viewsets
from rest_framework import permissions

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from data.serializers import UserSerializer, GroupSerializer, ProjectSerializer
from data.models import Project
from data.permission import IsWebuser, IsCoordinator, IsSurveyor, IsSuperUser


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsWebuser | IsSurveyor, permissions.IsAuthenticated]
        elif self.action == "create":
            permission_classes = [IsCoordinator, permissions.IsAuthenticated]
        else:
            permission_classes = [IsSuperUser, permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsWebuser | IsSurveyor, permissions.IsAuthenticated]
        elif self.action == "create":
            permission_classes = [IsCoordinator, permissions.IsAuthenticated]
        else:
            permission_classes = [IsSuperUser, permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsWebuser | IsSurveyor, permissions.IsAuthenticated]
        elif self.action == "create":
            permission_classes = [IsCoordinator, permissions.IsAuthenticated]
        else:
            permission_classes = [IsSuperUser, permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    # def get_serializer_class(self):
    #     if self.request.method in ["POST", "PUT"]:
    #         return ProjectSerializer
    #     else:
    #         return ProjectSerializer

