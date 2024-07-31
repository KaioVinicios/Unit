import os
import pandas as pd
import time

if os.path.exists('db.xlsx'):
    dataframe = pd.read_excel('db.xlsx')
else:
    dataframe = pd.DataFrame(columns=['Nome', 'Idade', 'Curso'])

def menu():
    os.system('clear')
    print('Bem vindo ao menu!\nEscolha uma opção para continuar.\n[1]- Cadastrar aluno\n[2]- Exibir os alunos cadastrados\n[3]- Atualizar dados de um aluno\n[4]- Excluir um aluno\n[5]- Fechar sistema')
    opcao = input('Digite uma opção do menu: ')
    while opcao not in ['1','2','3','4','5']:
        print('Opção inválida, tente novamente.')
        opcao = input('Digite uma opção do menu: ')
    os.system('clear')
    if opcao == '1':
        cadastrar_aluno()
        menu()
    elif opcao == '2':
        exibir_alunos()
        input('Pressione Enter para sair.')
        menu()
    elif opcao == '3':
        atualizar_alunos()
        menu()
    elif opcao == '4':
        excluir_aluno()
        menu()
    elif opcao == '5':
        salvar_no_bd(dataframe)
        return print('Até logo!')
   
def cadastrar_aluno():
    nome = input('Digite o nome do aluno: ')
    idade = input('Digite a idade do aluno: ')
    curso = input('Digite o curso do aluno: ')
    global dataframe
    dataframe = pd.concat([dataframe, pd.DataFrame({'Nome': [nome], 'Idade': [idade], 'Curso': [curso]})], ignore_index=True)
    print("Cadastro realizado com sucesso!")
    time.sleep(3)

def exibir_alunos():
    print('Alunos cadastrados: ')
    for id, row in dataframe.iterrows():
        print(f'id: {id} - Aluno: {row["Nome"]} - Idade: {row["Idade"]} - Curso: {row["Curso"]}')

def atualizar_alunos():
    print('Atualizar aluno:')
    exibir_alunos()
    id = int(input('Qual o id do aluno que deseja alterar os dados? '))
    atributo = input(f'Atributos encontrados {dataframe.columns.tolist()}\n Qual atributos acima deseja alterar ? ')
    while atributo not in dataframe.columns:
        atributo = input(f'Atributo inválido, por favor digite o atributo exatamente como apresentado a seguir: {dataframe.columns.tolist()}: ')
    novo_valor = input(f'Qual o novo valor que o atributo {atributo} deve receber ? ')
    if atributo == 'Idade':
        novo_valor = int(novo_valor)
    dataframe.at[id, atributo] = novo_valor
    print(f'{atributo} atualizado para {novo_valor} com sucesso!')
    time.sleep(3)

def excluir_aluno():
    print('Excluir aluno:')
    exibir_alunos()
    id = int(input('Qual o id do aluno que deseja excluir os dados? '))
    global dataframe
    dataframe = dataframe.drop(index=id).reset_index(drop=True)
    print('Dados excluídos com sucesso!')
    time.sleep(3)

def salvar_no_bd(dados):
    dados.to_excel('db.xlsx', index=False)

menu()
