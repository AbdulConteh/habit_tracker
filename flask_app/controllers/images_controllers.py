from flask_app import app
from flask import redirect, render_template

@app.route('/upload_img', methods=['POST'])
def uploadImage():
    pass