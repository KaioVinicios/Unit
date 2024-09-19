import numpy as np
import matplotlib.pyplot as plt

v0 = 30  # Velocidade inicial (m/s)
g = 9.81  # Aceleração gravitacional (m/s^2)
x_total = 90  # Distância horizontal total (m)
y0 = 1.8  # Altura inicial (m)
y_final = 1  # Altura final (m)
precision = 1e-5  # Precisão para o método de Newton e bissecção



def trajectory_eq(theta, x, v0, g, y0):
    return np.tan(theta) * x - (g / (2 * v0**2 * np.cos(theta)**2)) * x**2 + y0



def f(theta):
    return trajectory_eq(theta, x_total, v0, g, y0) - y_final



def df(theta):
    return (x_total / np.cos(theta)**2) - ((g * x_total**2) / (v0**2 * np.cos(theta)**3)) * np.sin(2 * theta)


def newton_method(f, df, theta0, tol):
    theta = theta0
    while abs(f(theta)) > tol:
        theta = theta - f(theta) / df(theta)
    return theta


def bisection_method(f, a, b, tol):
    while (b - a) / 2 > tol:
        midpoint = (a + b) / 2
        if f(midpoint) == 0:
            return midpoint
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2


theta_initial = np.radians(45)
theta_newton = newton_method(f, df, theta_initial, precision)

theta_bissection = bisection_method(f, 0, np.pi/2, precision)

x_vals = np.linspace(0, x_total, 500)
y_vals_newton = trajectory_eq(theta_newton, x_vals, v0, g, y0)
y_vals_bissection = trajectory_eq(theta_bissection, x_vals, v0, g, y0)
