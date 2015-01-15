__author__ = 'ghost'

from django.conf.urls import patterns, include, url
from signage import views

urlpatterns = patterns('',
    url(r'^$', views.Index.as_view(), name='index'),
)
