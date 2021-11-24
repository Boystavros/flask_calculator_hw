from flask import render_template
from app import app
from modules.calculator import *


@app.route('/<operation>/<num_1>/<num_2>')
def index(operation, num_1, num_2):
    #return render_template('index.html', calc_operation=operation, first=num_1, second=num_2)