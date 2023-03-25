a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
amaior = c < a > b
bmaior = a < b > c
cmaior = a < c > b
if amaior:
    print('O maior número é ', a)
if bmaior:
    print('O maior número é ', b)
if cmaior:
    print('O maior número é ', c)
    
