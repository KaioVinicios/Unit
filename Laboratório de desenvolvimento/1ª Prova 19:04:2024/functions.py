import json

def cadastrar_evento(agenda):
    titulo = input("Digite o título do evento: ")
    data = input("Digite a data do evento (DD/MM/AAAA): ")
    hora = input("Digite a hora do evento (HH:MM): ")
    descricao = input("Digite a descrição do evento: ")
    
    evento = {
        "titulo": titulo,
        "data": data,
        "hora": hora,
        "descricao": descricao
    }
    
    agenda.append(evento)
    print("Evento cadastrado com sucesso!")

def visualizar_agenda(agenda):
    if not agenda:
        print("Agenda vazia.")
    else:
        for i, evento in enumerate(agenda, 1):
            print(f"\nEvento {i}:")
            print("Título:", evento["titulo"])
            print("Data:", evento["data"])
            print("Hora:", evento["hora"])
            print("Descrição:", evento["descricao"])

def atualizar_evento(agenda):
    visualizar_agenda(agenda)
    if not agenda:
        return
    
    num_evento = int(input("Digite o número do evento que deseja atualizar: "))
    if num_evento < 1 or num_evento > len(agenda):
        print("Número de evento inválido.")
        return
    
    evento = agenda[num_evento - 1]
    print("\nAtualize os campos do evento (deixe em branco para manter o mesmo valor):")
    
    titulo = input("Novo título: ")
    if titulo:
        evento["titulo"] = titulo
    
    data = input("Nova data (DD/MM/AAAA): ")
    if data:
        evento["data"] = data
    
    hora = input("Nova hora (HH:MM): ")
    if hora:
        evento["hora"] = hora
    
    descricao = input("Nova descrição: ")
    if descricao:
        evento["descricao"] = descricao
    
    print("Evento atualizado com sucesso!")

def salvar_agenda(agenda):
    with open("agenda.txt", "w") as file:
        json.dump(agenda, file)
    print("Agenda salva com sucesso!")

def carregar_agenda():
    try:
        with open("agenda.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def main():
    agenda = carregar_agenda()
    
    while True:
        print("\n===== Menu =====")
        print("1. Cadastrar evento")
        print("2. Visualizar agenda")
        print("3. Atualizar evento")
        print("4. Salvar agenda")
        print("5. Encerrar programa")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_evento(agenda)
        elif opcao == "2":
            visualizar_agenda(agenda)
        elif opcao == "3":
            atualizar_evento(agenda)
        elif opcao == "4":
            salvar_agenda(agenda)
        elif opcao == "5":
            salvar_agenda(agenda)
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Escolha novamente.")

import json

def cadastrar_evento(agenda):
    titulo = input("Digite o título do evento: ")
    data = input("Digite a data do evento (DD/MM/AAAA): ")
    hora = input("Digite a hora do evento (HH:MM): ")
    descricao = input("Digite a descrição do evento: ")
    
    evento = {
        "titulo": titulo,
        "data": data,
        "hora": hora,
        "descricao": descricao
    }
    
    agenda.append(evento)
    print("Evento cadastrado com sucesso!")

def visualizar_agenda(agenda):
    if not agenda:
        print("Agenda vazia.")
    else:
        for i, evento in enumerate(agenda, 1):
            print(f"\nEvento {i}:")
            print("Título:", evento["titulo"])
            print("Data:", evento["data"])
            print("Hora:", evento["hora"])
            print("Descrição:", evento["descricao"])

def atualizar_evento(agenda):
    visualizar_agenda(agenda)
    if not agenda:
        return
    
    num_evento = int(input("Digite o número do evento que deseja atualizar: "))
    if num_evento < 1 or num_evento > len(agenda):
        print("Número de evento inválido.")
        return
    
    evento = agenda[num_evento - 1]
    print("\nAtualize os campos do evento (deixe em branco para manter o mesmo valor):")
    
    titulo = input("Novo título: ")
    if titulo:
        evento["titulo"] = titulo
    
    data = input("Nova data (DD/MM/AAAA): ")
    if data:
        evento["data"] = data
    
    hora = input("Nova hora (HH:MM): ")
    if hora:
        evento["hora"] = hora
    
    descricao = input("Nova descrição: ")
    if descricao:
        evento["descricao"] = descricao
    
    print("Evento atualizado com sucesso!")

def salvar_agenda(agenda):
    with open("agenda.txt", "w") as file:
        json.dump(agenda, file)
    print("Agenda salva com sucesso!")

def carregar_agenda():
    try:
        with open("agenda.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    