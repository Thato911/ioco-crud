from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import PersonSerializer, EmployeeSerializer, PositionSerializer
from .models import Employee, Person, Position

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer