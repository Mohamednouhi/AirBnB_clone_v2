#!/usr/bin/python3

"""A simple Flask web application with two routes: '/' and '/hbnb'"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_world():
    """displays Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays HBNB"""
    return "HBNB"

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)
