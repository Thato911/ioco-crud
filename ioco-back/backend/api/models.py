from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()

    @property
    def employee(self):
        return self.employee_set.all()

    objects = models.Manager()

class Employee(models.Model):
    employee_num = models.CharField(max_length=16)
    employee_date = models.DateField()
    terminated = models.DateField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)


