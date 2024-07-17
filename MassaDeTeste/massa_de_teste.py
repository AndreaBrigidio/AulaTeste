import pandas as pd

dados = {
    "Nome": ["Ana", "Carlos", "Maria", "Pedro", "João", "Lúcia", "Rafael"],
    "Idade": [28, 35, 42, 19, 56, 30, 24],
    "Cidade": ["Recife", "Salvador", "Recife", "São Paulo", "Salvador", "Manaus", "Recife"],
}

df = pd.DataFrame(dados)

moradores_recife = df[df["Cidade"] == "Recife"]

print(moradores_recife)