import re
from flask import flash
from flask_app import app 
from flask_app.config.mysqlconnection import connectToMySQL
db = "habit_tracker_db"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_user(cls, data):
        query = """
        INSERT INTO users(first_name,last_name,email,password)
        VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s)
        """
        results = connectToMySQL(db).query_db(query, data)
        return results

    @staticmethod
    def validate_users(User):
        specialSym = ["$", "/", "@", "%"]
        val = True
        if len(User['first_name']) < 3:
            flash('Name must be at least 3 characters. Please try again!')
            is_valid = False
        if len(User['last_name']) < 3:
            flash('Name must be at least 3 characters. Please try again!')
            is_valid = False
        if not EMAIL_REGEX.match(User['email']):
            flash('Email must not be registered. Please try again!')
            is_valid = False
        if len(User['password']) < 6:
            flash('Password must be over 6 characters. Please try again!')
        if not any(char.isdigit() for char in User['password']):
            flash('Password must have at least 1 number. Please try again!')
            is_valid = False
        if not any(char in specialSym for char in User['password']):
            flash('Password should have at least one of the symbols: $, /, @, %')
            is_valid = False
        return is_valid

