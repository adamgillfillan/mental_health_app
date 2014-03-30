from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from mental.models import UserProfile, Voltage


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