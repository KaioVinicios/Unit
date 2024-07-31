def ValorPagamento(valorPrestacao, diasEmAtraso = 0):
    if diasEmAtraso != 0:
        valorPrestacao += (valorPrestacao * 0.03) + (valorPrestacao * (0.001 * diasEmAtraso))
    return valorPrestacao
    

def relatorio(prestacoes):
    return f"O valor total arrecadado foi de R${sum(prestacoes):.2f} em {len(prestacoes)} prestações diferentes."


prestacoes = []
while True:
    valor = int(input("OBS -> Digite 0 para encerrar e exibir o relatório.\nDigite o valor da prestação: "))
    if valor == 0:
        break
    
    diasDeAtraso = int(input("Digite o número de dias em atraso: "))
    prestacoes.append(ValorPagamento(valor, diasDeAtraso))
    
print(relatorio(prestacoes))
