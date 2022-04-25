from flask_app import app
from flask_app.models.habits_models import Habit
from flask import render_template, request, redirect, session , flash

@app.route('/create_habit', methods=['POST'])
def createHabit():
    data = {
        "habit" : request.form['habit'],
        "goal" : request.form['goal'],
        "habit_type" : request.form['habit_type'],
        "start_date" : request.form['start_date'],
        "frequency" : request.form['frequency']
    }
    Habit.create_habit(data)
    return redirect('/add_habit')

@app.route('/edit_habit')
def edit():
    return render_template('/edit_habit.html')

@app.route('/info')
def info():
    return render_template('/info_page.html')

@app.route('/add_habit')
def addHabit():
    show = Habit.show_habit)

    return render_template('/add_habit.html', 