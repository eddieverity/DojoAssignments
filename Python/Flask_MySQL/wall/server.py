import re
from datetime import datetime as dt

from flask import Flask, render_template, flash, redirect, request, session
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = "6a204bd89f3c8348afd5c77c717a097a"

mysql = MySQLConnector(app, 'wall')
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    if 'user_id' in session:
        all_users = mysql.query_db('select * from users')
        all_messages = mysql.query_db('select * from messages')
        all_comments = mysql.query_db('select * from comments')

        return render_template('wall.html', all_users=all_users, all_comments=all_comments, all_messages=all_messages)
    return render_template('login.html')

@app.route('/login')
def login():
    if 'user_id' in session:
        return redirect('/wall')
    return render_template('login.html')

@app.route('/message', methods=['POST'])
def message():
    message=request.form['message']
    user_id=session['user_id']

    query = "INSERT INTO messages (message, user_id, created_at, updated_at) VALUES (:message, :user_id, NOW(), NOW())"

    data = {
        'message': request.form['message'], 
        'user_id':  session['user_id']
    }

    mysql.query_db(query, data)
    return redirect('/')

@app.route('/comment', methods=['POST', 'GET'])
def comment():

    comment=request.form['comment']
    user_id=session['user_id']
    message_id = request.form['message_id']

    query = "INSERT INTO comments (comment, user_id, message_id, created_at, updated_at) VALUES (:comment, :user_id, :message_id, NOW(), NOW())"

    data = {
        'comment': request.form['comment'], 
        'user_id':  session['user_id'],
        'message_id': request.form['message_id']
    }

    mysql.query_db(query, data)
    return redirect('/')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    email = request.form['html_email']
    password = request.form['html_password']

    parameters = {}
    parameters['email'] = email
    users = mysql.query_db('select * from users where email = :email', parameters)
    if len(users) == 1:
        user = users[0]
 
        if user['password'] == password:
            setup_session(user['id'], user['first_name'], user['email'])
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

    if len(first_name) < 2:
        flash('First name must be at least 2 characters long!')
        is_valid = False
    if len(last_name) < 2:
        flash('Last name must be at least 2 characters long!')
        is_valid = False
    if email_regex.search(email) is None:
        flash('Invalid email address!')
        is_valid = False
    if len(password) < 8:
        flash('Passwords must be at least 8 characters long!')
        is_valid = False
    if password != confirm:
        flash('Confirm password does not match')
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
    
def setup_session(user_id, first_name, email):
    session['user_id'] = user_id
    session['first_name'] = first_name
    session['email'] = email

app.run(debug=True)







