# Put your app in here.
from flask import Flask, request
from operations import *


app = Flask(__name__)


@app.route("/add")
def add_view():
    """View that show sums of query paramaters a and b."""
    a = request.args.get("a")
    b = request.args.get("b")
    if not a and b:
        return "Must provide a and b in query parameters."
    return str(add(int(a), int(b)))


@app.route("/sub")
def sub_view():
    """View that shows differene of query paramaters a and b."""
    a = request.args.get("a")
    b = request.args.get("b")
    if not a and b:
        return "Must provide a and b in query parameters."
    return str(sub(int(a), int(b)))


@app.route("/mult")
def mult_view():
    """View that shows product of query paramaters a and b."""
    a = request.args.get("a")
    b = request.args.get("b")
    if not a and b:
        return "Must provide a and b in query parameters."
    return str(mult(int(a), int(b)))


@app.route("/div")
def div_view():
    """View that shows quotient of query paramaters a and b."""
    a = request.args.get("a")
    b = request.args.get("b")
    if not a and b:
        return "Must provide a and b in query parameters."
    return str(div(int(a), int(b)))


@app.route("/math/<op>")
def all_in_one(op):
    """View that uses op variable to determine operation on a and b."""
    dic = {"add": add, "sub": sub, "mult": mult, "div": div}

    if not op in dic:
        return "404"

    a = request.args.get("a")
    b = request.args.get("b")
    if not a and b:
        return "Must provide a and b in query parameters."

    return str(dic[op](int(a), int(b)))

    # if op == 'add':
    #     return str(add(int(a), int(b)))
    # if op == 'sub':
    #     return str(sub(int(a), int(b)))
    # if op == 'mult':
    #     return str(mult(int(a), int(b)))
    # if op == 'div':
    #     return str(div(int(a), int(b)))
