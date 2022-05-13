from flask_app import app
from flask_bcrypt import Bcrypt 

from flask_app.models.users_models import User
from flask_app.models.habits_models import Habit
from flask_app.models.messages_models import Message
from flask import render_template, redirect, session , flash, request
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('/home.html')

@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id" : session["user_id"]
    }
    # print(data)
    user = User.get_user(data)
    habits = Habit.get_user_habits(data)
    users = User.get_all()
    messages = Message.get_user_message(data)
    # print("**********habit", habits)
    return render_template('/profile.html', user = user, habits = habits, users=users, messages = messages)

@app.route("/user_register", methods=['POST'])
def create():
    if not User.validate_users(request.form):
        return redirect('/')
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : bcrypt.generate_password_hash(request.form['password'])
    }
    # print(data['password'])
    id = User.create_user(data)
    session['user_id'] = id
    return redirect ('/')

@app.route("/login", methods=['POST'])
def login():
    data = {
        "email" : request.form["email"]
    }
    user = User.get_account(data)
    if not user:
        flash("Unregistered email. Please try again", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid password.", "login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect ('/profile')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')