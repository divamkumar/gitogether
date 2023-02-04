from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

import requests
def foo():
    url = "https://api.github.com/users/divankumar/repos"

    payload = ""

    response = requests.request("GET", url, data=payload)

    return response

print(foo())