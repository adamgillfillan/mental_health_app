__author__ = 'Adam'
import os
import random


def add_user(name, email, voltage):
    user = UserProfile.objects.get_or_create(name=name, email=email, voltage=voltage)[0]

    return user


def add_voltage(voltage):
    this_voltage = Voltage.objects.get_or_create(voltage=voltage)[0]

    return this_voltage


def add_many_voltages():
    my_array = []

    for i in range(100):
        x = random.randrange(100)
        new_voltage = add_voltage(x)
        my_array.append(new_voltage)

    return my_array


def add_many_users(voltages):
    my_users = []

    for i in range(len(voltages)):
        user_collin = add_user('Collin', 'cyborg@ut.edu', voltages[i])
        user_marc = add_user('Marc', 'markyMark@ncsu.edu', voltages[i])
        user_sharon = add_user('Sharon', 'sharon@unc.edu', voltages[i])
        user_adam = add_user('Adam', 'ballin@ncsu.edu', voltages[i])
        my_users.append(user_collin)
        my_users.append(user_marc)
        my_users.append(user_sharon)
        my_users.append(user_adam)

    return my_users


def populate():

    my_voltages = add_many_voltages()
    add_many_users(my_voltages)

    #Print out all users
    for user in UserProfile.objects.all():
        print("Name: {0}, Email: {1}, Voltage: {2}".format(
            user.name,
            user.email,
            user.voltage.voltage
        ))

    for voltage in Voltage.objects.all():
        print("Voltage: {0}".format(
            voltage.voltage,
        ))

# Start execution here!
if __name__ == '__main__':
    print("Starting mental health population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mental_health.settings')
    from mental.models import UserProfile, Voltage
    populate()