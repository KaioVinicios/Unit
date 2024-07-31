from functions import *

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

main()
