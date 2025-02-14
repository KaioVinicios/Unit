# 01, 02  
conjunto1 = {2, 4, 6, 8, 10}
conjunto2 = {1, 3, 5, 7, 9}

print(conjunto1, conjunto2, conjunto1 & conjunto2, conjunto1 | conjunto2, conjunto1 - conjunto2)
# Conjunto final == conjunto resultante da operação

# 03, 04
conjunto3 = {1,2,3,4,5}
conjunto4 = {4,5,6,7,8}

print(conjunto3 & conjunto4, conjunto4 - conjunto3, conjunto3 - conjunto4)

# 05    
lista1 = [1,2,2,3,4,4,5]
conjunto_unicos = set(lista1)
print(conjunto_unicos)

# 06
# Conjunto imutável, conjunto de elementos onde não é posivel alteração a partir de sua definição.
conjunto_imutavel = frozenset(set([1,2,3,4,5]))
print(conjunto_imutavel)

# 07, 08
texto = "Eu amo muito o meu cachorro Obi. O nome dele é Obi porque eu amo muito Star Wars."
palavras = texto.lower().replace(".", "").replace(",", "").split()
conjunto_palavras_unicas = set(palavras)
print(conjunto_palavras_unicas)

cores = {"vermelho", "verde", "azul"}

cor_verificar = "amarelo"
if cor_verificar in cores:
    print(f"A cor '{cor_verificar}' já está no conjunto.")
else:
    print(f"A cor '{cor_verificar}' não está no conjunto. Adicionando agora...")
    cores.add(cor_verificar)

print(f"Conjunto final de cores: {cores}")