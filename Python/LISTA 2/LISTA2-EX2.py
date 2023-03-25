def isleap(ano):
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)
ano = int(input("Qual o ano em questão? "))
if ano == 4:
    print('O ano em questão é um ano bissexto')
else:
    print('O ano em questão NÃO é bissexto')
