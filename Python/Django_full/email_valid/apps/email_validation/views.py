from django.shortcuts import render, redirect, HttpResponse
from .models import Email
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages


def ValidateEmail( email ):    
  try:
    validate_email( email )
    return True
  except ValidationError:
    return False

def index(request):
  return render(request, "email_validation/index.html")

def verify(request):
  email = request.POST['email']
  if ValidateEmail(email):
    request.session['semail']=request.POST['email']
    email = Email.objects.create(email=request.POST['email'])
    return redirect('/success')
  else:
    messages.error(request, 'Email address not valid!!')
    return redirect('/')

def success(request):
  email= Email.objects.all()
  context = {
    "email": email,   
  }
  return render(request, "email_validation/success.html", context)

def goback(request):
  request.session.clear()
  return redirect('/')
