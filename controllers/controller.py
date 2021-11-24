from flask import render_template
from app import app
from modules.calculator import add


@app.route('/add/<str_1>/<str_2>')
def index(str_1, str_2):
    num_1 = int(str_1)
    num_2 = int(str_2)
    result = add(num_1, num_2)
    return render_template('index.html', output=result)