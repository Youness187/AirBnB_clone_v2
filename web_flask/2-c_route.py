#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello(strict_slashes=False):
    """Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb(strict_slashes=False):
    """HBNB"""
    return "HBNB"


@app.route("/c/<path:subpath>")
def c_is_fun(subpath, strict_slashes=False):
    """C is fun"""
    return "C {}".format(subpath.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
