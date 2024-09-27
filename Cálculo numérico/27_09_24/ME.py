# Alunos: Kaio Vinícios e João Vitor Lyra.

import math

math.log

def funcao(t):
    return (1800 * math.log(160000 / (160000 - 2600*t))- 9.81*t) - 750

def derivada(t):
    return (23400 / (-13 * t + 800)) - 9.81
    

def bisseccao(xa, xb, precisao): 
    if funcao(xa) * funcao(xb) > 0:
        print('\nATENÇÃO! f(Xa) * f(Xb) > 0\nO intervalo [Xa, Xb] fornecido PODE ou NÃO conter uma raiz segundo o teorema de Bolzano.\n')

    while abs(xb - xa) >= precisao:  
        xm = (xa + xb) / 2
        if abs(funcao(xm)) < precisao:  
            return print(f'Raiz = {xm};')
        if funcao(xa) * funcao(xm) < 0:
            xb = xm
        else:
            xa = xm
    return print(f'Raiz encontrada: {xm};')


def newton(x, precisao):
    while abs(funcao(x)) >= precisao:
        x_novo = x - funcao(x) / derivada(x)
        if abs(x_novo - x) < precisao:  
            break
        x = x_novo  
    print(f'Raiz encontrada: {x};')

bisseccao(20, 30, 10e-10)
newton(25, 10e-10)