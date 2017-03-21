from django.shortcuts import render, redirect, HttpResponse

from django.contrib import messages
from .models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re
import bcrypt

def badname_regex(name):
  reggie=re.compile(r'^[a-zA-Z]+$')
  if reggie.match(name) is None:
    return True

def index(request):
  return render(request, "l_r/index.html")

def DupEmail(email):
  try:
    User.objects.get(email = email)
    return True
  #tried ValidationError
  except User.DoesNotExist:
    return False

def register(request):
 

  is_valid = True
  first_name = request.POST['first_name']
  last_name = request.POST['last_name']
  email = request.POST['email']
  password = request.POST['password'].encode(encoding="utf-8")
  confirm = request.POST['confirm']
  pw_hash=bcrypt.hashpw(password, bcrypt.gensalt())

  if ValidateEmail(email) != True:
    messages.error(request, 'email address not valid')
    is_valid = False

  if DupEmail(email):
    messages.error(request, 'email address in use')
    is_valid= False

  if badname_regex(first_name) or badname_regex(last_name):
    messages.error(request, 'name must contain letters only')
    return redirect('/')  
  
  if len(first_name) < 2:
    messages.error(request, 'name must be at least 2 characters long')
    is_valid = False
  if len(last_name) < 2:
    messages.error(request, 'name must be at least 2 characters long')
    is_valid = False

  if len(password) < 8:
    messages.error(request, 'password must be at least 8 characters long')
    is_valid = False
  if password != confirm:
    messages.error(request, 'passwords do not match')
    is_valid = False
    
  if is_valid:

    curr_user= User.objects.create(
      first_name=request.POST['first_name'],
      last_name=request.POST['last_name'],
      email=request.POST['email'],
      password= pw_hash
      )


    request.session['s_first_name']=request.POST['first_name']
    request.session['msg']='registered'

    return redirect('/success')
   

  else:
    return redirect('/')

  

def login(request):
  l_email=request.POST['l_email']
  try:
    curr_user=User.objects.get(email = l_email)

    # print pw_hash
    # print curr_user.password

    l_password=request.POST['l_password'].encode(encoding="utf-8")
    if bcrypt.hashpw(l_password, curr_user.password.encode("utf-8")) == curr_user.password:
      request.session['s_first_name']=curr_user.first_name
      request.session['msg']='logged in'
      return redirect('/success')
    else:
      messages.error(request, 'password does not match registered user')
      return redirect('/')
  except User.DoesNotExist:
    messages.error(request, 'email does not exist in database, please register')
    return redirect('/')

  pass


def success(request):
  pass
  return render(request, "l_r/success.html")

def ValidateEmail( email ):    
  try:
    validate_email( email )
    return True
  except ValidationError:
    return False


   
