#!/usr/bin/python3
"""
This module contains a Flask web application.

The web application listens on 0.0.0.0, port 5000 and has the following routes:
- '/': displays "Hello HBNB!"
"""

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """
    This function handles the route '/' and returns "Hello HBNB!".
    """
    return "Hello HBNB!"

if __name__ == '__main__':
    """
    Main function to run the Flask web application.
    """
    app.run(host='0.0.0.0', port=5000)

