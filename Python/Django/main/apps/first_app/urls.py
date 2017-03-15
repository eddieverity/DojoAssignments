from django.conf.urls import url

def index(request):
  print ('8'*10)
  print ("bananaphone")

urlpatterns = [
    url(r'^$', index)
]