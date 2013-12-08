from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'demo.views.index'),
    url(r'^basic/$', 'demo.views.basic'),
    url(r'^horizontal/$', 'demo.views.horizontal'),

    url(r'^admin/', include(admin.site.urls)),
)
