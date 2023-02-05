from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


current_user_name = None
current_user_profile = None
current_github_data = None


@app.route('/', methods=['GET', 'POST'])
def opening_page():
    if request.method  == 'GET':
        return '<p>This is a GET request!</p>'
    elif request.method == 'POST':
        return "<p>POST</p>"
    else:
        return '<p>INALID</p>'

@app.route('/signin', methods=['POST'])
def signin():
    return request.form['username'] + " " + request.form['password']

@app.route('/signup', methods=['POST'])
def signup():
    return request.form['fullname'] + ' ' + request.form['username'] + " " + request.form['password']