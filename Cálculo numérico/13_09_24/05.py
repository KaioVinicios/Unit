import math

def funcao(t):
    return (9*math.e**-t * math.sin(2*math.pi*t) - 3.5) # OK

def derivada(t):
    return 9*(6.2318*math.e**-t * math.cos(6.2318*t) - math.e**-t * math.sin(6.2318*t))

def bisseccao(xa, xb, precisao):
    if not(funcao(xa) * funcao(xb) < 0):  # OK
        xa = float(input('Digite um novo valor para Xa: '))
        xb = float(input('Digite um novo valor para Xb: '))
    
    xm = (xa + xb) / 2    
    while abs(funcao(xm)) > precisao:
        xm = (xa + xb) / 2
        if funcao(xa) * funcao(xm) < 0:
            xb = xm
        else:
            xa = xm
        print(xa, xb)
    return print(f"Raiz encontrada x == {xm}")

def newton(x, precisao):
    while abs(funcao(x)) >= precisao:
        x_novo = x - funcao(x) / derivada(x)
        if abs(x_novo - x) < precisao:  
            break
        x = x_novo  
    print(f'Raiz encontrada: {x}')

bisseccao(xa=0.1, xb=0.8, precisao=0.00001)
newton(0.3, 0.00001)