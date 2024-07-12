import numpy as np
import matplotlib.pyplot as plt

# Define the square wave function
def square_wave(x):
    return np.sign(np.sin(x))

# Set the period and number of harmonics
T = 2 * np.pi
num_harmonics = 10

# Calculate the Fourier coefficients
a0 = 0
an = np.zeros(num_harmonics)
bn = np.zeros(num_harmonics)

# Create the Fourier approximation
x = np.linspace(0, T, 1000)
F = a0 / 2 + np.sum([an[n - 1] * np.cos(2 * np.pi * n * x / T) + bn[n - 1] * np.sin(2 * np.pi * n * x / T) for n in range(1, num_harmonics + 1)], axis=0)


for n in range(1, num_harmonics + 1):
    an[n - 1] = (1 / T) * np.trapz(square_wave(x) * np.cos(2 * np.pi * n * x / T), x)
    bn[n - 1] = (1 / T) * np.trapz(square_wave(x) * np.sin(2 * np.pi * n * x / T), x)


# Plot the original function and the Fourier approximation
plt.figure()
plt.plot(x, square_wave(x), label="Original Function")
plt.plot(x, F, label="Fourier Approximation")
plt.legend()
plt.title("Fourier Approximation of a Square Wave")
plt.show()
