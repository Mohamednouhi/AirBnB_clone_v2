#!/usr/bin/python3

"""flask web application that has 3 routes"""
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_world():
    """displays  “Hello HBNB!” """
    return "“Hello HBNB!”"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays hbnb"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """displays c and the text we gave it"""
    text_variable = text.replace('_', ' ')
    return f"C {text_variable}"

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)

