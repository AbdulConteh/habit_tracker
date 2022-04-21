import re
from flask import flash
from flask_app import app 
from flask_app.config.mysqlconnection import connectToMySQL
db = "habit_tracker_db"

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def create_user(cls, data):
        query = """
        INSERT INTO users ( "first_name", "last_name", "email", "password")
        VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s)
        """
        result = connectToMySQL(db).query_db(query, data)
        return result 

