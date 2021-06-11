from .models import Employee
from rest_framework import serializers


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['url', 'fio', 'position', 'date_of_employment', 'salary_amount', 'salary_paid', 'chief', 'level']


class EmployeeLevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['url', 'fio', 'position', 'date_of_employment', 'salary_amount', 'salary_paid', 'chief', 'level']