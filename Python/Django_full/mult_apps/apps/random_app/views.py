from django.shortcuts import render, HttpResponse, redirect
import random
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):

  unique_id = get_random_string(length=14)
  unique_word={"somekey":unique_id}

  if 'counter' in request.session:
    request.session['counter'] += 1
  else:
    request.session['counter'] = 1
  return render(request, 'random_app/index.html', unique_word)

def random_word(request):
  if request.method == "POST":
    return redirect('random_app:home')

def reset(request):
  request.session.clear()
  return redirect('random_app:home')