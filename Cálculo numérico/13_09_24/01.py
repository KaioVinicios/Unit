import math

P = 35000  # valor do veículo
A = 8500   # pagamentos anuais
n = 7      # número de anos

def funcao(i):
    return P * (i * (1 + i)**n) / ((1 + i)**n - 1) - A

def derivada(i):
    term1 = (1 + i)**n
    return P * (term1 * (term1 - 1) - n * i * (1 + i)**(n - 1)) / ((term1 - 1)**2)

def bisseccao(xa, xb, precisao):
    if not(funcao(xa) * funcao(xb) < 0):  
        xa = float(input('Digite um novo valor para Xa: '))
        xb = float(input('Digite um novo valor para Xb: '))
    
    while abs(xb - xa) >= precisao:  
        xm = (xa + xb) / 2
        if abs(funcao(xm)) < precisao:  
            return print(f'{xm} = raiz')
        if funcao(xa) * funcao(xm) < 0:
            xb = xm
        else:
            xa = xm
    return print(f'Raiz encontrada: {xm}')


def newton(x, precisao):
    while abs(funcao(x)) >= precisao:
        x_novo = x - funcao(x) / derivada(x)
        if abs(x_novo - x) < precisao:  
            break
        x = x_novo  
    print(f'Raiz encontrada: {x}')



bisseccao(xa=0.01, xb=0.2, precisao=0.00001)
newton(0.1, 0.00001)
