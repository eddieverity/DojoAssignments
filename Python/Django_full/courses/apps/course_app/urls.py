from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index),
  url(r'^go_back', views.go_back),
  url(r'^add', views.add),
  url(r'^delete/(?P<id>\d+)$', views.delete),

]