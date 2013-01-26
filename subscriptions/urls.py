# coding:utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'subscriptions.views.subscribe', name='subscribe'),
    url(r'^(\d+)/$', 'subscriptions.views.subscription', name='subscription'),
)