from flask import Flask, render_template, request
from utils import is_even, is_odd, is_prime


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<int:number>')
@app.route('/<int:number>/odd')
@app.route('/<int:number>/even')
@app.route('/<int:number>/prime')
def number_range(number):
    url = request.url_rule.rule
    numbers = range(1, number+1)
    number_type = 'All'
    is_selected_type = lambda num: num

    if 'odd' in url:
        is_selected_type = is_odd
        number_type = 'Odd'
    elif 'even' in url:
        is_selected_type = is_even
        number_type = 'Even'
    elif 'prime' in url:
        is_selected_type = is_prime
        number_type = 'Prime'

    numbers = [num for num in numbers if is_selected_type(num)]

    return render_template('number_display.html', numbers=numbers, number_type=number_type, number=number)