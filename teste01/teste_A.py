import requests
cep = input("Qual é o seu cep?")

response = requests.get (f'https://viacep.com.br/ws/{cep}/json/')

data = response.json()
print(f'O logardouro dessa chamada é', data['logradouro'])