import pandas as pd

clientes_df = pd.read_excel('Pacientes.xlsx')

clientes_df.at[2, 'RG'] = '9876543'

clientes_df['Status'] = ['Ativo'] * len(clientes_df)


novos_clientes = pd.DataFrame({
    'Nome': ['Novo Cliente 1', 'Novo Cliente 2'],
    'Idade': [30, 45],
    'RG': ['1234567', '7654321']
})

clientes_df = pd.concat([clientes_df, novos_clientes], ignore_index=True)


cliente_mais_antigo = clientes_df['Idade'].idxmin()
clientes_df.at[cliente_mais_antigo, 'Status'] = 'Inativo'

clientes_df.to_excel('Pacientes_atualizado.xlsx', index=False)
