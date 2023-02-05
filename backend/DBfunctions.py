import os
import psycopg2
import requests #used in new_user()

# Create a cursor.
# pg_conn_string = os.environ["PG_CONN_STRING"]
pg_conn_string = "postgresql://sean:YO33pJN_JINPFMD6k5CIzg@hackroach-4895.6wr.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full"
connection = psycopg2.connect(pg_conn_string)

cursor = connection.cursor()


def set_database():
    cursor.execute("CREATE DATABASE IF NOT EXISTS gitTogether")
    cursor.execute("USE gitTogether")

# Create a table
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

    #TODO: implement fetch langauges for username
    #call to api.github
    url = f"https://api.github.com/{username}"
    response = requests.request("GET", url, data=payload)
    # --> languages
    languages = "Python C Go"
    cursor.execute(
        "INSERT INTO users VALUES (%s, %s, %s, %s)", (username, fullname, password, languages)
    )
    connection.commit()

def get_user_by_username(username):
    cursor.execute("SELECT * FROM users WHERE username = %s ", (username, ))
    return cursor.fetchone()

# Insert data into a table.
def insert_data():
    cursor.execute(
        "INSERT INTO courses VALUES (default, 'Distributed Systems', 'ece', 454, 1.5)"
    )
    cursor.execute(
        "INSERT INTO courses (name, program, code) VALUES ('Databases', 'cs', 348)"
    )
    cursor.execute(
        "INSERT INTO courses (name, program, code, credits) VALUES ('Programming for Performance', 'ece', 459, 1)"
    )
    connection.commit()

# Update data in a table.
def update_rows():
    cursor.execute("UPDATE courses SET program = 'ECE' where program = 'ece'")
    cursor.execute("UPDATE courses SET program = 'CS' where program = 'cs'")
    connection.commit()

# Delete rows.
def delete_rows():
    cursor.execute("DELETE FROM courses WHERE code = 459")
    connection.commit()

def alter_table():
    cursor.execute("ALTER TABLE courses DROP COLUMN credits")
    connection.commit()

    cursor.execute("ALTER TABLE courses ADD COLUMN credits INT DEFAULT 1")
    connection.commit()

# Query a table.
def select_all():
    cursor.execute("SELECT * FROM courses")
    results = cursor.fetchall()
    connection.commit()
    print(results)
    print('\n')

def select_some_with_params():
    cursor.execute("SELECT * FROM courses WHERE program = %s", ('ECE',))
    results = cursor.fetchall()
    connection.commit()
    print(results)
    print('\n')

# Drop table.
def drop_tables():
    cursor.execute("DROP TABLE courses")
    connection.commit()

def add_course_with_params():
    cursor.execute("INSERT INTO courses VALUES (default, %s, %s, %s, %s)",
                   ("Algorithms", "CS", "341", 1))
    connection.commit()

def add_course_with_named_params():
  data = {
    'name': 'Programming for Performance',
    'code': '459',
    'program': 'ECE',
  }
  cursor.execute("INSERT INTO courses VALUES (default, %(name)s, %(program)s, %(code)s)", data)

if __name__=="__main__":
    print("Now running intro_to_psycopg2.py as __main__")
    create_tables()
    
# insert_data()
# update_rows()
# delete_rows()
# alter_table()
# add_course_with_params()
# select_all()
# select_some_with_params()
# drop_tables()
