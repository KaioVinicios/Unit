print("Exercício 1 - Variáveis e Tipos de Dados")
int_var = 42
float_var = 3.14
string_var = "Olá, Python!"
print(f"int_var: Valor={int_var}, Tipo={type(int_var)}")
print(f"float_var: Valor={float_var}, Tipo={type(float_var)}")
print(f"string_var: Valor='{string_var}', Tipo={type(string_var)}")
print()

print("Exercício 2 - Operadores e Condicionais")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num1 > num2:
    maior = num1
    diferenca = num1 - num2
else:
    maior = num2
    diferenca = num2 - num1
print(f"O maior número é {maior}. Diferença entre eles: {diferenca}")
print()

print("Exercício 3 - Loops e Estruturas de Controle 1")
soma = 0
for i in range(1, 11):
    soma += i
    print(f"Número: {i}, Soma acumulada: {soma}")
print()

print("Exercício 4 - Loops e Estruturas de Controle 2")
numeros = []
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
media = sum(numeros) / len(numeros)
print(f"A média dos números é: {media}")
print()

print("Exercício 5 - Array")
array = [10, 20, 30, 40, 50]
print(f"Array inicial: {array}")
array.pop()  
array.pop(0) 
print(f"Array após remoções: {array}")
print()

print("Exercício 6 - Pilha")
pilha = []
for elem in [100, 200, 300, 400, 500]:
    pilha.append(elem)
print(f"Pilha inicial: {pilha}")
pilha.pop()  
pilha.pop()  
print(f"Pilha após remoções: {pilha}")
print()


print("Exercício 7 - Fila")
from collections import deque
fila = deque(["A", "B", "C", "D", "E"])
print(f"Fila inicial: {fila}")
fila.popleft() 
fila.append("F")  
print(f"Fila após operações: {fila}")
print()


print("Exercício 8 - Lista Ligada")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_first(self):
        if self.head:
            self.head = self.head.next

    def remove_last(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next and current.next.next:
            current = current.next
        current.next = None

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements

lista_ligada = LinkedList()
for elem in [11, 22, 33, 44, 55]:
    lista_ligada.append(elem)
print(f"Lista ligada inicial: {lista_ligada.display()}")
lista_ligada.remove_first()
lista_ligada.remove_last()
print(f"Lista ligada após remoções: {lista_ligada.display()}")