from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^l_r/$', l_r, name='l_r'),
    url(r'^golds/$', golds, name='golds'),
    url(r'^course_app/$', course_app, name='course_app'),
    url(r'^random_app/$', random_app, name='random_app'),
    url(r'^time_control/$', time_control, name='time_control'),
    
]