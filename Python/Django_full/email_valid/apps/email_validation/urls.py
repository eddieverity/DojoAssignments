from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index),
  url(r'^verify', views.verify),
  url(r'^success', views.success),
  url(r'^goback', views.goback),

]