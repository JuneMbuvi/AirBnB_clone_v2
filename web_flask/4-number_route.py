#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, escape, abort


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


@app.route("/number/<n>", strict_slashes=False)
def n_func(n):
    """displays n is a number only if n is an integer"""
    try:
        n = int(n)
        return f'{n} is a number'
    except ValueError:
        abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
