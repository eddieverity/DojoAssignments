from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 
import re
@app.route('/')
def index():
  return render_template("index.html")


@app.route('/process', methods=["POST"])
def validate():
  session['email'] = request.form["email"]
  session['first_name'] = request.form["first_name"]
  session['last_name'] = request.form["last_name"]
  session['password'] = request.form["password"]
  session['confirm_password'] = request.form["confirm_password"]

  if len(session['email']) < 1 or len(session['first_name']) < 1 or len(session['last_name']) < 1 or len(session['password']) < 1 or len(session['confirm_password']) < 1:
    flash("Please fill out all fields")
    print "fill fields"
    return redirect('/')
  if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", session['email']) :
    flash("Enter a valid email address")
    print "email"
    return redirect('/')




  if ((session['first_name']).isalpha != True) or ((session['first_name']).isalpha != True):
    flash("No numbers or special characters in name fields")
    print "no#"
    return redirect('/')
  if len(session['password']) < 8:
    flash("Password must be greater than 8 characters")
    print "pw small"
    return redirect('/')

  #elif #valid email

  if session['password'] != session['confirm_password']:
    flash("Password & confirm needs to match")
    print "pw != pw"
    return redirect('/')

  
  print "done"
  return redirect('/')

  # if len(request.form['name']) < 1 or len(request.form['comments']) < 1 or len(request.form['comments']) > 120:
  #   print "lengths not correct"
  #   flash("Please fill out all fields and keep comments less than 120 characters")
  #   return redirect('/')
  

app.run(debug=True)