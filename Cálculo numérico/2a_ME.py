import math
from funcoes_2a_unidade import simpsons_rule, trapezoidal_rule
def funcao(x):
    return ((math.e**x)*math.sin(x))/1+x**2
a=0
b=2
n1=1
n2=5
n3=20

# print(simpsons_rule(funcao, a, b, n1)) 
# print(simpsons_rule(funcao, a, b, n2))
print(simpsons_rule(funcao, a, b, n3))

print(trapezoidal_rule(funcao, a, b, n1))
print(trapezoidal_rule(funcao, a, b, n2))
print(trapezoidal_rule(funcao, a, b, n3))
