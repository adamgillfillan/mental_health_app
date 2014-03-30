from django.db import models


# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)


class Voltage(models.Model):
    voltage = models.IntegerField(default=0)
    user = models.ForeignKey(UserProfile)
    time = models.IntegerField()