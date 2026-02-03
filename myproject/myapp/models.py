from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200,blank=True, null=True)
    phone = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
