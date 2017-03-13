import re
from datetime import datetime as dt

from flask import Flask, render_template, flash, redirect, request, session
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = "6a204bd89f3c8348afd5c77c717a097a"

mysql = MySQLConnector(app, 'babylon')
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    if 'user_id' in session:
        all_users = mysql.query_db('select * from users')
        return render_template('index.html', all_users = all_users)
    return render_template('index.html')

@app.route('/login')
def login():
    if 'user_id' in session:
        return redirect('/')

    return render_template('login.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    email = request.form['html_email']
    password = request.form['html_password']

    # 1) query the database (get the user)
    parameters = {}
    parameters['email'] = email
    users = mysql.query_db('select * from users where email = :email', parameters)
    if len(users) == 1:
        user = users[0]
        # 2) compare values from the database with values from the form    
        if user['password'] == password:
            # 3) update the session
            setup_session(user['id'], user['last_name'], user['email'])
            return redirect('/')
    
    flash('invalid login')
    return redirect('/login')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    is_valid = True

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['html_email']
    password = request.form['html_password']
    confirm = request.form['html_confirm']

    if len(first_name) < 3:
        flash('name must be at least 3 characters long')
        is_valid = False
    if len(last_name) < 3:
        flash('name must be at least 3 characters long')
        is_valid = False
    if email_regex.search(email) is None:
        flash('inavlid email address')
        is_valid = False
    if len(password) < 8:
        flash('password must be at least 8 characters long')
        is_valid = False
    if password != confirm:
        flash('passwords do not match')
        is_valid = False
        
    if is_valid:
        parameters = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password,
            'created_at': dt.now()
        }

        create_user_sql = 'insert into users (first_name, last_name, email, password, created_at) values (:first_name, :last_name, :email, :password, :created_at)'
        user_id = mysql.query_db(create_user_sql, parameters)
        setup_session(user_id, last_name, email)
        
        return redirect('/')
    else:
        return redirect('/login')

    
def setup_session(user_id, last_name, email):
    session['user_id'] = user_id
    session['last_name'] = last_name
    session['email'] = email

app.run(debug=True)