from django.shortcuts import render

# Create your views here.
def index(request):
  context = {
    'msg' : "No Ninjas here!",
    'img' : ""
  }
  return render(request, 'vanish/index.html', context)

def ninjas(request):
  context = {
  'msg' : "",
  'img' : "vanish/img/tmnt.png"
  }
  return render(request, 'vanish/index.html', context)

def process(request, name):
  context = {
    'msg' : "",
    'img' : "vanish/img/notapril.jpg"
  }

  if name == 'blue':
    context = {
    'img' : "vanish/img/leonardo.jpg"
    }

  if name == 'purple':
    context = {
    'img' : "vanish/img/donatello.jpg"
    }

  if name == 'red':
    context = {
    'img' : "vanish/img/raphael.jpg"
    }

  if name == 'orange':
    context = {
    'img' : "vanish/img/michelangelo.jpg"
    }

  return render(request, 'vanish/index.html', context)
