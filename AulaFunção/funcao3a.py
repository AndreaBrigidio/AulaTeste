def verificar_grupo(numero_matricula):
    if numero_matricula % 2 == 0:
        return "VOCÊ ESTÁ NO TIME AZUL"
    else:
        return "VOCÊ ESTÁ NO TIME AMARELO"

numero_matricula = int(input("Digite o número da matrícula: "))
mensagem = verificar_grupo(numero_matricula)
print(mensagem)