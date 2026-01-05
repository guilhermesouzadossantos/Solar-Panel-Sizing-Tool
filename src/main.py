import pandas as pd

# LEITURA DE DADOS

# Leitura da planilha Dados_cliente1 (FATURA)
df_fatura = pd.read_excel('./data/raw/Dados_cliente1.xlsx')

# Leitura da planilha Dados_cliente1 (INFORMACOES)
df_informacoes = pd.read_excel('./data/raw/Dados_cliente1.xlsx', sheet_name=1)

# Leitura da planilha HSP-RS
df_hsp = pd.read_excel('./data/raw/HSP-RS.xlsx')


# CALCULAR MÉDIA APARADA COM BASE EM UMA NOVA COLUNA

# Cria nova coluna para remover os valores máximo e mínimo
df_fatura['CONSUMO (KWH) APARADO'] = df_fatura['CONSUMO (KWH)']

# Valor max = 0
max_index = df_fatura['CONSUMO (KWH) APARADO'].idxmin()
df_fatura.loc[max_index, 'CONSUMO (KWH) APARADO'] = 0

#Valor min = 0
min_index = df_fatura['CONSUMO (KWH) APARADO'].idxmax()
df_fatura.loc[min_index, 'CONSUMO (KWH) APARADO'] = 0

# Calcula média aparada desconsiderando linhas com consumo = 0 
print(df_fatura[df_fatura['CONSUMO (KWH) APARADO'] != 0] ['CONSUMO (KWH) APARADO'].mean())