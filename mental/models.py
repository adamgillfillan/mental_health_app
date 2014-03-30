from django.db import models


class Voltage(models.Model):
    voltage = models.IntegerField(default=0)


# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    voltage = models.ForeignKey(Voltage)




