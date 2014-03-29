from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from mental.models import UserProfile


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


def get_user_list():
    user_list = UserProfile.objects.all()
    return user_list