from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 



@app.route('/')
def index():

  if 'gold' not in session:

    session['gold']=0
    session['trip_history']=[]
  return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def process_money():


  session['place']=request.form["building"]
  if session['place']=='farm':
    win=random.randrange(10,21)
    session['gold']+=win
    now = str(datetime.now())
    history=session['trip_history']
    history.insert(0,'Earned '+str(win)+' gold from the farm!' + now + '\n')
    session['trip_history']=history



    return redirect('/')
  elif session['place']=='cave':
    win=random.randrange(5,11)
    session['gold']+=win
    now = str(datetime.now())
    history=session['trip_history']
    history.insert(0,'Earned '+str(win)+' gold from the cave!' + now + '\n')
    session['trip_history']=history

    return redirect('/')
  elif session['place']=='house':
    win=random.randrange(2,6)
    session['gold']+=win
    now = str(datetime.now())
    history=session['trip_history']
    history.insert(0,'Earned '+str(win)+' gold from the house!' + now + '\n')
    session['trip_history']=history
    return redirect('/')
  elif session['place']=='casino':
    winlose=random.randrange(0,2)
    if winlose == 1:
      win=random.randrange(0,51)
      session['gold']+=win
      now = str(datetime.now())
      history=session['trip_history']
      history.insert(0,'Earned '+str(win)+' gold from the casino!' + now + '\n')
      session['trip_history']=history

    else:
      win=random.randrange(0,51)
      session['gold']-=win
      now = str(datetime.now())
      history=session['trip_history']
      history.insert(0,'Lost '+str(win)+' gold from the casino!' + now + '\n')
      session['trip_history']=history

   
    return redirect('/')

@app.route('/reset')
def reset():
  session.clear()
  return redirect('/')





# @app.route('/guess', methods=['POST'])
# def guess():
#   session['guessed_num'] = request.form["guess"]
#   if int(session['guessed_num']) > session['current_random']:
#     return render_template('toohigh.html')
#   elif int(session['guessed_num']) < session['current_random']:
#     return render_template('toolow.html')
#   else:
#     session.pop('current_random')
#     randomNumber()
#     print session['current_random']
#     return render_template('youwin.html')









app.run(debug=True)