from .models import Employee
from rest_framework import serializers


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['url', 'fio', 'position', 'date_of_employment', 'salary_amount', 'salary_paid', 'chief', 'level']


class EmployeeDetailSerializer(serializers.Serializer):
    fio = serializers.CharField(max_length=150)
    position = serializers.CharField(max_length=100 )
    date_of_employment = serializers.DateField()
    salary_amount = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    salary_paid = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    level = serializers.CharField(max_length=1)

    class Meta:
        model = Employee
        fields = '__all__'