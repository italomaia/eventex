# coding:utf-8
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'eventex.views.home', name='home'),
    url(r'^inscricao/', include('subscriptions.urls', namespace='subscriptions')),

    # url(r'^admin/', include(admin.site.urls)),
)
