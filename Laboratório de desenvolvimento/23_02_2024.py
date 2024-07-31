usuarios = []

def solicitar_informacoes():
    nome = input("Digite seu nome: ")
    sexo = 'qualquer'
    while sexo not in ["F", "M"]:
        sexo = input("Digite seu sexo: (F/M) ")
        if sexo not in ["F", "M"]:
            print('Dado inválido, por favor digite F para Feminino ou M para Masculino.')
    placa = input("Digite a placa do carro: ")
    km = int(input("Digite a quantidade de KMs contratados: "))
    dias = int(input("Digite a quantidade de dias contratados: "))
    usuarios.append([nome, sexo, placa, km, dias])

def calcular():
    dia_contratado = 70.00
    km_contratado = 0.10
    for u in usuarios:
        print("O valor total a ser cobrado é de R$", ((dia_contratado * u[4]) + (km_contratado * u[3])))

def media_km():
    media = [] 
    for u in usuarios:
        media.append(u[3])
    print(f'A média de clientes contratados é de {(max(media)/len(media))}KMs')

def cliente_f_maior7():
    especiais = []
    for u in usuarios:
        if u[1] == 'F' and u[4] > 7:
            especiais.append(u[0])
    print("As clientes que seguem as especificações de serem do sexo Feminino e ter contratado o serviço por mais de 7 dias são: ", ', '.join(especiais), '.')

decisao = ''
while decisao != 'SAIR':
    solicitar_informacoes()
    decisao = input('Se não deseja adicionar mais clientes digite "SAIR": ')
calcular()
media_km()
cliente_f_maior7()
