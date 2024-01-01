#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, escape, abort, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """displays a html page"""
    try:
        states = sorted(storage.all(State).values(), key=lambda s: s.name)
        return render_template("7-states_list.html", states=states)
    except ValueError:
        abort(404)


@app.teardown_appcontext
def teardown(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
