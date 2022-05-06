from flask_app import app
from flask_app.controllers import users_controllers
from flask_app.controllers import habits_controllers
from flask_app.controllers import messages_controllers
from dotenv import load_dotenv

load_dotenv() 

if __name__=="__main__":
    app.run(debug=True)