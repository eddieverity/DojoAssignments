from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^time_control', index, name='home')

]
