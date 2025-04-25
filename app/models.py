from django.db import models

# Create your models here.

class Employee(models.Model):
    Empname=models.CharField(max_length=50)
    Empid=models.IntegerField()
    Empdept=models.CharField(max_length=20)
    Address=models.TextField()

    def __str__(self):
        return self.Empname
    

