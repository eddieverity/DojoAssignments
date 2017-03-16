from django.conf.urls import url, include
from views import *


urlpatterns = [
    url(r'^$', index),
    url(r'^random_word$', random_word),
    url(r'^reset$', reset)
]
