from flask import Flask, session

app = Flask(__name__)

app.secret_key = "habits all day"
app.config['MAX_CONTENT_LENGTH'] = 16 *1024 * 1024



