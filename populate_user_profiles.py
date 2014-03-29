__author__ = 'Adam'
import os


def add_user(name, email, voltage):
    user = UserProfile.objects.get_or_create(name=name, email=email, voltage=voltage)

    return user


def populate():

    add_user(name='Collin', email='cyborg@ut.edu', voltage='40')
    add_user(name='Marc', email='markyMark@ncsu.edu', voltage='20')
    add_user(name='Sharon', email='sharon@unc.edu', voltage='60')
    add_user(name='Adam', email='ballin@ncsu.edu', voltage='90')

    # Print out all users
    for user in UserProfile.objects.all():
        print("Name: {0}, Email: {1}, Voltage: {2}".format(
            user.name,
            user.email,
            user.voltage
        ))

# Start execution here!
if __name__ == '__main__':
    print("Starting mental health population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mental_health.settings')
    from mental.models import UserProfile
    populate()
