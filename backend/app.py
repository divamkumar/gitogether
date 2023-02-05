from flask import Flask
import json
from flask import request
from flask_cors import CORS
import psycopg2
from get_user_lang import get_user_languages #used in new_user()

# Create a cursor.
pg_conn_string = "postgresql://sean:YO33pJN_JINPFMD6k5CIzg@hackroach-4895.6wr.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full"
connection = psycopg2.connect(pg_conn_string)

cursor = connection.cursor()


# Create and 'use' database
def set_database():
    cursor.execute("CREATE DATABASE IF NOT EXISTS gitTogether")
    cursor.execute("USE gitTogether")


# Create tables for gitTogether
def create_tables():
    cursor.execute("CREATE TABLE IF NOT EXISTS users ( \
    username STRING PRIMARY KEY, \
    fullName STRING NOT NULL,\
    password STRING NOT NULL,\
    languages STRING\
    )")

    cursor.execute("CREATE TABLE IF NOT EXISTS matches ( \
    username1 STRING NOT NULL, \
    username2 STRING NOT NULL, \
    PRIMARY KEY(username1, username2) \
    )")
    connection.commit()


#prints all tables in database
def print_database_logistics():
    print("tables...\t", end='')
    cursor.execute("SHOW TABLES")
    print(cursor.fetchall())

    print("Contents of users:\t", end='')
    cursor.execute("SELECT * FROM users")
    print(cursor.fetchone())

    print("Contents of matches:\t", end='')
    cursor.execute("SELECT * FROM matches")
    print(cursor.fetchone())


#Add new user in 'user' table
def new_user(username, fullname, password):
    #Required: username is git username
    #primary key on username
    #retrieve this user's used language through api.github.com --> str
    languages = get_user_languages(username)

    cursor.execute(
        "INSERT INTO users VALUES (%s, %s, %s, %s)", (username, fullname, password, languages)
    )
    connection.commit()


#Remove user from the 'user' table
def delete_user(username):
    cursor.execute("DELETE FROM users WHERE username=%s", (username,))
    connection.commit()


def get_user_by_username(username) -> tuple:
    cursor.execute("SELECT * FROM users WHERE username = %s ", (username, ))
    return cursor.fetchone()


#insert a new match pairing into table 'matches'
def new_match(username1, username2):
    cursor.execute("INSERT INTO matches VALUES (%s, %s)", (username1, username2))
    connection.commit()


def delete_match(username1, username2):
    cursor.execute("DELETE FROM matches WHERE username1=%s AND username2=%s", (username1, username2))
    connection.commit()

#get a list of all matches that include this user 'username'
def get_matches(username) -> list:
    cursor.execute("SELECT * FROM matches WHERE username1=%s OR username2=%s", (username,))
    return cursor.fetchall()



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
    return request.form['fullname'] + ' ' + request.form['username'] + " " + request.form['password']
