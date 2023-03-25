a = int(input('Digite a: '))
b = int(input('Digite b: '))
while a%b != 0:
    a,b = b,a%b
print(f'mdc: {b}')
