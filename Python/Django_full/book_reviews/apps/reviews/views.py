from django.shortcuts import render, redirect, HttpResponse, reverse
from .models import User, Book, Review
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re
import bcrypt
from django.db.models import Count



# Create your views here.
def index(request):

  return render(request, 'reviews/login.html')

def badname_regex(name):
  reggie=re.compile(r'^[a-zA-Z]+$')
  if reggie.match(name) is None:
    return True

def DupEmail(email):
  try:
    User.objects.get(email = email)
    return True
  #tried ValidationError
  except User.DoesNotExist:
    return False

def register(request):
 

  is_valid = True
  name = request.POST['name']
  alais = request.POST['alias']
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

  if badname_regex(name):
    messages.error(request, 'name must contain letters only')
    return redirect('reviews:login')  
  
  if len(name) < 2:
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
      name=request.POST['name'],
      alias=request.POST['alias'],
      email=request.POST['email'],
      password= pw_hash
      )


    request.session['alias']=request.POST['alias']
    request.session['msg']='registered'
    request.session['id']=curr_user.id
    return redirect('reviews:books')
   

  else:
    return redirect('reviews:index')

def login(request):
  l_email=request.POST['l_email']
  try:
    curr_user=User.objects.get(email = l_email)

    # print pw_hash
    # print curr_user.password
    # it's not 'if this hashed password = entered hashed password'
    l_password=request.POST['l_password'].encode(encoding="utf-8")
    if bcrypt.hashpw(l_password, curr_user.password.encode("utf-8")) == curr_user.password:
      request.session['alias']=curr_user.alias
      request.session['id']=curr_user.id
      request.session['msg']='logged in'
      return redirect('reviews:books')
    else:
      messages.error(request, 'password does not match registered user')
      return redirect('reviews:index')
  except User.DoesNotExist:
    messages.error(request, 'email does not exist in database, please register')
    return redirect('reviews:index')
def ValidateEmail( email ):    
  try:
    validate_email( email )
    return True
  except ValidationError:
    return False

def logout(request):
  request.session.clear()
  return redirect('reviews:index')
  pass

def books(request):
  context = {
    'books' : Book.objects.all(),
    'User' : User.objects.all(),
    'current_reviews' : Review.objects.filter().order_by('-created_at')[:4]
  }
  print context
  return render(request, 'reviews/books.html', context)


def add(request):
  context = {
    'books': Book.objects.all(),
  }
  return render(request, 'reviews/add.html', context)

def add_book(request):
  name = request.POST['name']
  author = request.POST['author']
  review = request.POST['review']
  rating = request.POST['rating']
  curr_book= Book.objects.create(
  name=request.POST['name'],
  author=request.POST['author'],
  )

  Review.objects.create(
  rating=rating,
  book_id=curr_book.id,
  description=review,
  poster_id=request.session['id']
  )
  url = reverse('reviews:book_display', kwargs={'book_id':curr_book.id})
  return redirect(url)

def book_display(request, book_id):
  curr_user=request.session['id']
  context = {
    'books': Book.objects.filter(id=book_id),
    'reviews': Review.objects.filter(book_id=book_id),
    'user': User.objects.all(),
    'curr_user': curr_user
  }

  return render(request, 'reviews/book_display.html', context)

def user_display(request, user_id):
  context = {
    'user': User.objects.get(id=user_id),
    'total_reviews': Review.objects.filter(poster_id=user_id).count()
  }
  print context
  return render(request, 'reviews/user.html', context)
