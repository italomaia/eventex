from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'eventex.views.home', name='home'),
    url(r'^inscricao/$', 'subscriptions.views.subscribe', name='subscribe'),

    # url(r'^eventex/', include('eventex.foo.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)
