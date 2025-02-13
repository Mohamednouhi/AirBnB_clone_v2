#!/usr/bin/python3

"""flask web app"""

from flask import Flask

app = Flask(__name__)
app.config['STRICT_SLASHES'] = False

@app.route('/')
def hello_world():
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    return "HBNB"

@app.route('/c/<text>')
def c(text):
    text = text.replace('_', ' ')
    return f"C {text}"

@app.route('/python/<text>')
@app.route('/python/')
def python(text="is_cool"):
    text = text.replace('_', ' ')
    return f"Python {text}"

@app.route('/number/<int:n>')
def number(n):
    return f"{n} is a number"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

