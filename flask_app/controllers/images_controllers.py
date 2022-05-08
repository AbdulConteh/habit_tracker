import os
from flask_app import app
import urllib.request
from werkzeug.utils import secure_filename
from flask import redirect, render_template, request, url_for, flash

UPLOAD_FOLDER = r'projects\habit_tracker\flask_app\static\uploads'

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload_img', methods=['POST'])
def uploadImage():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print('upload_img:' + filename)
        flash('Image successfully uploaded')
        return redirect('/profile', filename = filename)
    else:
        flash('Image type not allowed')
        return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
    print('display_image filename:' + filename)
    return redirect(url_for('static', filename='uploads' + filename), code=301)