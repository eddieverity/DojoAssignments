from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 
def sumSessionCounter():
  try:
    session['counter'] += 1
  except KeyError:
    session['counter'] = 1

@app.route('/')
def index():
    sumSessionCounter()
    return render_template('index.html')



@app.route('/ninja', methods=['POST'])
def ninja():
  session['counter'] +=1
  return redirect('/')

@app.route('/hacker', methods=['POST'])
def hacker():
  session['counter'] =0
  return redirect('/')


app.run(debug=True)