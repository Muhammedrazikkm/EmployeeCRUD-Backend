from django.db import models

# Create your models here.

#  name: new FormControl(),
#       email: new FormControl(),
#       department: new FormControl(),
#       phone: new FormControl(),
#       salary: new FormControl()

class Employee(models.Model):
    name=models.CharField(max_length=250)
    email=models.CharField(max_length=200)
    department=models.CharField(max_length=250)
    phone=models.CharField(max_length=200)
    salary=models.PositiveIntegerField()

    def __str__(self):
        return self.name