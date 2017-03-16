from django.shortcuts import render, redirect

# Create your views here.
def index(request):
  if 'counter' in request.session:
    request.session['counter'] += 1
  else:
    request.session['counter'] = 1
  return render(request, 'survey/index.html')

def process(request):
  if request.method == "POST":
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comments'] = request.POST['comments']
  
  return redirect('/results')

def results(request):

  return render(request, 'survey/results.html')

def goback(request):
  return redirect(request, '/')