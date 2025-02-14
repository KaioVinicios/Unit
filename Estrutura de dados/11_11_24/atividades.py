# 02
# Criação de um dicionário
meu_dicionario = {}
meu_dicionario['nome'] = 'João'
meu_dicionario['idade'] = 25

# Recuperação de um valor
print(meu_dicionario['nome'])  # Saída: João

# Remoção de um valor
del meu_dicionario['idade']

# O que acontece se você tentar acessar uma chave inexistente?
# R: Gera um KeyError.
try:
    print(meu_dicionario['idade'])  # Tentando acessar uma chave inexistente
except KeyError:
    print("Chave 'idade' não encontrada.")  # Tratamento do erro

# Como você pode verificar se uma chave existe antes de acessá-la?
# R: Usando o operador `in`.
if 'idade' in meu_dicionario:
    print(meu_dicionario['idade'])
else:
    print("A chave 'idade' não existe.")

print("\n")

# 03
# Criação de uma tabela hash simples
tabela_simples = [None] * 5

def hash_simples(chave):
    return len(chave) % 5  # Função hash simplificada

# Inserção de valores
tabela_simples[hash_simples('maçã')] = 'fruta vermelha'
tabela_simples[hash_simples('banana')] = 'fruta amarela'

print(tabela_simples)  # Pode haver colisões dependendo da função hash

# Simulação de colisões
tabela_simples[hash_simples('uva')] = 'fruta roxa'  # Pode sobrescrever
print(tabela_simples)

# O que acontece quando duas chaves geram o mesmo índice?
# R: Uma colisão ocorre, e o valor existente pode ser sobrescrito se não houver um mecanismo de resolução.

# Como podemos lidar com esse problema?
# R: Podemos usar encadeamento (listas ligadas em cada índice) ou sondagem (linear ou quadrática).

print("\n")

# 04
class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return len(key) % self.size

    def put(self, key, value):
        index = self.hash_function(key)
        if not self.table[index]:
            self.table[index] = []
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash_function(key)
        if self.table[index]:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
        return None

    def remove(self, key):
        index = self.hash_function(key)
        if self.table[index]:
            for i, pair in enumerate(self.table[index]):
                if pair[0] == key:
                    self.table[index].pop(i)
                    return True
        return False

# Testando os métodos
ht = HashTable()
ht.put("maçã", "fruta vermelha")
ht.put("banana", "fruta amarela")
print(ht.get("maçã"))  # Saída: fruta vermelha
ht.remove("banana")
print(ht.get("banana"))  # Saída: None

print("\n")

# 05
class HashTableCollision:
    def __init__(self, size=5):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return len(key) % self.size

    def put_linear(self, key, value):
        index = self.hash_function(key)
        for i in range(self.size):
            idx = (index + i) % self.size
            if not self.table[idx]:
                self.table[idx] = (key, value)
                return
        raise Exception("Tabela cheia")

    def put_quadratic(self, key, value):
        index = self.hash_function(key)
        for i in range(self.size):
            idx = (index + i**2) % self.size
            if not self.table[idx]:
                self.table[idx] = (key, value)
                return
        raise Exception("Tabela cheia")

# Testando sondagem linear e quadrática
htc = HashTableCollision()
htc.put_linear("maçã", "fruta vermelha")
htc.put_linear("banana", "fruta amarela")
print(htc.table)

htc_quadratic = HashTableCollision()
htc_quadratic.put_quadratic("maçã", "fruta vermelha")
htc_quadratic.put_quadratic("banana", "fruta amarela")
print(htc_quadratic.table)

# Como as colisões afetam o tempo de busca e inserção?
# R: Colisões aumentam o tempo de busca e inserção, pois o algoritmo precisa percorrer índices adicionais.

# Qual método de resolução de colisões parece mais eficiente?
# R: Encadeamento para grandes volumes de dados; sondagem quadrática para tabelas menores.

print("\n")

# 06
class ResizingHashTable:
    def __init__(self, initial_size=5, load_factor=0.7):
        self.size = initial_size
        self.table = [None] * initial_size
        self.num_elements = 0
        self.load_factor = load_factor

    def hash_function(self, key):
        return len(key) % self.size

    def put(self, key, value):
        if self.num_elements / self.size > self.load_factor:
            self.resize()
        index = self.hash_function(key)
        for i in range(self.size):
            idx = (index + i) % self.size
            if not self.table[idx] or self.table[idx][0] == key:
                self.table[idx] = (key, value)
                self.num_elements += 1
                return

    def resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size
        self.num_elements = 0
        for item in old_table:
            if item:
                self.put(item[0], item[1])

# Testando redimensionamento
rht = ResizingHashTable()
for i in range(50):
    rht.put(f"chave{i}", f"valor{i}")

print(rht.size)  # Tamanho após redimensionamento

# O que acontece quando o redimensionamento ocorre?
# R: O tamanho da tabela dobra e os elementos são re-hashados para suas novas posições.

# Como o tempo de busca e inserção muda antes e depois do redimensionamento?
# R: Antes, o tempo aumenta devido ao aumento de colisões. Depois, ele diminui devido à redução de colisões.