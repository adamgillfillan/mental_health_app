from django.template import RequestContext
from django.shortcuts import render_to_response
from mental.models import UserProfile, Voltage
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import random
import datetime
import time

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
        mytime = int(time.time())
        print(mytime)
        v = Voltage(voltage = request.POST['voltages'], user = get_user_list()[0], time = mytime)
        v.save()
    return HttpResponse('Data added')

def cleardb(request):
    Voltage.objects.all().delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

#
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


    # # begin charting
    # xdata = voltages_list.values('voltage')
    # #ydata = voltages_list.values('time')
    # ydata = voltages_list.values('user')
    # chartdata = {'x': xdata,
    #              'name1': user_name, 'y1': ydata}
    # charttype = "lineChart"
    # chartcontainer = 'linechart_container'
    # data = {
    #     'charttype': charttype,
    #     'chartdata': chartdata,
    #     'chartcontainer': chartcontainer,
    #     'extra': {'x_is_date': False}
    # }
    # context_dict['data'] = data
    # # Go render the response and return it to the client.
    # return render_to_response('mental/user.html', context_dict, context)
    #
    # start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)
    # nb_element = 100
    # xdata = range(nb_element)
    # xdata = map(lambda x: start_time + x * 1000000000, xdata)
    # ydata = [i + random.randint(1, 10) for i in range(nb_element)]
    # ydata2 = map(lambda x: x * 2, ydata)
    #
    # tooltip_date = "%d %b %Y %H:%M:%S %p"
    # extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"},
    #                "date_format": tooltip_date}
    # chartdata = {'x': xdata,
    #              'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie,
    #              'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie}
    # charttype = "lineChart"
    # data = {
    #     'charttype': charttype,
    #     'chartdata': chartdata,
    #     'extra': {
    #         'x_is_date': True,
    #         'x_axis_format': "%d %b %Y %H"
    #     }
    # }
    # return render_to_response('mental/user.html', context_dict, context)


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

    # Go render the response and return it to the client.
    return render_to_response('mental/user.html', context_dict, context)