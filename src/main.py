import pandas as pd

# Leitura da planilha Dados_cliente1 (FATURA)
df_fatura = pd.read_excel('./data/raw/Dados_cliente1.xlsx')

# Leitura da planilha Dados_cliente1 (INFORMACOES)
df_informacoes = pd.read_excel('./data/raw/Dados_cliente1.xlsx', sheet_name=1)

# Leitura da planilha HSP-RS
df_hsp = pd.read_excel('./data/raw/HSP-RS.xlsx')



# Calcular a media de consumo do cliente
media_consumo = df_fatura['CONSUMO (KWH)'].mean()

# Definir a potencia do painel escolhido pelo cliente
potencia_painel = df_informacoes['PAINEL (W)'].max()