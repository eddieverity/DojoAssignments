from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")
@app.route('/results', methods=["POST", "GET"])
def create_user():
  print "Got Post Info"
  name = request.form["name"]
  location = request.form["location"]
  language = request.form["language"]
  comments = request.form["comments"]

  return render_template('results.html', name = name, location = location, language = language, comments = comments)

app.run(debug=True)