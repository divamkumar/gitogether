from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


current_user_fullname_db = "Divam Kumar"
current_user_username_db = "divamkumar"
current_user_password_db = "asdf"

curfullname = None
curusername = None
curpassword = None


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
    # return request.form['username'] + " " + request.form['password']
    # if request.form['username'] != current_user_username_db:
    #     if request.form['password'] != current_user_password_db:
    #         return 200
    #     return 401
    # else:
    #     return 401 
    return "200"
        

@app.route('/signup', methods=['POST'])
def signup():
    # return request.form['fullname'] + ' ' + request.form['username'] + " " + request.form['password']
    return "201"

@app.route('/getuser', methods=['GET'])
def get_user():
    pass

@app.route('/judgeuser', methods=['POST'])
def judgeuser():
    pass