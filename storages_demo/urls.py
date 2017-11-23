from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views
import images.views

urlpatterns = [
    url(r'^$', images.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]
