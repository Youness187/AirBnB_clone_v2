#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask
from flask import render_template

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


@app.route("/python/<path:subpath>")
@app.route("/python/")
def python_is_cool(subpath="is cool", strict_slashes=False):
    """Python is cool"""
    return "Python {}".format(subpath.replace("_", " "))


@app.route("/number/<int:number>")
def number(number, strict_slashes=False):
    """Is it a number"""
    return "{} is a number".format(number)


@app.route("/number_template/<int:number>")
def number_template(number, strict_slashes=False):
    """Number template"""
    return render_template("5-number.html", number=number)


@app.route("/number_odd_or_even/<int:number>")
def number_odd_or_even(number, strict_slashes=False):
    """Number odd or even"""
    return render_template("6-number_odd_or_even.html", number=number)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
