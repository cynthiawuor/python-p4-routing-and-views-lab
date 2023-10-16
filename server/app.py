#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:input_string>')
def print_string(input_string):
    print(input_string)  # Print to the console
    return input_string  # Display in the web browser

@app.route('/count/<int:num>')
def count(num):
    numbers = "\n\n".join(map(str, range(num)))  # Add an extra line break
    return numbers

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation"

    return f"{num1} {operation} {num2} = {result}"

if __name__ == '__main__':
    app.run(debug=True)
