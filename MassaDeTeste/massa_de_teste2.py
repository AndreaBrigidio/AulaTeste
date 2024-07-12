import pandas as pd

df = pd.read_csv('env\dados_ficticios.csv')

print(df.head())

filtro_idade = df['idade'] > 40
filtro_renda5000 = df['renda'] > 5000
filtro_renda15000 = df['renda'] > 15000

df_filtrado = df[filtro_idade & filtro_renda]

print(df_filtrado)


