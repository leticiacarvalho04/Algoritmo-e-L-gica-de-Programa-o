peso = int(input('Quantos quilos de peixe você está portando? '))
if peso > 50:
    multa = 4*peso
    print('Você ultrapassou o limite e deverá pagar uma multa de R$',multa)
else:
    print('Não houve excesso de peso')
