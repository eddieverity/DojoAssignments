from flask import Flask, render_template, flash, redirect, request, session
from mysqlconnection import MySQLConnector
from datetime import datetime as dt
import re

app = Flask(__name__)
app.secret_key = "6a204bd89f3c8348afd5c77c717a097a"

mysql = MySQLConnector(app, 'email')
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/auth', methods=['POST'])
def auth():
  email = request.form['email']
  if email_regex.search(email) is None:
    flash('Email is not valid!')
    return redirect('/')
  else:
    session['email']=request.form['email']
    #session variable entered email address
    #update sql database with new email address
    parameters = {
      'email': email,
      'created_at': dt.now()
    }
    create_user_sql = 'insert into email (email, created_at) values (:email, :created_at)'
    user_id = mysql.query_db(create_user_sql, parameters)
    return redirect('/success')

@app.route('/success')
def success():
  #sql query select * users in database
  query= "SELECT * FROM email"
  emails=mysql.query_db(query)
  return render_template('success.html', emails=emails)#, email = session email, db object)

app.run(debug=True)

