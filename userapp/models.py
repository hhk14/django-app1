from django.db import models
from django.urls import reverse
# Create your models here.

class Employee(models.Model):
    ename = models.CharField(max_length=50)
    eno = models.IntegerField()
    esal = models.FloatField()
    eaddr = models.CharField(max_length=50)

    def get_absolute_url(self):       
        return reverse('list', kwargs={})