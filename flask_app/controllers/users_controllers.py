from flask_app import app
from flask_bcrypt import Bcrypt 
from flask_app.models.users_models import User
from flask import render_template, redirect, session , flash, request
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('/home.html')

@app.route('/profile')
def profile():
    return render_template('/profile.html')

@app.route("/user_register", methods=['POST'])
def create():
    # if not User.validate_user(request.form):
    #     return redirect('/')
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : bcrypt.generate_password_hash(request.form['password']),
        "confirm_password" : request.form["confirm_password"]
    }
    print(data['password'])
    id = User.create_user('data')
    session['users_id'] = id
    return redirect ('/')
