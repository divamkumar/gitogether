from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

import http.client
def foo():
    conn = http.client.HTTPSConnection("api.github.com")

    payload = ""

    dataGit = conn.request("GET", "/users/divamkumar/repos", payload)

    res = conn.getresponse()
    data = res.read()

    #print(data.decode("utf-8"))
    return dataGit.json()

print(foo())