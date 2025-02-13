#!/usr/bin/python3

"""flask web app with a lot of routes"""
from flask import Flask, render_template
app = Flask(__name__)
app.config['STRICT_SLASHES']=False

@app.route('/')
def hello_world():
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    return "HBNB"

@app.route('/c/<text>')
def c(text):
    text=text.replace('_', ' ')
    return f"C {text}"

@app.route('/python/')
@app.route('/python/<text>')
def python(text='is cool'):
    text=text.replace('_',' ')
    return f"{text} is cool"

@app.route('/number/<int:n>')
def number(n):
    return f"{n} is a number"

@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=n)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)
