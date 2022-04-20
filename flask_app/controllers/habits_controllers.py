from flask_app import app
from flask import render_template, redirect, session , flash

@app.route('/add_habit')
def add():
    return render_template('/add_habit.html')

@app.route('/edit_habit')
def edit():
    return render_template('/edit_habit.html')

@app.route('/info')
def info():
    return render_template('/info_page.html')