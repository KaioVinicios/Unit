import pandas as pd


# a)
df = pd.read_excel('transacoes.xlsx')

# b)
df['saldo_acumulado'] = df['valor'].cumsum()

# c)
despesas = df[df['valor'] < 0]
top_despesas = despesas.groupby('categoria')['valor'].sum().sort_values().head(5).reset_index()

# d)
df['data'] = pd.to_datetime(df['data'])
df['mes'] = df['data'].dt.to_period('M')
soma_mensal = df.groupby('mes')['valor'].sum().reset_index()

# e)
df[['data', 'descricao', 'valor', 'categoria', 'saldo_acumulado']].to_excel('saldo_acumulado.xlsx', index=False)
top_despesas.to_excel('top_despesas.xlsx', index=False)
soma_mensal.to_excel('soma_mensal_transacoes.xlsx', index=False)
