from django.shortcuts import render, redirect, HttpResponse
from .models import Course, Description, Comment

# Create your views here.
def index(request):

  course=Course.objects.all()
  desc= Description.objects.all()

  context = {
    "courses": course,
    "desc": desc
  }
  return render(request, "course_app/index.html", context)

def go_back(request):
  return redirect('/')

def add(request):
  course = Course.objects.create(name=request.POST['name']) # course automatically getting assigned course_id, then referenced in description.create below

  Description.objects.create(desc=request.POST['desc'], course=course)
  return redirect('/')

def delete(request, id):

  
  instance = Course.objects.filter(id = id).delete()
  
  return redirect('/')
