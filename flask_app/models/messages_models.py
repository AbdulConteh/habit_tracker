import re
from flask import flash
from flask_app import app 
from flask_app.config.mysqlconnection import connectToMySQL
db = "habit_tracker_db"

class Message:
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sender_id = data['sender_id']
        self.receiver_id = data['receiver_id']

    def create_habit(self, data):
        query = """
        INSERT INTO messages ( 'habit_name', 'goal', 'habit_type', 'start_date', 'frequency', 'user_id')
        VALUES(%(habit_name)s, %(goal)s, %(habit_type)s, %(start_date)s, %(frequency)s, %(user_id)s);
        """
        results = connectToMySQL(db).query_db(query, data)
        return results 