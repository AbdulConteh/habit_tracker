from flask_app import app
from flask import render_template, redirect, session , flash

@app.route('/')
def index():
    return render_template('/home.html')

@app.route('/profile')
def profile():
    return render_template('/profile.html')

@app.route('/user_register', method=['POST'])
def registration():
    pass
