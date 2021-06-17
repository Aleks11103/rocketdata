from rest_framework import generics, viewsets, permissions, views
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey
from .permissions import HasEmployeeAPIKey
from .serializers import EmployeeSerializer, EmployeeDetailSerializer
from .models import Employee, EmployeeAPIKey


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]


class EmployeeLevelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.filter(level='5')
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]


class EmployeeDetailView(generics.RetrieveAPIView):
    permission_classes = [HasEmployeeAPIKey]

    def get(self, request):
        print(request)
        key = request.META["HTTP_AUTHORIZATION"].split()[1]
        api_key = EmployeeAPIKey.objects.get_from_key(key)
        print('\n', api_key.employee_id, '\n')
        employee = Employee.objects.get(id=api_key.employee_id)
        print('\n', employee, '\n')
        data = EmployeeDetailSerializer(employee)
        print('\n', data.data, '\n')
        return Response({'employee': data.data}, content_type='application/json')