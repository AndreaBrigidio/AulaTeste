import pandas as pd

# Dados fornecidos
dados = {
    "Nome": ["Ana", "Carlos", "Maria", "Pedro", "João", "Lúcia", "Rafael"],
    "Idade": [28, 35, 42, 19, 56, 30, 24],
    "Cidade": ["Recife", "Salvador", "Recife", "São Paulo", "Salvador", "Manaus", "Recife"],
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Filtrando os moradores do Recife
moradores_recife = df[df["Cidade"] == "Recife"]

# Exibindo os moradores do Recife
print(moradores_recife)