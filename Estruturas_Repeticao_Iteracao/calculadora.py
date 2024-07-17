n1 = float(input("Primeiro digito: ")) 
O1 = input("Operadores Aritméticos (+,-,*,/): ") 
n2 = float(input("Segundo digito: ")) 


match O1:
    case "+":
        print(n1+n2)
    case "-":
        print(n1-n2)
    case"*":
        print(n1*n2)
    case "/":
        print(n1/n2)
    case _:
        print("Operador incorreto, por favor, coloque um operador valido")