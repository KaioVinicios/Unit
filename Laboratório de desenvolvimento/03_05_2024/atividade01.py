import pandas

arquivo = pandas.read_excel('Pacientes.xlsx')

print(arquivo.loc[0:1])
print(arquivo.loc[0: , ['Nome', 'CPF']])
print(arquivo.loc[arquivo['Naturalidade'] == 'Aracaju'])
# arquivo.loc[len(arquivo)] = [1231121642, 'kaio', '08052005', 333, 'Aracaju']