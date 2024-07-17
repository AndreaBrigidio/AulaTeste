import requests

def verificar_frete_gratis(cep):
    estados_norte_nordeste = ["AC", "AL", "AM", "AP", "BA", "CE", "MA", "PA", "PB", "PE", "PI", "RN", "RO", "RR", "SE", "TO"]
    
    estado = cep[:2].upper()
    
    # Verificar se o estado está na lista de estados elegíveis
    if estado in estados_norte_nordeste:
        return True  # Elegível para frete grátis
    else:
        return False  # Não elegível para frete grátis

# Exemplo de uso
cep_usuario = input("Digite o CEP: ")
if verificar_frete_gratis(cep_usuario):
    print("Você tem frete grátis!")
else:
    print("Frete não grátis.")