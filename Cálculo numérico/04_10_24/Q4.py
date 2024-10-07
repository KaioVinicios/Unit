import math

g = 9.8
m = 110
v = 40
t = 7
# c == ?

def funcao(c):
    return (g * m * (1 - math.exp(-t * (c/m)))) / c - 40
    

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


bisseccao(xa=15, xb=20, precisao=10e-6) # 18.80674362...
