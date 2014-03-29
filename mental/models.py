from django.db import models


# Create your models here.
class UserProfile(models.Model):
    # Name of user. Use "User" model later
    # user = models.OneToOneField(User)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    voltage = models.IntegerField(default=0)


