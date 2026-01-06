import pandas as pd
import math

# Leitura da planilha Dados_cliente1 (FATURA)
df_fatura = pd.read_excel('./data/raw/Dados_cliente.xlsx')

# Leitura da planilha Dados_cliente1 (INFORMACOES)
df_informacoes = pd.read_excel('./data/raw/Dados_cliente.xlsx', sheet_name=1)

# Leitura da planilha HSP-RS
df_hsp = pd.read_excel('./data/raw/HSP-RS.xlsx')


# Cria nova coluna para remover os valores máximo e mínimo
df_fatura['CONSUMO (KWH) APARADO'] = df_fatura['CONSUMO (KWH)']

# Valor max = 0
max_index = df_fatura['CONSUMO (KWH) APARADO'].idxmin()
df_fatura.loc[max_index, 'CONSUMO (KWH) APARADO'] = 0

#Valor min = 0
min_index = df_fatura['CONSUMO (KWH) APARADO'].idxmax()
df_fatura.loc[min_index, 'CONSUMO (KWH) APARADO'] = 0

# Calcula média aparada desconsiderando linhas com consumo = 0 
consumo_medio = df_fatura[df_fatura['CONSUMO (KWH) APARADO'] != 0] ['CONSUMO (KWH) APARADO'].mean()
print('Consumo médio mensal:',consumo_medio,'kWh')


# Calcula media de consumo diária 
consumo_medio_diario = consumo_medio / 30

# Define o valor de horas de sol pleno comparando a lista de horas do RS com a cidade do cliente
hsp = df_hsp.loc[df_hsp['CIDADE'].isin(df_informacoes['CIDADE']), 'HSP'].item()

# Fórmula para calcular a capacidade do sistema (20% de perda)
capacidade_sistema_kwp = consumo_medio_diario / (hsp * 0.8)

print('Horas de sol pleno:',hsp)
print(f'Capacidade do sistema: {capacidade_sistema_kwp:.2f} kWp')