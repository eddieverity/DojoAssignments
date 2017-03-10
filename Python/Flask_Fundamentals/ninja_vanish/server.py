from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 

@app.route('/')
def index():
  session['msg']="No ninjas"
  session['img']=""
  print session['msg']
  return render_template("index.html")

@app.route('/ninja')
def blue():
  session['msg']=""
  session['img']="/static/img/tmnt.png"
  return render_template("index.html")

@app.route('/ninja/<color>')
def handler_function(color):
  session['msg']=""
  if color == 'blue':
    session['img']="/static/img/leonardo.jpg"
    return render_template("index.html")
  if color== 'red':
    session['img']="/static/img/raphael.jpg"
    return render_template("index.html")
  if color== 'orange':
    session['img']="/static/img/michelangelo.jpg"
    return render_template("index.html")
  if color== 'purple':
    session['img']="/static/img/donatello.jpg"
    return render_template("index.html")
  else:
    session['img']="/static/img/notapril.jpg"
    return render_template("index.html")

app.run(debug=True)