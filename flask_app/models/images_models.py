from flask_app.config.mysqlconnection import MySQLConnection
db = "habit_tracker_db"

class Images:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']