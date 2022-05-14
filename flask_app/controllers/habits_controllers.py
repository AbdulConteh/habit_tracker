from flask_app import app
from flask_app.models.habits_models import Habit
from flask_app.models.users_models import User
import os
from flask import render_template, request, redirect, session , flash
# from projects.habit_tracker.server import FLASK_APP_API_KEY

# print(os.environ.get(FLASK_APP_API_KEY) )

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

@app.route('/update_habit/<int:id>', methods=['POST'])
def update_habit(id):
    data = {
        "habit_name" : request.form['habit_name'],
        "goal" : request.form['goal'],
        "habit_type" : request.form['habit_type'],
        "start_date" : request.form['start_date'],
        "frequency" : request.form['frequency'], 
        "id" : id
    }
    Habit.edit_habit(data)
    print("**********", session['user_id'])
    print(data)
    return redirect('/add_habit')

@app.route('/edit_habit/<int:id>')
def edit(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id" : session["user_id"]
    }
    user = User.get_user(data)
    habits = Habit.get_user_habits(data)
    # print("**********", habits)
    for x in habits:
        # print("**********habit.id", x.id)
        # print("**********id", id)
        # print("**********", x.habit_name)
        if x.id == id:
            habit = x
            # print("**********habit", habit)
    return render_template('/edit_habit.html', user = user, habit = habit)

@app.route('/info')
def info():
    user = User.get_all()
    return render_template('/info_page.html', user = user)

@app.route('/add_habit')
def addHabit():
    if 'user_id' not in session:
        return redirect('/')
    show_habits = Habit.show_all_habits()
    data = {
        "id" : session["user_id"]
    }
    user = User.get_user(data)
    return render_template('/add_habit.html', show_habits = show_habits, user = user)

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        "id" : id
    }
    Habit.delete(data)
    return redirect('/add_habit')