from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^process$', process),
    url(r'^results$', results),
    url(r'^goback$', goback)

]