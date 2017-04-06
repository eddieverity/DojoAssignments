"""mult_apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include


urlpatterns = [
  

    url(r'^', include('apps.merge_apps.urls', namespace='merge_apps')),
    url(r'^time_control/', include('apps.time_control.urls', namespace='time_control')),
    url(r'^course_app/', include('apps.course_app.urls', namespace='course_app')),
    url(r'^golds/', include('apps.golds.urls', namespace='golds')),
    url(r'^l_r/', include('apps.l_r.urls', namespace='l_r')),
    url(r'^random_app/', include('apps.random_app.urls', namespace='random_app'))
]
