from django.shortcuts import render, redirect, HttpResponse
from .models import Course, Description, Comment, User, Enrollment
from django.db.models import Count

# Create your views here.
def index(request):

  course=Course.objects.all()
  desc= Description.objects.all()

  context = {
    "courses": course,
    "desc": desc
  }
  return render(request, "course_app/index.html", context)

def student_add(request):

  course=Course.objects.all().annotate(count=Count('enrollments__id'))
  student=User.objects.all()
  enrollment=Enrollment.objects.all()

  context = {
    "course": course,
    "student": student,
    "enrollment": enrollment,
  
  }


  return render(request, "course_app/student_add.html", context)

def enroll(request):
  enroll = Enrollment.objects.create(course_id=request.POST['course'], student_id=request.POST['student'])

  return redirect('course_app:student_add')



def go_back(request):
  return redirect('course_app:home')

def add(request):
  course = Course.objects.create(name=request.POST['name'], number_enrolled=0) # course automatically getting assigned course_id, then referenced in description.create below

  Description.objects.create(desc=request.POST['desc'], course=course)
  return redirect('course_app:home')

def delete(request, id):

  
  instance = Course.objects.filter(id = id).delete()
  
  return redirect('course_app:home')
