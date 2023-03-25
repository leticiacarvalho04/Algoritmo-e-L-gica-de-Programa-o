a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
amaior = c < a > b
bmaior = a < b > c
cmaior = a < c > b
amenor = c > a < b
bmenor = a > b < c
if amaior:
    print('O maior número é ', a)
elif amenor:
    print('O menor número é ', a)
if bmaior:
    print('O maior número é ', b)
elif bmenor:
    print('O menor número é ', b)
if cmaior:
    print('O maior número é ', c)
else:
    print('O menor número é ', c)
