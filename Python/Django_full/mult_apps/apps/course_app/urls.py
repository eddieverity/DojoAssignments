from django.conf.urls import url, include
from . import views

urlpatterns = [
  url(r'^course_app', views.index, name='home'),
  url(r'^go_back', views.go_back, name='go_back'),
  url(r'^add', views.add, name='add'),
  url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
  url(r'^student_add', views.student_add, name='student_add'),
  url(r'^enroll', views.enroll, name='enroll'),

]