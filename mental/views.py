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

    user_name = user_name_url
    context_dict = {'user_name': user_name,
                    'user_name_url': user_name_url}
    user_list = get_user_list()
    context_dict['user_list'] = user_list

    my_user = UserProfile.objects.get(name=user_name)
    voltages = Voltage.objects.filter(user=my_user)
    voltages_list = voltages

    context_dict['voltages'] = voltages_list
    context_dict['user'] = my_user


    # begin charting
    xdata = voltages_list.values('voltage')
    #ydata = voltages_list.values('time')
    ydata = voltages_list.values('user')
    chartdata = {'x': xdata,
                 'name1': user_name, 'y1': ydata}
    charttype = "lineChart"
    chartcontainer = 'linechart_container'
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {'x_is_date': False}
    }
    context_dict['data'] = data
    # Go render the response and return it to the client.
    return render_to_response('mental/user.html', context_dict, context)

# working code:
# def user(request, user_name_url):
#     context = RequestContext(request)
#
#     user_name = user_name_url
#     context_dict = {'user_name': user_name,
#                     'user_name_url': user_name_url}
#     user_list = get_user_list()
#     context_dict['user_list'] = user_list
#
#     my_user = UserProfile.objects.get(name=user_name)
#     voltages = Voltage.objects.filter(user=my_user)
#     voltages_list = voltages
#
#     context_dict['voltages'] = voltages_list
#     context_dict['user'] = my_user
#
#     # Go render the response and return it to the client.
#     return render_to_response('mental/user.html', context_dict, context)