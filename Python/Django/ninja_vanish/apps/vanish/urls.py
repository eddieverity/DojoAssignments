from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^ninjas/(?P<name>[a-zA-Z]+)$', process),
    url(r'^ninjas$', ninjas),
]

