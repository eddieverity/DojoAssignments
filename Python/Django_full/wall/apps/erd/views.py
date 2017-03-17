from django.shortcuts import render
from .models import User, Message, Comment

# Create your views here.
def index(request):
  User.objects.create(first_name="Ed", last_name="Verity")
  user= User.objects.all()
  print user
  render(request, "erd/index.html")