a = int(input("Digite o valor do lado 1 de um triângulo: "))
b = int(input("Digite o valor do lado 2 de um triângulo: "))
c = int(input("Digite o valor do lado 3 de um triângulo: "))
if a<b+c and b<a+c and c<a+b:
    if a==b==c:
        print('Seu triângulo é um equilátero')
    elif a==b or b==c or c==a:
        print('Seu triângulo é isósceles')
    else:
        print('Seu triângulo é escaleno')
else:
    print("A forma informada não se trata de um triângulo")
