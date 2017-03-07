from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 
@app.route('/')
def index():
  return render_template("index.html")
@app.route('/results', methods=["POST", "GET"])
def create_user():
  print "Got Post Info"
  session['name'] = request.form["name"]
  session['location'] = request.form["location"]
  session['language'] = request.form["language"]
  session['comments'] = request.form["comments"]

  return render_template('results.html', name = session["name"], location = session["location"], language = session["language"], comments = session["comments"])

app.run(debug=True)