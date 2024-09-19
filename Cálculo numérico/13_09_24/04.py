import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, bisect


r = 2  # raio em metros
L = 5  # comprimento em metros
V_given = 8  # volume em metros cúbicos



def volume_function(h, r, L):
    term1 = r**2 * np.arccos((r - h) / r)
    term2 = (r - h) * np.sqrt(2 * r * h - h**2)
    return (term1 - term2) * L



def objective_function(h, r, L, V_given):
    return volume_function(h, r, L) - V_given


h_min, h_max = 0, 2  
tolerance = 1e-5


h_bissection = bisect(objective_function, h_min, h_max,
                      args=(r, L, V_given), xtol=tolerance)


h_newton = newton(objective_function, x0=1.5,
                  args=(r, L, V_given), tol=tolerance)

print(f"Altura obtida (Método da bisseção): {h_bissection:.5f} m")
print(f"Altura obtida (Método de Newton): {h_newton:.5f} m")
