#!/usr/bin/python3
"""flask web app that runs 4 routes"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_world():
    """'displays  Hello HBNB!"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays  HBNB!"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """displays C followed by the text"""
    text_variable = text.replace(' ', '_')
    return f"C {text_variable}"

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """displays Python followed by the text """
    text_variable=text.replace(' ', '_')
    return f"Python {text_variable}"

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)

