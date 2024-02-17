#!/usr/bin/python3
"""a flask web application that listens on port 0.0.0.0, and displays "Hello HBNB!"""""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """this function handles the route '/' """
    return "Hello HBNB!"


if __name__ == '__main__':
    """
    Main function to run the Flask web application.
    """
    app.run(host='0.0.0.0', port=5000)

