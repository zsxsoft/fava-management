from django.contrib import admin
from django.conf.urls import url
from django.urls import path

import proxy.views

urlpatterns = [
    path('', admin.site.urls),
    url(r'fava/(?P<path>.*)$', proxy.views.ReverseFava.as_view()),
    path('control/restart/', proxy.views.restart),
]
