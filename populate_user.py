__author__ = 'Adam'
import os
import random


def add_user(name, email):
    user = UserProfile.objects.get_or_create(name=name, email=email)[0]
    return user


def populate():
    add_user("Collin", "cyborg@ut.edu")
    for user in UserProfile.objects.all():
        print("Name: {0}, Email: {1}".format(
            user.name,
            user.email,
        ))
# Start execution here!
if __name__ == '__main__':
    print("Starting mental health population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mental_health.settings')
    from mental.models import UserProfile, Voltage
    populate()
