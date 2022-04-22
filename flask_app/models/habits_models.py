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

    def create_habit(self, data):
        query = """
        INSERT INTO habits ( 'habit_name', 'goal', 'habit_type', 'start_date', 'frequency', 'user_id')
        VALUES(%(habit_name)s, %(goal)s, %(habit_type)s, %(start_date)s, %(frequency)s, %(user_id)s);
        """
        results = connectToMySQL(db).query_db(query, data)
        return results 

    def show_habit(self, data):
        query = "SELECT * FROM habits"
        results = connectToMySQL(db).query_db(query, data)
        return results