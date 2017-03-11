from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 

@app.route('/')
def index():
  msg="No ninjas"
  img=""
  print msg
  return render_template("index.html", img=img, msg=msg)

@app.route('/ninja')
def blue():
  msg=""
  img="/static/img/tmnt.png"
  return render_template("index.html", msg=msg, img=img)

@app.route('/ninja/<color>')
def handler_function(color):
  msg=""
  if color == 'blue':
    img="/static/img/leonardo.jpg"
    return render_template("index.html", img=img, msg=msg)
  if color== 'red':
    img="/static/img/raphael.jpg"
    return render_template("index.html", img=img, msg=msg)
  if color== 'orange':
    img="/static/img/michelangelo.jpg"
    return render_template("index.html", img=img, msg=msg)
  if color== 'purple':
    img="/static/img/donatello.jpg"
    return render_template("index.html", img=img, msg=msg)
  else:
    img="/static/img/notapril.jpg"
    return render_template("index.html", img=img, msg=msg )

app.run(debug=True)