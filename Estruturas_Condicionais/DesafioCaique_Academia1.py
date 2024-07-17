dias = int (input('Quantos dias de frequencia você tem?: '))

if dias == 21:
    print('UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ')

elif dias <= 21 and dias > 1:
    print('VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO')

else:
    frequencia = (input('Você faltou ontem [y/n]: '))

if frequencia == 'y':
    print('QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO')

elif frequencia == 'n': print('VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO')