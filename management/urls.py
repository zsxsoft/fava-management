from django.contrib import admin
from django.urls import re_path
from django.urls import path

import proxy.views

urlpatterns = [
    re_path(r'fava/(?P<path>.*)$', proxy.views.ReverseFava.as_view()),
    path('control/restart/', proxy.views.restart),
    path('', admin.site.urls),
]
