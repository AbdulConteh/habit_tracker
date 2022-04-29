import re
from flask import flash
from flask_app import app 
from flask_app.config.mysqlconnection import connectToMySQL
db = "habit_tracker_db"

class Habit:
    def __init__(self, data):
        self.id = data['id']
        self.habit_name = data['habit_name']
        self.goal = data['goal']
        self.habit_type = data['habit_type']
        self.start_date = data['start_date']
        self.frequency = data['frequency']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_habit(cls, data):
        query = """
        INSERT INTO habits ( habit_name, goal, habit_type, start_date, frequency, user_id)
        VALUES(%(habit_name)s, %(goal)s, %(habit_type)s, %(start_date)s, %(frequency)s, %(user_id)s);
        """
        results = connectToMySQL(db).query_db(query, data)
        return results 

    @classmethod
    def edit_habit(cls, data):
        query = """
        UPDATE habits SET habit_name= %(habit_name)s, goal=%(goal)s, habit_type=%(habit_type)s,start_date=%(start_date)s
        ,frequency=%(frequency)s, updated_at=NOW()
        WHERE id = %(id)s;
        """
        results = connectToMySQL(db).query_db(query, data)
        return results 

    @classmethod
    def show_all_habits(cls):
        query = "SELECT * FROM habits; "
        results = connectToMySQL(db).query_db(query)
        return results

    @classmethod
    def get_user_habits(cls, data):
        query ="SELECT * FROM habits WHERE user_id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        show_habit = []
        for habit in results:
            show_habit.append(cls(habit))
        return show_habit


    @classmethod
    def delete(cls, data):
        query = " DELETE FROM habits WHERE id = %(id)s;"
        result = connectToMySQL(db).query_db(query, data)
        return result