from django.shortcuts import render
import datetime
from django.utils.timezone import utc

# Create your views here. THIS IS THE CONTROLLER IN mvC or mtV
def index(request):
  time=datetime.datetime.utcnow().replace(tzinfo=utc)
  context={
  "somekey":time
  }
  return render(request, "time_control/index.html", context)
