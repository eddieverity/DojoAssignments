from flask import Flask , render_template, redirect, session, flash, request

app = Flask(__name__)
app.secret_key = 'somegreatsecret'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/rabbits')
def rabbits():
  history=session['trip_history']
  history.insert(0,'clicked rabbits')
  session['trip_history']=history
  return render_template('rabbits.html')

@app.route('/hares')
def hares():
  history=session['trip_history']
  history.insert(0,'clicked hares')
  session['trip_history']=history
  return render_template('hares.html')

@app.route('/pica')
def pica():
  history=session['trip_history']
  history.insert(0,'clicked pica')
  session['trip_history']=history
  return render_template('pica.html')

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/auth', methods=['POST'])
def auth():
  server_email=request.form['email']
  server_password=request.form['password']
  if server_email=='abc@abc.com' and server_password=='qwerty':
    session['user_name']='some user'
    session['email']=server_email
    session['trip_history']=[]
    return redirect('/')
  else:
    return redirect('/login')

@app.route('/logout')
def logout():
  session.clear()
  return redirect('/')


app.run(debug=True)