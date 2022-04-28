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

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        users = []
        results = connectToMySQL(db).query_db(query)
        for user in results:
            users.append(cls (user))
        return users

    @classmethod
    def get_account(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(db).query_db(query, data)
        if len(results) < 1:
            return False
        return User(results[0])

    @classmethod
    def get_user(cls, data):
        query = " SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @staticmethod
    def validate_users(User):
        specialSym = ["$", "/", "@", "%"]
        is_valid = True
        if len(User['first_name']) < 3:
            flash('Name must be at least 3 characters. Please try again!', 'register')
            is_valid = False
        if len(User['last_name']) < 3:
            flash('Name must be at least 3 characters. Please try again!', 'register')
            is_valid = False
        if not EMAIL_REGEX.match(User['email']):
            flash('Email must not be registered. Please try again!', 'register')
            is_valid = False
        if len(User['password']) < 6:
            flash('Password must be over 6 characters. Please try again!', 'register')
        if not any(char.isdigit() for char in User['password']):
            flash('Password must have at least 1 number. Please try again!', 'register')
            is_valid = False
        if not any(char in specialSym for char in User['password']):
            flash('Password should have at least one of the symbols: $, /, @, %', 'register')
            is_valid = False
        if User["password"] != User["confirm_password"]:
            flash("Password don't match. Please try again", "login")
            is_valid = False
        return is_valid

