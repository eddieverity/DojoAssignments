from django.shortcuts import render, redirect
import random
import datetime
from django.utils.timezone import utc

# Create your views here.
def index(request):
  if 'gold' not in request.session:

    request.session['gold']=0
    request.session['trip_history']=[]

  return render(request, 'golds/index.html')

def process_money(request):
  if request.method=="POST":
    place=request.POST['building']
    now=str(datetime.datetime.utcnow())

    if place == 'farm':

      win=random.randrange(10,21)
      request.session['gold']+=win
      history=request.session['trip_history']
      history.insert(0,'Earned '+str(win)+' gold from the farm!  ' + now + '\n')
      request.session['trip_history']=history
      return redirect('/')

    if place == 'cave':

      win=random.randrange(5,11)
      request.session['gold']+=win
      history=request.session['trip_history']
      history.insert(0,'Earned '+str(win)+' gold from the cave!  ' + now + '\n')
      request.session['trip_history']=history
      return redirect('/')

    
    if place == 'house':

      win=random.randrange(2,6)
      request.session['gold']+=win
      history=request.session['trip_history']
      history.insert(0,'Earned '+str(win)+' gold from the house!  ' + now + '\n')
      request.session['trip_history']=history
      return redirect('/')

    if place =='casino':

      winlose=random.randrange(0,2)
      if winlose == 1:
        win=random.randrange(0,51)
        request.session['gold']+=win
        history=request.session['trip_history']
        history.insert(0,'Earned '+str(win)+' gold from the casino!  ' + now + '\n')
        request.session['trip_history']=history
        return redirect('/')

      else:
        win=random.randrange(0,51)
        request.session['gold']-=win

        history=request.session['trip_history']
        history.insert(0,'Lost '+str(win)+' gold from the casino!  ' + now + '\n')
        request.session['trip_history']=history

   
        return redirect('/')

def reset(request):
  request.session.clear()
  return redirect('/')
