from django.conf.urls import url, include
from views import *


urlpatterns = [
    url(r'^random_app', index, name='home'),
    url(r'^random_word$', random_word, name='random_word'),
    url(r'^reset$', reset, name='reset')
]
