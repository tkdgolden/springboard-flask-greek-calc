# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def adding():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)
    return str(result)
    
    
@app.route('/sub')
def subing():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = sub(a, b)
    return f"{result}"

@app.route('/mult')
def multing():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = mult(a, b)
    return f"{result}"

@app.route('/div')
def diving():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = div(a, b)
    return f"{result}"

@app.route('/math/<function>')
def math_function(function):
    function = function
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = "error"
    match function:
        case "add":
            result = add(a, b)
        case "sub":
            result = sub(a, b)
        case "mult":
            result = mult(a, b)
        case "div":
            result = div(a, b)
    return f"{result}"
        