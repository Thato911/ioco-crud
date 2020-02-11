from django.contrib.auth.models import User
from rest_framework import serializers, fields
from .models import Employee, Person, Position

class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = ('title', )

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    employee_date = serializers.DateField(input_formats=['%d-%m-%Y', 'iso-8601'])
    terminated = serializers.DateField(input_formats=['%d-%m-%Y', 'iso-8601'])
    class Meta:
        model = Employee
        fields = ('id', 'employee_num', 'employee_date', 'position', 'terminated')

    def __init__(self, *args, **kwargs):
        super(EmployeeSerializer,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['terminated'].required = False

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    employee = EmployeeSerializer(many=True)
    birth_date = serializers.DateField(input_formats=['%d-%m-%Y', 'iso-8601'])
    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'birth_date', 'employee')

    def create(self, validated_data):
        employee_data = validated_data.pop('employee')
        person = Person.objects.create(**validated_data)
        Employee.objects.create(person=person, **employee_data)
        return person

    def update( self, instance, validated_data):
        employee_data = validated_data.pop('employee')
        employee = instance.employee

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.save()

        employee.employee_num = employee_data.get('employee_num', employee.employee_num)
        employee.employee_date = employee_data.get('employee_date', employee.employee_date)
        employee.position = employee_data.get('position', employee.position)
        employee.terminated = employee_data.get('terminated', employee.terminated)
        employee.save()
        return instance


