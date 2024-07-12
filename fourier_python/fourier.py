import sympy as sym
from sympy import pi

x = sym.symbols('x')
n = 5                  #no of terms
k = 3                   #no of cycles

def fourier(function, L, R, n = 3, k = 2):
    ser = sym.fourier_series(function, (x, L, R))
    print(ser.truncate(n))
    sym.plot(ser.truncate(n),(x, k * -pi, k * pi))
    
# L = -pi
# R = pi
# square_wave = sym.Piecewise((-1, x < 0),(1, x > 0))
# fourier(square_wave, L, R)

# L = 0
# R = 2*pi
# saw_tooth_wave = -(5/pi)* x + 5
# fourier(saw_tooth_wave, L, R)

# L = 0
# R = pi
# full_wave_rectifier = sym.sin(x)
# fourier(full_wave_rectifier, L, R)

L = -pi
R = pi
y = x
fourier(y, L, R)

