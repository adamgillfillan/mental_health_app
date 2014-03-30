from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from mental.models import UserProfile, Voltage
from django.http import HttpResponse


# import the logging library


# Create your views here.
def index(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('mental/index.html', context_dict, context)


def users(request):
    context = RequestContext(request)

    user_list = get_user_list()

    context_dict = {'user_list': user_list}
    return render_to_response('mental/users.html', context_dict, context)


def voltages(request):
    context = RequestContext(request)

    voltage_list = get_voltage_list()

    context_dict = {'voltage_list': voltage_list}
    return render_to_response('mental/voltages.html', context_dict, context)


def get_user_list():
    user_list = UserProfile.objects.all()
    return user_list


def get_voltage_list():
    voltage_list = Voltage.objects.all()
    return voltage_list


def addvoltages(request):
    if (request.method == "POST"):
        print(request.POST)
        v = Voltage(voltage = request.POST['voltages'], user = get_user_list()[0])
        v.save()
    return HttpResponse('Data added')
        
def user(request, user_name_url):
    context = RequestContext(request)

    user_name = user_name_url.replace('_', ' ')
    context_dict = {'user_name': user_name,
                    'user_name_url': user_name_url}
    user_list = get_user_list()
    context_dict['user_list'] = user_list

    try:
        my_user = UserProfile.objects.get(name=user_name)
        voltages = Voltage.objects.filter(user=my_user)
        voltages_list = voltages.order_by('-voltages')

        # Adds our results list to the template context under name pages.
        context_dict['voltages'] = voltages_list

        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['user'] = my_user

    except UserProfile.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render_to_response('mental/user.html', context_dict, context)