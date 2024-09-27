import math

def funcao(x):
    return 2*x*(math.e**x) - 3

def derivada(x):
    return 2*(math.e**x) + 2*x * math.e**x


def bisseccao(xa, xb, precisao):  # OK
    # if not(funcao(xa) * funcao(xb) < 0):  
    #     xa = float(input('Digite um novo valor para Xa: '))
    #     xb = float(input('Digite um novo valor para Xb: '))

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
    print(f'Raiz encontrada: {x}')


def secante(x, x1, precisao):
    while abs(funcao(x1)) > precisao:  
        x_novo = x1 - (funcao(x1) * (x1 - x)) / (funcao(x1) - funcao(x))
        if abs(x_novo - x1) < precisao:
            break
        x, x1 = x1, x_novo  
    print(f'Raiz encontrada: {x1}')


bisseccao(xa=3, xb=10, precisao=0.00001)
newton(3, 0.00001)
secante(2, 1, precisao=0.00001)
