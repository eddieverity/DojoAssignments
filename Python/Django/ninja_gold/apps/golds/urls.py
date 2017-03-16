from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^process_money$', process_money),
    url(r'^reset$', reset)

]