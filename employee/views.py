from django.shortcuts import render
from rest_framework_mongoengine import viewsets

from employee.models import Employee
from employee.serializers import EmployeeSerializer

class EmployeeView(viewsets.ModelViewSet):
    lookup_field = 'empId'
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer