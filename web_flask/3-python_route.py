#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """function that displays hello hbnb!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_func(text):
    """displays C"""
    return f'C {escape(text.replace("_", " "))}'


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python_func(text="is cool"):
    """displays python"""
    return f'Python {escape(text.replace("_", " "))}'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
