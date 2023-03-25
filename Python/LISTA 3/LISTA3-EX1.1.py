n = int(input('Escreva um número entre 0 e 10: '))
d = 0 <= n <= 10
if n == d:
    print('Valor válido')
else:
    while n != d:
        print('Número inválido! Digite novamente')
        print(n = int(input('Escreva um número entre 0 e 10: ')))
        if n == d:
            print('Valor válido')
            
    
