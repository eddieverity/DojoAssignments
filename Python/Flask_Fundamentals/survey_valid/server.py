from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 

@app.route('/')
def index():
  return render_template("index.html")


@app.route('/process', methods=["POST"])
def validate():
  session['name'] = request.form["name"]
  session['location'] = request.form["location"]
  session['language'] = request.form["language"]
  session['comments'] = request.form["comments"]
  if len(request.form['name']) < 1 or len(request.form['comments']) < 1 or len(request.form['comments']) > 120:
    print "lengths not correct"
    flash("Please fill out all fields and keep comments less than 120 characters")
    return redirect('/')
  return render_template('results.html', name = session["name"], location = session["location"], language = session["language"], comments = session["comments"])

app.run(debug=True)