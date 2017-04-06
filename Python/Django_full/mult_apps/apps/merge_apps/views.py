from django.shortcuts import render, redirect

# Create your views here.
def index(request):
  return render(request, 'merge_apps/index.html')

def l_r(request):
  return redirect('l_r:home')

def golds(request):
  return redirect('golds:home')
def course_app(request):
  return redirect('course_app:home')
def random_app(request):
  return redirect('random_app:home')
def time_control(request):
  return redirect('time_control:home')
