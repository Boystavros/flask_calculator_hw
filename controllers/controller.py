from flask import render_template
from app import app
from modules.calculator import add, divide, multiply, subtract


@app.route('/<operation>/<str_1>/<str_2>')
def index(operation, str_1, str_2):
    num_1 = int(str_1)
    num_2 = int(str_2)
    if  operation == 'add':
        result = add(num_1, num_2)
    elif operation == 'subtract':
        result = subtract(num_1, num_2)
    elif operation == 'multiply':
        result = multiply(num_1, num_2)
    elif operation == 'divide':
        result = divide(num_1, num_2)
    else:
        result = "not available"
    return render_template('index.html', output=result)

