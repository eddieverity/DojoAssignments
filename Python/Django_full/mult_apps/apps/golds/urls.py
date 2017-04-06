from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^golds', index, name='home'),
    url(r'^process_money$', process_money, name='process_money'),
    url(r'^reset$', reset, name='reset')

]