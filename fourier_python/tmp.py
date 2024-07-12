from sympy import symbols, pi, fourier_series
import numpy as np
import matplotlib.pyplot as plt

# Define the variable and the function
x = symbols('x')
func = x**2

# Generate the Fourier series
fs = fourier_series(func, (x, -pi, pi))

# Calculate the series coefficients
coeffs = [fs.coeff(k) for k in range(0, 11)]

# Create an array of points
x_values = np.linspace(-pi, pi, 1000)

# Initialize the sum of terms
sum_terms = 0

# Sum the terms of the Fourier series
for k in range(0, 11):
    sum_terms += coeffs[k] * np.cos(2 * pi * k * x_values)

# Plot the Fourier series
plt.plot(x_values, sum_terms, label='Fourier series')
plt.plot(x_values, func.subs(x, x_values), label='Original function')
plt.legend()
plt.show()