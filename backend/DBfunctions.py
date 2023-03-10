import os
import psycopg2
from get_user_lang import get_user_languages #used in new_user()
from compare_langs import compare_languages

# Create a cursor.
# pg_conn_string = os.environ["PG_CONN_STRING"]
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
    print("=="*15)
    print("tables...\t", end='')
    cursor.execute("SHOW TABLES")
    print(cursor.fetchall())

    print("Contents of users:\t", end='')
    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())

    print("Contents of matches:\t", end='')
    cursor.execute("SELECT * FROM matches")
    print(cursor.fetchall())


#Add new user in 'user' table
def new_user(username, fullname, password):
    #Required: username is git username
    #primary key on username
    #retrieve this user's used language through api.github.com --> str
    languages = get_user_languages(username)

    #insert user into table 'users'
    cursor.execute("INSERT INTO users VALUES (%s, %s, %s, %s)", (username, fullname, password, languages))

    #find every valid match currently in db and insert them and new user as a pair into table 'matches'
    cursor.execute("SELECT username, languages FROM users WHERE username!=%s",(username,))
    potentialMatches = cursor.fetchall()
    for partner in potentialMatches:
        if compare_languages(languages, partner[1]):
            new_match(username, partner[0])

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


#delete a SINGLE match from table 'matches'
def delete_match(username1, username2):
    cursor.execute("DELETE FROM matches WHERE username1=%s AND username2=%s", (username1, username2))
    connection.commit()

#get a list of all matches that include this user 'username'
def get_matches(username) -> list:
    cursor.execute("SELECT * FROM matches WHERE username1=%s OR username2=%s", (username,))
    return cursor.fetchall()


#removes a user from database completely. Removes all instances from tables 'users' and 'matches'
def delete_user_completely(username):
    cursor.execute("DELETE FROM users WHERE username=%s", (username,))
    cursor.execute("DELETE FROM matches WHERE username1=%s OR username2=%s", (username, username))
    connection.commit()
