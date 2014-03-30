__author__ = 'Adam'

from django.conf.urls import patterns, url
from mental import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^users', views.users, name='users'),
    url(r'^voltages', views.voltages, name='voltages'),
    url(r'^user/(?P<user_name_url>\w+)/$', views.user, name='user'),
    url(r'^addvoltages', views.addvoltages),
    )
