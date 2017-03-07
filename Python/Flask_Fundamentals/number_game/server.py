from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 



def randomNumber():
  session['current_random']=random.randrange(1,101)

@app.route('/')
def index():
  randomNumber()
  print session['current_random']
  return render_template('index.html')



@app.route('/guess', methods=['POST'])
def guess():
  session['guessed_num'] = request.form["guess"]
  if int(session['guessed_num']) > session['current_random']:
    return render_template('toohigh.html')
  elif int(session['guessed_num']) < session['current_random']:
    return render_template('toolow.html')
  else:
    session.pop('current_random')
    randomNumber()
    print session['current_random']
    return render_template('youwin.html')

@app.route('/reset', methods=['POST'])
def reset():
  randomNumber()
  return render_template('index.html')
      



app.run(debug=True)