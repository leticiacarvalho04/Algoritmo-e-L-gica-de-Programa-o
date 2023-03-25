n = int(input('Digite n: '))
x = range(n, n+1, n+2)
for i in range(n, n + 1, n + 2):
        if n == x:
            print('O valor inserido é um triângulo')
        else:
            print(f'O valor {n} não é um triângulo')
