import math

def funcao(h):
    return math.pi * h**2 * ((3 * 3 - h) / 3) - 30 # OK

def derivada(h):
    return math.pi*h*(-h + 6)

def bisseccao(xa, xb, precisao):
    if not(funcao(xa) * funcao(xb) < 0): 
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


bisseccao(xa=8, xb=9, precisao=0.00001)
newton(1, 0.00001)