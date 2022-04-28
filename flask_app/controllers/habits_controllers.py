from flask_app import app
from flask_app.models.habits_models import Habit
from flask_app.models.users_models import User
from flask import render_template, request, redirect, session , flash

@app.route('/create_habit', methods=['POST'])
def createHabit():
    data = {
        "habit_name" : request.form['habit_name'],
        "goal" : request.form['goal'],
        "habit_type" : request.form['habit_type'],
        "start_date" : request.form['start_date'],
        "frequency" : request.form['frequency'], 
        "user_id" : session['user_id']
    }
    Habit.create_habit(data)
    return redirect('/add_habit')

@app.route('/update_habit', methods=['POST'])
def update_habit():
    Habit.edit_habit(request.form)
    return redirect('/add_habit')

@app.route('/edit_habit/<int:id>')
def edit(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id" : id
    }
    user = User.get_all()
    habit = Habit.get_user_habit(data)
    return render_template('/edit_habit.html', user = user, habit = habit)

@app.route('/info')
def info():
    if 'user_id' not in session:
        return redirect('/')
    user = User.get_all()
    return render_template('/info_page.html', user = user)

@app.route('/add_habit')
def addHabit():
    if 'user_id' not in session:
        return redirect('/')
    show_habits = Habit.show_all_habits()
    return render_template('/add_habit.html', show_habits = show_habits)

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        "id" : id
    }
    Habit.delete(data)
    return redirect('/add_habit')