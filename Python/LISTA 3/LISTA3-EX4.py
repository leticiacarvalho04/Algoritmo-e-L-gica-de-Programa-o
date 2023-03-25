fn = int(input('Escreva o número de Fibonacci:'))
a,b = 1,1
contador = 1
while contador <= fn-2:
    a,b = b, a+b
    contador = contador + 1
print(b)
