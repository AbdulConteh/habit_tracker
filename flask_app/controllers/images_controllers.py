import os
import requests 
from flask import jsonify
from flask_app import app
from flask import redirect, session

print( os.environ.get("FLASK_APP_API_KEY") )

@app.route('/upload_img', methods=['POST'])
def uploadImage():
    pass