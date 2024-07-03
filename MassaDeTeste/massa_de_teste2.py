import pandas as pd

# Carregando o arquivo CSV em um DataFrame
df = pd.read_csv('env\dados_ficticios.csv')

#Exibindo as primeiras linhas do DataFrame
print(df.head())

filtro_idade = df['idade'] > 40
filtro_renda5000 = df['renda'] > 5000
filtro_renda15000 = df['renda'] > 15000

df_filtrado = df[filtro_idade & filtro_renda]

# Exibindo o DataFrame filtrado
print(df_filtrado)


