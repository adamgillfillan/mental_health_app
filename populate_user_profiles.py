__author__ = 'Adam'
import os
import random


def add_user(name, email):
    user = UserProfile.objects.get_or_create(name=name, email=email)[0]

    return user


def add_voltage(voltage, user, time):
    this_voltage = Voltage.objects.get_or_create(voltage=voltage, user=user, time=time)[0]

    return this_voltage


def add_many_voltages(user):
    x = random.randrange(100)
    seconds = random.randrange(1000)

    new_time = 1000 * seconds
    new_voltage = add_voltage(x, user, new_time)

    return new_voltage


def populate():
    collin = add_user("Collin", "cyborg@ut.edu")
    marc = add_user("Marc", "marcyMarc@ncsu.edu")
    sharon = add_user("Sharon", "sharon@unc.edu")
    adam = add_user("Adam", "baller@ncsu.edu")

    for i in range(100):
        add_many_voltages(collin)
        add_many_voltages(marc)
        add_many_voltages(sharon)
        add_many_voltages(adam)

    # Print out all users
    for user in UserProfile.objects.all():
        print("Name: {0}, Email: {1}".format(
            user.name,
            user.email,
        ))

    for voltage in Voltage.objects.all():
        print("Voltage: {0}, User: {1}, User Email: {2}, Time: {3}".format(
            voltage.voltage,
            voltage.user.name,
            voltage.user.email,
            voltage.time,
        ))

# Start execution here!
if __name__ == '__main__':
    print("Starting mental health population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mental_health.settings')
    from mental.models import UserProfile, Voltage
    populate()