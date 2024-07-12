from flask import Flask, render_template, request
from sympy import symbols, Piecewise, fourier_series, plot
from sympy.abc import x
from sympy import pi, sin, cos
import os
import matplotlib.pyplot as plt
from sympy import *
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    n = int(request.form['no_of_terms'])
    k = int(request.form['no_of_cycles'])
    L = int(request.form['interval_start'])
    R = int(request.form['interval_end'])

    # Extract the user-input periodic function
    user_input_function = request.form['input_periodic_function']

    # Use sympify to convert the user-input string to a symbolic expression
    function = sympify(user_input_function)

    #function = -(5/pi)* x + 5
    #function = Piecewise((-1, x < 0),(1, x > 0))

    ser = fourier_series(function, (x, L* pi, R * pi))
    p = plot(ser.truncate(n), (x, k * -pi, k * pi), show=False)

    expr = ser.truncate(n)
    # Convert the expression to a list of terms
    term_list = expr.as_ordered_terms()
        
    image_path = 'static/plot.png'  # Save the image to the 'static' folder
    p.save(image_path)
    
    return render_template('index.html', plot_image=image_path, term_list=term_list)

if __name__ == '__main__':
    app.run(debug=True)
