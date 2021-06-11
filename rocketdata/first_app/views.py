from rest_framework import serializers, viewsets, permissions
from .serializers import EmployeeSerializer, EmployeeLevelSerializer
from .models import Employee


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # permission_classes = [permissions.IsAdminUser]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EmployeeLevelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.filter(level='5')
    serializer_class = EmployeeLevelSerializer
    # permission_classes = [permissions.IsAdminUser]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
