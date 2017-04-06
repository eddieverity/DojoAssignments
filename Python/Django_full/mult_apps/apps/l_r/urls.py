from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^l_r', views.index, name='home'),
    url(r'^register', views.register, name='register'),
    url(r'^login', views.login, name='login'),
    url(r'^success', views.success, name='success'),
]
