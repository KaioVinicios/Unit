# Definição dos personagens
personagens = ["Pai", "Mãe", "Filho1", "Filho2", "Filha1", "Filha2", "Policial", "Prisioneiro"]

# Estados iniciais
lado_esquerdo = set(personagens)
lado_direito = set()
barco = set()
historico = []
lado_barco = "esquerdo"

# Função para verificar se a travessia é válida
def validar_estado(lado):
    if "Mãe" in lado and ("Filho1" in lado or "Filho2" in lado) and "Pai" not in lado:
        print("Mãe não pode ficar sozinha com os filhos.")
    if "Pai" in lado and ("Filha1" in lado or "Filha2" in lado) and "Mãe" not in lado:
        print("Pai não pode ficar sozinho com as filhas.")
    if "Prisioneiro" in lado and any(p in lado for p in ["Pai", "Mãe", "Filho1", "Filho2", "Filha1", "Filha2"]) and "Policial" not in lado:
        print("Prisioneiro não pode ficar sozinho com ninguém sem o policial.")
    else:
        return True
    return False

# Função para realizar uma travessia
def atravessar(passageiros):
    global lado_esquerdo, lado_direito, barco, lado_barco
    
    if len(passageiros) > 2:
        print("Erro: O barco só pode transportar até duas pessoas.")
        return
    if not any(p in passageiros for p in ["Pai", "Mãe", "Policial"]):
        print("Erro: O barco precisa de um piloto (Pai, Mãe ou Policial).")
        return
    
    lado_atual = lado_esquerdo if passageiros[0] in lado_esquerdo else lado_direito
    lado_oposto = lado_direito if lado_atual == lado_esquerdo else lado_esquerdo
    
    if not all(p in lado_atual for p in passageiros):
        print("Erro: Um ou mais passageiros não estão no lado correto do rio.")
        return
    
    # Simular a movimentação
    for p in passageiros:
        lado_atual.remove(p)
        barco.add(p)
    
    if not validar_estado(lado_atual):
        print("Erro: Essa movimentação deixa um grupo em situação inválida.")
        for p in passageiros:
            lado_atual.add(p)  # Reverte a mudança
        barco.clear()
        return
    
    # Movendo os passageiros para o lado oposto
    for p in passageiros:
        lado_oposto.add(p)
    
    # Atualizar os estados globais
    if lado_atual == lado_esquerdo:
        lado_direito = lado_oposto
        lado_esquerdo = lado_atual
        lado_barco = "direito"
    else:
        lado_esquerdo = lado_oposto
        lado_direito = lado_atual
        lado_barco = "esquerdo"
    
    barco.clear()
    historico.append((set(lado_esquerdo), set(lado_direito)))
    
    print(f"Travessia bem-sucedida: {passageiros} foram para o outro lado.")
    print(f"O barco agora está no lado {lado_barco}.")
    verificar_vitoria()

# Função para verificar se todos chegaram ao lado direito
def verificar_vitoria():
    if lado_direito == set(personagens):
        print("Seu histórico de travessias: " + "".join(str(item) for item in historico))
        print("Parabéns! Todos atravessaram o rio com segurança.")
        exit()

# Loop principal
while True:
    print("\nLado Esquerdo:", lado_esquerdo)
    print("Lado Direito:", lado_direito)
    print(f"O barco está no lado {lado_barco}.")
    print("Quem deseja atravessar? (Digite dois nomes separados por vírgula)")
    entrada = input(">> ").strip().split(",")
    passageiros = [p.strip() for p in entrada if p.strip() in personagens]
    atravessar(passageiros)
    