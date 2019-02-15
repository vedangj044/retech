from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.conf import settings
# Create your models here.
class vehicle(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    register = models.CharField(max_length=10)
    people = models.CharField(max_length=10)
    model = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class ride(models.Model):
    to = models.CharField(max_length=100)
    fro = models.CharField(max_length=100)
    contact_date = models.DateField(blank=True)
    contact_time = models.TimeField(blank=True)
    vehicl = models.ForeignKey(vehicle, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cont = models.ForeignKey(ride, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
