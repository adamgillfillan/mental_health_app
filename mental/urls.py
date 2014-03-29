__author__ = 'Adam'

from django.conf.urls import patterns, url
from mental import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
)
